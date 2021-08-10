from dependency_injector.wiring import inject, Provide

from databases.base_db import GraphApi


@inject
def find_next_nodes(prev_node_id, graph_api: GraphApi = Provide['graph_api']):
    if isinstance(prev_node_id, int):
        nodes = graph_api.find_nodes_by_id(prev_node_id)
    else:
        nodes = graph_api.find_nodes_by_label(label="Start")
    return nodes


def get_post_process():
    return None
