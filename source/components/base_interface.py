from telegram import Update, ReplyKeyboardRemove
from messengers.base_wrappers import BaseUserData
from typing import Optional, Any
from abc import ABC, abstractmethod


class BaseComponent(ABC):
    """
    Base class to represent required functions for components.
    """
    @abstractmethod
    def create_answer(self, node, update: Update, context):
        pass

    def parse_answer(self, update: Update, context) -> Optional[int]:
        pass

    @staticmethod
    def _create_message(text: str, update: Update, user_data: BaseUserData, reply_markup=ReplyKeyboardRemove(), ):
        if not update.message:
            query = update.callback_query
            user_data.send_message(query.message.chat_id, text, reply_markup)
        else:
            update.message.reply_text(text, reply_markup=reply_markup)


class AggregatedComponent(BaseComponent):
    """
    Component that can be used as aggregated one
    """
    def create_answer(self, nodes, update: Update, user_data: BaseUserData):
        input_desc = "ERROR"
        self._create_message(input_desc, update, user_data)
        user_data.clear_context()

    @abstractmethod
    def create_reply_markup(self, nodes, update: Update, user_data: BaseUserData) -> Optional[Any]:
        pass
