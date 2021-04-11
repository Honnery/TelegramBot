import logging

from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from post_process import  find_post_process

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# ToDo Use class to store all this info in one place
def find_button(update, context: CallbackContext):
    text = update.message.text
    ind = context.user_data["context"]["variants"][text]
    del context.user_data["context"]["variants"]
    return ind


def save_input_info(update, context: CallbackContext):
    input_text = update.message.text

    context.user_data["params"][context.user_data["context"]["param_name"]] = input_text
    del context.user_data['context']['param_name']


def find_inline_key(update:Update, context: CallbackContext):
    return int(update.callback_query.data)

states = {
    "Button": find_button,
    "Input": save_input_info,
    "InlineKey": find_inline_key,
          }


def handle_prev_answer(update: Update, context: CallbackContext):
    state = context.user_data.get("state")
    if state in states:
        prev_id = states[state](update, context)
        if isinstance(prev_id, int):
            context.user_data["prev_point_id"] = prev_id
    find_post_process(update, context)

    if state:
        del context.user_data["state"]
