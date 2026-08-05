from flask import Blueprint, render_template, request

from Utils.hash_utils import (
    generate_hash,
    SUPPORTED_ALGORITHMS
)

verify_bp = Blueprint(
    "verify",
    __name__,
    url_prefix="/verify"
)


@verify_bp.route("/", methods=["POST"])
def verify():

    verify_text = request.form.get(
        "verify_text",
        ""
    ).strip()

    verify_hash = request.form.get(
        "verify_hash",
        ""
    ).strip()

    algorithm = request.form.get(
        "algorithm",
        "SHA256"
    )

    verify_result = ""
    error = ""

    if not verify_text:

        error = "Please enter text."

    elif not verify_hash:

        error = "Please enter hash."

    elif algorithm not in SUPPORTED_ALGORITHMS:

        error = "Invalid Algorithm."

    else:

        calculated_hash = generate_hash(
            verify_text,
            algorithm
        )

        if calculated_hash.lower() == verify_hash.lower():

            verify_result = "MATCH ✅"

        else:

            verify_result = "NOT MATCH ❌"

    return render_template(

        "index.html",

        algorithms=SUPPORTED_ALGORITHMS.keys(),

        verify_result=verify_result,

        verify_text=verify_text,

        verify_hash=verify_hash,

        selected_algorithm=algorithm,

        generated_hash="",

        compare_result="",

        hash_a="",

        hash_b="",

        input_text="",

        error=error

    )
