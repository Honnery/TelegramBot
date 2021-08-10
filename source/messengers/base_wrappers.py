from abc import ABC, abstractmethod


class BaseApiWrapper(ABC):
    def __init__(self, start_conv_func, receive_answer_func):
        self._initial_start_conv = start_conv_func
        self._initial_receive_answer = receive_answer_func

    @abstractmethod
    def start_polling(self):
        pass

    @abstractmethod
    def _create_user_context(self, context):
        pass

    @abstractmethod
    def _create_update(self, update):
        pass

    def start_conversation(self, update, context):
        update = self._create_update(update)
        context = self._create_user_context(context)
        self._initial_start_conv(update, context)

    def receive_answer(self, update, context):
        update = self._create_update(update)
        context = self._create_user_context(context)
        self._initial_receive_answer(update, context)


# ToDo
class BaseUserData:
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

    # ToDO Move to Update
    @abstractmethod
    def send_message(self, chat_id, text, reply_markup):
        pass

    def clear_context(self):
        self.prev_point_id = None
        self.state = None
        self.context = {}
        self.properties = {}


