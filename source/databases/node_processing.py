from dependency_injector.wiring import inject, Provide

from databases.base_db import GraphApi


class NodeProcessor:
    graph_api: GraphApi = Provide['graph_api']

    def find_next_nodes(self, prev_node_id):
        if isinstance(prev_node_id, int):
            nodes = self.graph_api.find_nodes_by_id(prev_node_id)
        else:
            nodes = self.graph_api.find_nodes_by_label(label="Start")
        return nodes

    def get_post_process_for_node(self, node_id):
        self.graph_api.search_post_process(node_id)

    def match_node_by_id(self, node_id):
        self.graph_api.match_current_node(node_id)


node_processor = NodeProcessor()
