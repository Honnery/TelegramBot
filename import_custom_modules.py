import sys
from importlib import util
from functools import wraps

from settings import telegram_config

custom_functions_path = telegram_config.get("CUSTOMIZATION", "custom_functions_path")


def get_custom_module(func):
    spec = util.spec_from_file_location("custom_module", custom_functions_path)
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    @wraps(func)
    def wrapper(args):
        output = func(args, module)
        return output

    return wrapper


@get_custom_module
def call_function(function_name, module):
    output = getattr(module, function_name)()
    return output
