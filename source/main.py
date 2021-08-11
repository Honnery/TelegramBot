import logging

import databases
import process_answer
from containers import Container
from databases import node_processing
from messengers.base_message_sender import BaseMessageSender
from messengers.base_user_data import BaseUserData

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(message_sender: BaseMessageSender, user_data: BaseUserData):
    """
    For handler with command 'start'. Is Used to start conversation with bot.
    Clear context for previous conversation.
    Search for a new component.
    """
    user_data.clear_context()
    process_answer.find_new_answer(message_sender, user_data)


def receive_answer(message_sender: BaseMessageSender, user_data: BaseUserData):
    """
    Handle previous answer if it is exists.
    Search for a new answer.
    """
    process_answer.handle_prev_answer(message_sender, user_data)
    process_answer.find_new_answer(message_sender, user_data)


def main() -> None:
    container = Container()
    container.messenger_config.from_ini("../configs/telegram.ini")
    container.database_config.from_ini("../configs/database.ini")
    container.wire(modules=[node_processing, databases])
    messengers = container.messenger(start, receive_answer)
    messengers.start_polling()


if __name__ == '__main__':
    main()
