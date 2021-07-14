from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    CallbackContext
)
from utils.user_context import clear_context
from typing import Optional, Any
from abc import ABC, abstractmethod


class BaseComponent(ABC):
    """
    Base class to represent required functions for components.
    """
    @abstractmethod
    def create_answer(self, node, update: Update, context: CallbackContext):
        pass

    def parse_answer(self, update: Update, context: CallbackContext) -> Optional[int]:
        pass

    @staticmethod
    def _create_message(text: str, update: Update, context: CallbackContext, reply_markup=ReplyKeyboardRemove(), ):
        if not update.message:
            query = update.callback_query
            context.bot.send_message(query.message.chat_id, text, reply_markup=reply_markup)
        else:
            update.message.reply_text(text, reply_markup=reply_markup)


class AggregatedComponent(BaseComponent):
    """
    Component that can be used as aggregated one
    """
    def create_answer(self, nodes, update: Update, context: CallbackContext):
        input_desc = "ERROR"
        self._create_message(input_desc, update, context)
        clear_context(context)

    @abstractmethod
    def create_reply_markup(self, nodes, update: Update, context: CallbackContext) -> Optional[Any]:
        pass
