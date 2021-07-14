from telegram import Update
from telegram.ext import (
    CallbackContext,
)


def save_params(prev_node, action_node, update: Update, context: CallbackContext):
    """
    Just an example to show how to work with post processing.
    Saves param as text.
    """
    context.user_data["params"][action_node["param_name"]] = prev_node["text"]


post_processes = {
    "SaveParam": save_params,
}
