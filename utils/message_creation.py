from telegram import Update, ReplyKeyboardRemove

from telegram.ext import (
    CallbackContext,
)


def create_message(update: Update, context: CallbackContext, text: str, reply_markup=ReplyKeyboardRemove()):
    if not update.message:
        query = update.callback_query
        context.bot.send_message(query.message.chat_id, text, reply_markup=reply_markup)

    update.message.reply_text(
        text,
        reply_markup=reply_markup,
    )
