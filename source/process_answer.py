from dependency_injector.wiring import inject, Provide
from telegram import Update
from messengers.base_wrappers import BaseUserData

from components import conversation_interface
from databases import find_next_nodes
from databases.base_db import GraphApi
from post_processing import post_processes


def find_new_answer(update: Update, user_data: BaseUserData):
    prev_node_id = user_data.prev_point_id
    node = find_next_nodes(prev_node_id)[0]

    label_type = node.component_type
    user_data.state = label_type

    conversation_interface[label_type].create_answer(node, update, user_data)


@inject
def find_post_process(update: Update, user_data: BaseUserData, graph_api: GraphApi = Provide['graph_api']):
    prev_node_ind = user_data.prev_point_id
    post_proc_nodes = graph_api.search_post_process(prev_node_ind)

    if post_proc_nodes:
        post_proc_node = post_proc_nodes[0]
        state = post_proc_node.component_type
        node = graph_api.match_current_node(prev_node_ind)
        post_processes[state](node, post_proc_node, update, user_data)


def handle_prev_answer(update: Update, user_data: BaseUserData):
    label_type = user_data.state

    prev_id = conversation_interface[label_type].parse_answer(update, user_data)
    if isinstance(prev_id, int):
        user_data.prev_point_id = prev_id
    find_post_process(update, user_data)
    if label_type:
        user_data.state = None
