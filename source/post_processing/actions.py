from telegram import Update
from messengers.base_wrappers import BaseUserData


def save_params(prev_node, action_node, update: Update, user_data: BaseUserData):
    """
    Just an example to show how to work with post processing.
    Saves param as text.
    """
    user_data.properties[action_node["param_name"]] = prev_node["text"]


post_processes = {
    "SaveParam": save_params,
}
