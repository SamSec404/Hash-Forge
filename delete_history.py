from flask import Blueprint, redirect, url_for

from Utils.history import delete_history

delete_history_bp = Blueprint(
    "delete_history",
    __name__,
    url_prefix="/history"
)


@delete_history_bp.route("/delete/<int:index>")
def delete(index):

    delete_history(index)

    return redirect(
        url_for("history.history")
    )