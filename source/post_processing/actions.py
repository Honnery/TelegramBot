from messengers.base_user_data import BaseUserData
from messengers.base_message_sender import BaseMessageSender


def save_params(prev_node, action_node, message_sender: BaseMessageSender, user_data: BaseUserData):
    """
    Just an example to show how to work with post processing.
    Saves param as text.
    """
    user_data.properties[action_node["param_name"]] = prev_node["text"]


post_processes = {
    "SaveParam": save_params,
}
