from abc import abstractmethod, ABC


class BaseMessageSender(ABC):
    @abstractmethod
    def send_message(self, text: str, reply_markup=None):
        pass

    @property
    @abstractmethod
    def prev_message_text(self):
        pass

    @property
    @abstractmethod
    def prev_message_choice_data(self):
        pass

    @abstractmethod
    def prepare_buttons(self, variants):
        pass

    @abstractmethod
    def prepare_inline_keys(self, variants):
        pass
