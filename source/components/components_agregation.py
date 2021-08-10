from typing import Optional

from messengers.base_message_sender import BaseMessageSender
from messengers.base_user_data import BaseUserData
from .base_interface import AggregatedComponent
from .utils.agregated_components import collect_variants_from_nodes


class Button(AggregatedComponent):
    def create_reply_markup(self, nodes, message_sender: BaseMessageSender, user_data: BaseUserData):
        variants = collect_variants_from_nodes("text", nodes)
        user_data.context["variants"] = variants
        reply_markup = message_sender.prepare_buttons(variants)

        return reply_markup

    def parse_answer(self, message_sender: BaseMessageSender, user_data: BaseUserData):
        text = message_sender.prev_message_text
        ind = user_data.context["variants"][text]
        del user_data.context["variants"]
        return ind


class InlineKey(AggregatedComponent):
    def create_reply_markup(self, nodes, message_sender: BaseMessageSender, user_data: BaseUserData):
        variants = collect_variants_from_nodes("text", nodes)
        reply_markup = message_sender.prepare_inline_keys(variants)
        return reply_markup

    def parse_answer(self, message_sender: BaseMessageSender, user_data: BaseUserData) -> Optional[int]:
        return message_sender.prev_message_choice_data
