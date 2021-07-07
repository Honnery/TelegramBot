import logging

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
CallbackQueryHandler,
)

from create_answers import find_new_answer
from parse_answer import handle_prev_answer
from settings import telegram_config
from utils.user_context import clear_context

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    context = clear_context(context)
    find_new_answer(update, context)


def receive_answer(update: Update, context: CallbackContext):
    handle_prev_answer(update, context)
    find_new_answer(update, context)


def main() -> None:
    updater = Updater(telegram_config.get("BOT_INFO", "token"), use_context=True)
    dispatcher = updater.dispatcher

    # attach Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_answer))
    dispatcher.add_handler(CallbackQueryHandler(receive_answer))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
