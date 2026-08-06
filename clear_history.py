from flask import Blueprint, redirect, url_for

from Utils.history import clear_history

clear_history_bp = Blueprint(
    "clear_history",
    __name__,
    url_prefix="/history"
)


@clear_history_bp.route("/clear")
def clear():

    clear_history()

    return redirect(
        url_for("history.history")
    )