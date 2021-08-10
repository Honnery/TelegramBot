from databases import find_next_nodes
from messengers.base_message_sender import BaseMessageSender
from messengers.base_user_data import BaseUserData
from .base_interface import BaseComponent


class AggregateVariants(BaseComponent):
    """ Component that able to aggregate few comp into one for example Buttons, InlineKeys and etc"""

    def __init__(self):
        from . import conversation_interface
        self._conversation_interfaces = conversation_interface

    def create_answer(self,
                      node,
                      message_sender: BaseMessageSender,
                      user_data: BaseUserData):
        reply_markup, state = self._answers_aggregation(node.id, message_sender, user_data)
        user_data.state = state
        text = node["text"]
        message_sender.send_message(text, reply_markup)

    def _answers_aggregation(self, aggregation_node, message_sender: BaseMessageSender, user_data: BaseUserData):
        next_nodes = find_next_nodes(aggregation_node)
        nodes_type = next_nodes[0].component_type

        component = self._get_aggregation_comp(nodes_type)
        reply_markup = component.create_reply_markup(next_nodes, message_sender, user_data)

        return reply_markup, nodes_type

    def _get_aggregation_comp(self, nodes_type):
        return self._conversation_interfaces[nodes_type]


class Input(BaseComponent):
    """ Input component, node should has "text" param ..."""

    def create_answer(self, node, message_sender: BaseMessageSender, user_data: BaseUserData):
        input_desc = node["text"]
        user_data.context["param_name"] = node["param_name"]
        message_sender.send_message(input_desc)
        user_data.prev_point_id = node.id

    # ToDo extract context
    def parse_answer(self, message_sender: BaseMessageSender, user_data: BaseUserData) -> None:
        input_text = message_sender.prev_message_text

        param_name = user_data.context["param_name"]
        user_data.properties[param_name] = input_text
        del user_data.context['param_name']


class Finish(BaseComponent):

    def create_answer(self, node, message_sender: BaseMessageSender, user_data: BaseUserData):
        text = node["text"]
        message_sender.send_message(text)

    def parse_answer(self, message_sender: BaseMessageSender, user_data: BaseUserData):
        user_data.clear_context()
