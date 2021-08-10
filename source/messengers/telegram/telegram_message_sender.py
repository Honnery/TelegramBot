from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from messengers.base_message_sender import BaseMessageSender


class TelegramMessageSender(BaseMessageSender):
    def __init__(self, update: Update, context: CallbackContext):
        self.update = update
        self.bot = context.bot

    @property
    def prev_message_text(self):
        return self.update.message.text

    @property
    def prev_message_choice_data(self):
        return int(self.update.callback_query.data)

    def send_message(self, text: str, reply_markup=ReplyKeyboardRemove()):
        if self.update.message:
            self.update.message.reply_text(text, reply_markup=reply_markup)
        else:
            query = self.update.callback_query
            self.bot.send_message(query.message.chat_id, text, reply_markup=reply_markup)

    def prepare_buttons(self, variants):
        buttons = [[button_text] for button_text in variants.keys()]
        reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
        return reply_markup

    def prepare_inline_keys(self, variants):
        inline_buttons = [[InlineKeyboardButton(text, callback_data=node_id)] for text, node_id in variants.items()]
        reply_markup = InlineKeyboardMarkup(inline_buttons)
        return reply_markup
