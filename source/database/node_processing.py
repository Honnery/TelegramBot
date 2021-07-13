from .db_commands import graph_api


def find_next_nodes(prev_node_id):
    if isinstance(prev_node_id, int):
        nodes = graph_api.find_nodes_by_id(prev_node_id)
    else:
        nodes = graph_api.find_nodes_by_label(label="Start")
    return nodes

def get_post_process():
    return None