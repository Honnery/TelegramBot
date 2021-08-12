from abc import ABC, abstractmethod


class BaseNode(ABC):
    def __init__(self, node):
        self._node = node

    @property
    @abstractmethod
    def component_type(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        """
        Should be used to get special data that is useful and uniq
        for logic for different types of components
        """
        pass
