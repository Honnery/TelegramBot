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
class UserContext:
    @property
    @abstractmethod
    def prev_point_id(self):
        pass

    @property
    @abstractmethod
    def state(self):
        pass

    @property
    @abstractmethod
    def context(self):
        pass
