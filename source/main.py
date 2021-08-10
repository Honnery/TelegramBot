import logging

from telegram import Update
from telegram.ext import (
    CallbackContext,
)

import databases
import process_answer
from containers import Container
from utils.user_context import clear_context

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    """
    For handler with command 'start'. Is Used to start conversation with bot.
    Clear context for previous conversation.
    Search for a new component.
    """
    context = clear_context(context)
    process_answer.find_new_answer(update, context)


def receive_answer(update: Update, context: CallbackContext):
    """
    Handle previous answer if it is exists.
    Search for a new answer.
    """
    process_answer.handle_prev_answer(update, context)
    process_answer.find_new_answer(update, context)


def main() -> None:
    container = Container()
    container.messenger_config.from_ini("../configs/telegram.ini")
    container.database_config.from_ini("../configs/database.ini")
    container.wire(modules=[process_answer, databases])
    messengers = container.messenger(start, receive_answer)
    messengers.start_polling()


if __name__ == '__main__':
    main()
