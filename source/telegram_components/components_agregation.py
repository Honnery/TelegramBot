from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CallbackContext
)
from typing import Optional
from .utils.agregated_components import collect_variants_from_nodes
from .base_interface import AggregatedComponent


class Button(AggregatedComponent):
    def create_reply_markup(self, nodes, update: Update, context: CallbackContext):
        variants = collect_variants_from_nodes("text", nodes)
        context.user_data["context"]["variants"] = variants

        reply_markup = ReplyKeyboardMarkup(
            self._define_buttons(variants),
            one_time_keyboard=True,
            resize_keyboard=True)

        return reply_markup

    def parse_answer(self, update: Update, context: CallbackContext):
        text = update.message.text
        ind = context.user_data["context"]["variants"][text]
        del context.user_data["context"]["variants"]
        return ind

    @staticmethod
    def _define_buttons(variants):
        return [[button_text] for button_text in variants.keys()]


class InlineKey(AggregatedComponent):
    def create_reply_markup(self, nodes, update: Update, context: CallbackContext):
        variants = collect_variants_from_nodes("text", nodes)

        inline_keys = self._define_inline_keys(variants)
        reply_markup = InlineKeyboardMarkup(inline_keys)
        return reply_markup

    @staticmethod
    def _define_inline_keys(variants):
        return [[InlineKeyboardButton(text, callback_data=node_id)] for text, node_id in variants.items()]

    def parse_answer(self, update: Update, context: CallbackContext) -> Optional[int]:
        return int(update.callback_query.data)
