from telegram import Update
from .base_wrappers import BaseApiWrapper
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)


class TelegramApiWrapper(BaseApiWrapper):
    def __init__(self, token, initial_start, initial_receive_answer):
        super().__init__(initial_start, initial_receive_answer)
        self.updater = Updater(token, use_context=True)
        self._attach_handlers(self.updater)

    def _attach_handlers(self, updater):
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start_conversation))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.receive_answer))
        dispatcher.add_handler(CallbackQueryHandler(self.receive_answer))

    def start_polling(self):
        self.updater.start_polling()
        self.updater.idle()

    def _create_user_context(self, context):
        return context

    def _create_update(self, update):
        return update



