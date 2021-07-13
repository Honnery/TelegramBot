from telegram import Update
from database.db_commands import graph_api
from telegram.ext import (
    CallbackContext,
)
from telegram_components import conversation_interface
from database import find_next_nodes
from utils.user_context import update_state
from post_processing import post_processes


def find_new_answer(update: Update, context: CallbackContext):
    prev_node_id = context.user_data.get("prev_point_id")
    node = find_next_nodes(prev_node_id)[0]

    label_type = node.component_type
    update_state(label_type, context)

    conversation_interface[label_type].create_answer(node, update, context)


def find_post_process(update: Update, context: CallbackContext):
    prev_node_ind = context.user_data["prev_point_id"]
    post_proc_nodes = graph_api.search_post_process(prev_node_ind)

    if post_proc_nodes:
        post_proc_node = post_proc_nodes[0]
        state = post_proc_node.component_type
        node = graph_api.match_current_node(prev_node_ind)
        post_processes[state](node, post_proc_node, update, context)


def handle_prev_answer(update: Update, context: CallbackContext):
    label_type = context.user_data.get("state")
    prev_id = conversation_interface[label_type].parse_answer(update, context)
    if isinstance(prev_id, int):
        context.user_data["prev_point_id"] = prev_id
    find_post_process(update, context)
    if label_type:
        del context.user_data["state"]
