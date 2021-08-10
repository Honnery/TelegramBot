from telegram.ext import CallbackContext

from messengers.base_user_data import BaseUserData


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
