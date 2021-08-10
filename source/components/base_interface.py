from abc import ABC, abstractmethod
from typing import Optional, Any

from messengers.base_message_sender import BaseMessageSender
from messengers.base_user_data import BaseUserData


class BaseComponent(ABC):
    """
    Base class to represent required functions for components.
    """

    @abstractmethod
    def create_answer(self, node, message_sender: BaseMessageSender, context):
        pass

    def parse_answer(self, message_sender: BaseMessageSender, context) -> Optional[int]:
        pass


class AggregatedComponent(BaseComponent):
    """
    Component that can be used as aggregated one
    """

    def create_answer(self, nodes, message_sender: BaseMessageSender, user_data: BaseUserData):
        input_desc = "ERROR"
        message_sender.send_message(input_desc)
        user_data.clear_context()

    @abstractmethod
    def create_reply_markup(self, nodes, message_sender: BaseMessageSender, user_data: BaseUserData) -> Optional[Any]:
        pass
