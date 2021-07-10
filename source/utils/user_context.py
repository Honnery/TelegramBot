from telegram.ext import CallbackContext

def clear_context(context: CallbackContext):
    context.user_data["prev_point_id"] = None
    del context.user_data["state"]
    context.user_data["context"] = {}
    context.user_data["params"] = {}

    return context
