from abc import ABC, abstractmethod


class GraphApi(ABC):
    @abstractmethod
    def find_nodes_by_label(self, label):
        pass

    @abstractmethod
    def find_nodes_by_id(self, node_ind):
        pass

    @abstractmethod
    def search_post_process(self, node_ind=None):
        pass

    @abstractmethod
    def match_current_node(self, node_ind=None):
        pass
