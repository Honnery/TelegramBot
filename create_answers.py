from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CallbackContext,
)
from import_custom_modules import call_function
from db_commands import graph_api
from utils.message_creation import create_message


# ToDo Create subclasses for integration features
def create_buttons(nodes,
                   update: Update,
                   context: CallbackContext):
    variants = {node["text"]: node.id for node in nodes}
    context.user_data["context"]["variants"] = variants
    reply_markup = ReplyKeyboardMarkup(list(map(lambda a: [a], variants.keys()))[::-1], one_time_keyboard=True,
                                       resize_keyboard=True)
    return reply_markup


def execute_function(nodes,
                     update: Update,
                     context: CallbackContext):
    function_name = nodes[0]["name"]
    output = call_function(function_name)
    context.user_data["prev_point_id"] = nodes[0].id
    create_message(update, context, output)


def create_action_message(nodes,
                          update: Update,
                          context: CallbackContext):
    context.user_data["prev_point_id"] = nodes[0].id
    reply_markup = find_new_answer(update, context)
    text = nodes[0]["text"]
    create_message(update, context, text, reply_markup)


def finish_conversation(nodes,
                        update: Update,
                        context: CallbackContext):
    text = nodes[0]["text"]
    create_message(update, context, text)
    del context.user_data["prev_point_id"]
    del context.user_data["state"]
    del context.user_data["context"]
    del context.user_data["params"]


def input_info(nodes,
               update: Update,
               context: CallbackContext):
    node = nodes[0]
    context.user_data["prev_point_id"] = node.id
    input_desc = node["input_description"]
    context.user_data["context"]["param_name"] = node["param_name"]
    create_message(update, context, input_desc)


def create_inlines(nodes,
                   update: Update,
                   context: CallbackContext):
    variants = [[InlineKeyboardButton(node["text"], callback_data=node.id)] for node in nodes]
    reply_markup = InlineKeyboardMarkup(variants)
    return reply_markup


states = {
    "ActionLabel": create_action_message,
    "Button": create_buttons,
    "Input": input_info,
    "InlineKey": create_inlines,
    "CustomFunction": execute_function,
    "Finish": finish_conversation,
}


def find_new_answer(update: Update, context: CallbackContext):
    prev_id = context.user_data.get("prev_point_id")

    if isinstance(prev_id, int):
        nodes = graph_api.match_buttons(ind=prev_id)
    else:
        nodes = graph_api.match_buttons(label="Start")

    state = next(iter(nodes[0].labels))
    context.user_data["state"] = state

    reply_markup = states[state](nodes, update, context)

    return reply_markup
