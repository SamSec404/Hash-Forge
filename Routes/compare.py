from flask import Blueprint, render_template, request

from Utils.hash_utils import SUPPORTED_ALGORITHMS

compare_bp = Blueprint(
    "compare",
    __name__,
    url_prefix="/compare"
)


@compare_bp.route("/", methods=["POST"])
def compare():

    hash_a = request.form.get(
        "hash_a",
        ""
    ).strip()

    hash_b = request.form.get(
        "hash_b",
        ""
    ).strip()

    compare_result = ""
    error = ""

    if not hash_a:

        error = "Please enter first hash."

    elif not hash_b:

        error = "Please enter second hash."

    else:

        if hash_a.lower() == hash_b.lower():

            compare_result = "IDENTICAL ✅"

        else:

            compare_result = "DIFFERENT ❌"

    return render_template(
        "index.html",

        algorithms=SUPPORTED_ALGORITHMS.keys(),

        compare_result=compare_result,

        hash_a=hash_a,

        hash_b=hash_b,

        generated_hash="",

        verify_result="",

        input_text="",

        verify_text="",

        verify_hash="",

        selected_algorithm="SHA256",

        error=error
    )
