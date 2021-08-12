from databases.base_node import BaseNode


class Neo4jNode(BaseNode):
    @property
    def component_type(self):
        return next(iter(self._node.labels))

    @property
    def id(self):
        return self._node.id

    def __getitem__(self, item):
        return self._node[item]