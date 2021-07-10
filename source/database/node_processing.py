from .db_commands import graph_api


def find_next_nodes(prev_node_id):
    if isinstance(prev_node_id, int):
        nodes = graph_api.match_next_nodes(node_ind=prev_node_id)
    else:
        nodes = graph_api.match_next_nodes(label="Start")
    return nodes


