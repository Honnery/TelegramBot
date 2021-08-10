from telegram import Update
from .base_wrappers import BaseApiWrapper, BaseUserData
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
        return TelegramUserData(context)

    def _create_update(self, update):
        return update


class TelegramUserData(BaseUserData):
    def __init__(self, context: CallbackContext):
        self._telegram_user_data = context.user_data
        self._user_bot = context.bot

    @property
    def prev_point_id(self):
        return self._telegram_user_data["prev_point_id"]

    @prev_point_id.setter
    def prev_point_id(self, new_prev_point_id):
        self._telegram_user_data["prev_point_id"] = new_prev_point_id

    @property
    def state(self):
        return self._telegram_user_data.get("state", None)

    @state.setter
    def state(self, new_state):
        self._telegram_user_data["state"] = new_state

    @property
    def context(self):
        return self._telegram_user_data["context"]

    @context.setter
    def context(self, new_context):
        self._telegram_user_data["context"] = new_context

    @property
    def properties(self):
        return self._telegram_user_data["properties"]

    @properties.setter
    def properties(self, new_properties):
        self._telegram_user_data["properties"] = new_properties

    def send_message(self, chat_id, text, reply_markup):
        self._user_bot.send_message(chat_id, text, reply_markup=reply_markup)


