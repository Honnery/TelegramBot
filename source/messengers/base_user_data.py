from abc import ABC, abstractmethod


class BaseUserData(ABC):
    @property
    @abstractmethod
    def prev_point_id(self):
        pass

    @prev_point_id.setter
    @abstractmethod
    def prev_point_id(self, new_prev_point_id):
        pass

    @property
    @abstractmethod
    def state(self):
        pass

    @state.setter
    @abstractmethod
    def state(self, new_state):
        pass

    @property
    @abstractmethod
    def context(self):
        pass

    @context.setter
    @abstractmethod
    def context(self, new_context):
        pass

    @property
    @abstractmethod
    def properties(self):
        pass

    @properties.setter
    @abstractmethod
    def properties(self, new_properties):
        pass

    def clear_context(self):
        self.prev_point_id = None
        self.state = None
        self.context = {}
        self.properties = {}
