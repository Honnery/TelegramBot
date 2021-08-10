import logging

from telegram import Update
from messengers.base_wrappers import BaseUserData

import databases
import process_answer
from containers import Container

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, user_data: BaseUserData):
    """
    For handler with command 'start'. Is Used to start conversation with bot.
    Clear context for previous conversation.
    Search for a new component.
    """
    user_data.clear_context()
    process_answer.find_new_answer(update, user_data)


def receive_answer(update: Update, user_data: BaseUserData):
    """
    Handle previous answer if it is exists.
    Search for a new answer.
    """
    process_answer.handle_prev_answer(update, user_data)
    process_answer.find_new_answer(update, user_data)


def main() -> None:
    container = Container()
    container.messenger_config.from_ini("../configs/telegram.ini")
    container.database_config.from_ini("../configs/database.ini")
    container.wire(modules=[process_answer, databases])
    messengers = container.messenger(start, receive_answer)
    messengers.start_polling()


if __name__ == '__main__':
    main()
