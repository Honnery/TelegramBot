from telegram import Update
from telegram.ext import (
    CallbackContext
)
from typing import Optional
from database import find_next_nodes
from .base_interface import BaseComponent
from utils.user_context import clear_context


class AggregateVariants(BaseComponent):
    def __init__(self):
        from . import conversation_interface
        self._conversation_interfaces = conversation_interface

    def create_answer(self, nodes,
                      update: Update,
                      context: CallbackContext):
        aggregation_node = nodes[0]
        reply_markup, state = self._answers_aggregation(aggregation_node.id, update, context)
        context.user_data["state"] = state
        text = aggregation_node["text"]
        self._create_message(update, context, text, reply_markup)

    def _answers_aggregation(self, aggregation_node, update: Update, context: CallbackContext):
        next_nodes = find_next_nodes(aggregation_node)
        component = self._get_aggregation_comp(next_nodes)
        reply_markup = component.create_reply_markup(next_nodes, update, context)
        return reply_markup, component.__class__.__name__

    def _get_aggregation_comp(self, nodes):
        return self._conversation_interfaces[nodes[0].component_type]


class Input(BaseComponent):
    def parse_answer(self, update: Update, context: CallbackContext) -> None:
        input_text = update.message.text

        param_name = context.user_data["context"]["param_name"]
        context.user_data["params"][param_name] = input_text
        del context.user_data['context']['param_name']


class Finish(BaseComponent):

    def create_answer(self, nodes, update: Update, context: CallbackContext):
        text = nodes[0]["text"]
        self._create_message(update, context, text)

    def parse_answer(self, update: Update, context: CallbackContext):
        clear_context(context)
