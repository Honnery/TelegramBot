from telegram.ext import CallbackContext

def clear_context(context: CallbackContext):
    if context.user_data.get("prev_point_id"):
        del context.user_data["prev_point_id"]

    context.user_data["context"] = {}
    context.user_data["params"] = {}

    return context
