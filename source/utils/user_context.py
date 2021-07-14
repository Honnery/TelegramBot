from telegram.ext import CallbackContext


def clear_context(context: CallbackContext):
    """
    Clear information, saved in context.
    :param context:
    :return:
    """
    context.user_data["prev_point_id"] = None
    context.user_data.pop("state", None)
    context.user_data["context"] = {}
    context.user_data["params"] = {}

    return context


def update_state(state: str, context: CallbackContext):
    """Update state in context with required value"""
    context.user_data["state"] = state
