from flask import Blueprint, render_template

from Utils.history import load_history

from Utils.hash_utils import SUPPORTED_ALGORITHMS

history_bp = Blueprint(
    "history",
    __name__,
    url_prefix="/history"
)


@history_bp.route("/")
def history():

    history = load_history()

    return render_template(
        "index.html",

        history=history,

        algorithms=SUPPORTED_ALGORITHMS.keys(),

        generated_hash="",

        verify_result="",

        compare_result="",

        input_text="",

        verify_text="",

        verify_hash="",

        hash_a="",

        hash_b="",

        selected_algorithm="SHA256",

        error=""
    )