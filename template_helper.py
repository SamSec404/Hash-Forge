from flask import render_template

from Utils.hash_utils import SUPPORTED_ALGORITHMS
from Utils.history import load_history
from Utils.statistics import get_statistic


def render_home(**kwargs):

    context = {

        "algorithms": SUPPORTED_ALGORITHMS.keys(),

        "generated_hash": "",

        "verify_result": "",

        "compare_result": "",

        "input_text": "",

        "verify_text": "",

        "verify_hash": "",

        "hash_a": "",

        "hash_b": "",

        "selected_algorithm": "SHA256",

        "history": load_history(),

        "error": "",

        "identified_hash": "",

        "unknown_hash": "",

        **get_statistics(),

    }

    context.update(kwargs)

    return render_template(
        "index.html",
        **context
    )