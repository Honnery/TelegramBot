from telegram import Update
from telegram.ext import (
    CallbackContext,
)

def save_params(
        prev_node,
        action_node,
        update: Update,
        context: CallbackContext):
    context.user_data["params"][action_node["param_name"]] = prev_node["text"]


post_processes = {
    "SaveParam": save_params,
}
