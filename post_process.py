from db_commands import graph_api

from telegram import Update
from telegram.ext import (
    CallbackContext,
)


def save_params(prev_node, action_node, update: Update, context: CallbackContext):
    context.user_data["params"][action_node["param_name"]] = prev_node["text"]


post_processes = {
    "SaveParam": save_params,
}


def find_post_process(update: Update, context: CallbackContext):
    ind = context.user_data["prev_point_id"]
    post_proc_node = graph_api.search_post_process(ind)
    if post_proc_node:
        state = next(iter(post_proc_node[0].labels))
        node = graph_api.match_current_node(ind)
        post_processes[state](node[0], post_proc_node[0], update, context)

