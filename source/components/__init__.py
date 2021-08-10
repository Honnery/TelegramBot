from .components_agregation import Button, InlineKey
from .standart_components import Input, Finish, AggregateVariants

conversation_interface = {}

__all__ = [Button, Input, Finish, AggregateVariants, InlineKey]
conversation_interface.update({comp.__name__: comp() for comp in __all__})
