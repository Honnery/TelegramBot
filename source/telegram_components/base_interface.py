from telegram import Update, ReplyKeyboardRemove, ReplyMarkup
from telegram.ext import (
    CallbackContext
)
from typing import Optional, Any


class BaseComponent:

    def create_answer(self, nodes, update: Update, context: CallbackContext):
        node = nodes[0]
        input_desc = node["text"]
        context.user_data["context"]["param_name"] = node["param_name"]
        self._create_message(update, context, input_desc)
        context.user_data["prev_point_id"] = node.id

    def parse_answer(self, update: Update, context: CallbackContext) -> Optional[int]:
        pass

    @staticmethod
    def _create_message(update: Update, context: CallbackContext, text: str, reply_markup=ReplyKeyboardRemove()):
        if not update.message:
            query = update.callback_query
            context.bot.send_message(query.message.chat_id, text, reply_markup=reply_markup)

        update.message.reply_text(
            text,
            reply_markup=reply_markup,
        )


class AggregatedComponent(BaseComponent):
    def create_answer(self, nodes, update: Update, context: CallbackContext):
        node = nodes[0]
        # ToDo Update and check logic for issue with nodes
        input_desc = "ERROR "
        context.user_data["context"]["param_name"] = node["param_name"]
        self._create_message(update, context, input_desc)
        context.user_data["prev_point_id"] = node.id

    def create_reply_markup(self, nodes, update: Update, context: CallbackContext) -> Optional[Any]:
        pass
