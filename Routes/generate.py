from flask import Blueprint, render_template, request
from datetime import datetime

from Models.hash_record import HashRecord

from Utils.history import add_history
from Utils.hash_utils import (
    generate_hash,
    SUPPORTED_ALGORITHMS
)

generate_bp = Blueprint(
    "generate",
    __name__,
    url_prefix="/generate"
)


@generate_bp.route("/", methods=["POST"])
def generate():

    input_text = request.form.get(
        "input_text",
        ""
    ).strip()

    algorithm = request.form.get(
        "algorithm",
        "SHA256"
    )

    generated_hash = ""
    error = ""

    if not input_text:

        error = "Please enter some text."

    elif algorithm not in SUPPORTED_ALGORITHMS:

        error = "Invalid Algorithm."

    else:

        generated_hash = generate_hash(
            input_text,
            algorithm
        )

        record = HashRecord(

            record_type="Text",

            original_input=input_text,

            algorithm=algorithm,

            generated_hash=generated_hash,

            timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

        add_history(record)

    return render_template(
        "index.html",

        algorithms=SUPPORTED_ALGORITHMS.keys(),

        generated_hash=generated_hash,

        selected_algorithm=algorithm,

        input_text=input_text,

        error=error,

        verify_result="",

        compare_result="",

        verify_text="",

        verify_hash="",

        hash_a="",

        hash_b=""
    )
