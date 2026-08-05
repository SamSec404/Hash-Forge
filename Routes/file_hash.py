from flask import Blueprint, render_template, request, current_app
from werkzeug.utils import secure_filename
from datetime import datetime

from Models.hash_record import HashRecord

from Utils.history import add_history

import os

from Utils.hash_utils import (
    generate_file_hash,
    SUPPORTED_ALGORITHMS
)

from Utils.validators import allowed_file
from Utils.file_utils import delete_uploaded_file

file_hash_bp = Blueprint(
    "file_hash",
    __name__,
    url_prefix="/file-hash"
)


@file_hash_bp.route("/", methods=["POST"])
def file_hash():

    generated_hash = ""
    error = ""

    uploaded_file = request.files.get("uploaded_file")

    algorithm = request.form.get(
        "algorithm",
        "SHA256"
    )

    if not uploaded_file:

        error = "Please select a file."

    elif not allowed_file(uploaded_file.filename):

        error = "Invalid file type."

    else:

        filename = secure_filename(
            uploaded_file.filename
        )

        save_path = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            filename
        )

        uploaded_file.save(save_path)

        generated_hash = generate_file_hash(
            save_path,
            algorithm
        )

        record = HashRecord(

            record_type="File",

            original_input=filename,

            algorithm=algorithm,

            generated_hash=generated_hash,

            timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

        add_history(record)

        delete_uploaded_file(save_path)

    return render_template(
        "index.html",

        algorithms=SUPPORTED_ALGORITHMS.keys(),

        generated_hash=generated_hash,

        selected_algorithm=algorithm,

        verify_result="",

        compare_result="",

        input_text="",

        verify_text="",

        verify_hash="",

        hash_a="",

        hash_b="",

        error=error
    )
