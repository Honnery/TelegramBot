from telegram import Update
from telegram.ext import (
    CallbackContext
)
from database import find_next_nodes
from .base_interface import BaseComponent
from utils.user_context import clear_context, update_state


class AggregateVariants(BaseComponent):
    """ Component that able to aggregate few comp into one for example Buttoms, InlineKeys and etc"""
    def __init__(self):
        from . import conversation_interface
        self._conversation_interfaces = conversation_interface

    def create_answer(self, node,
                      update: Update,
                      context: CallbackContext):
        reply_markup, state = self._answers_aggregation(node.id, update, context)
        update_state(state, context)
        text = node["text"]
        self._create_message(text, update, context, reply_markup)

    def _answers_aggregation(self, aggregation_node, update: Update, context: CallbackContext):
        next_nodes = find_next_nodes(aggregation_node)
        nodes_type = next_nodes[0].component_type

        component = self._get_aggregation_comp(nodes_type)
        reply_markup = component.create_reply_markup(next_nodes, update, context)

        return reply_markup, nodes_type

    def _get_aggregation_comp(self, nodes_type):
        return self._conversation_interfaces[nodes_type]


class Input(BaseComponent):
    """ Input component, node should has "text" param ..."""
    def create_answer(self, node, update: Update, context: CallbackContext):
        input_desc = node["text"]
        context.user_data["context"]["param_name"] = node["param_name"]
        self._create_message(input_desc, update, context)
        context.user_data["prev_point_id"] = node.id

    # ToDo extract context
    def parse_answer(self, update: Update, context: CallbackContext) -> None:
        input_text = update.message.text

        param_name = context.user_data["context"]["param_name"]
        context.user_data["params"][param_name] = input_text
        del context.user_data['context']['param_name']


class Finish(BaseComponent):

    def create_answer(self, node, update: Update, context: CallbackContext):
        text = node["text"]
        self._create_message(text, update, context)

    def parse_answer(self, update: Update, context: CallbackContext):
        clear_context(context)
