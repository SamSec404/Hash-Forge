from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os
import hashlib

from config import (
    UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH
)

from utils.hash_utils import (
    generate_hash,
    generate_file_hash,
    SUPPORTED_ALGORITHMS
)

from utils.validators import allowed_file
from utils.file_utils import delete_uploaded_file

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

SUPPORTED_ALGORITHMS = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA224": hashlib.sha224,
    "SHA256": hashlib.sha256,
    "SHA384": hashlib.sha384,
    "SHA512": hashlib.sha512,
    "SHA3-224": hashlib.sha3_224,
    "SHA3-256": hashlib.sha3_256,
    "SHA3-384": hashlib.sha3_384,
    "SHA3-512": hashlib.sha3_512,
    "BLAKE2b": hashlib.blake2b,
    "BLAKE2s": hashlib.blake2s,
}


def generate_hash(text, algorithm):
    hash_object = SUPPORTED_ALGORITHMS[algorithm]()
    hash_object.update(text.encode("utf-8"))
    return hash_object.hexdigest()


@app.route("/", methods=["GET", "POST"])
def home():

    generated_hash = ""
    verify_result = ""
    compare_result = ""

    input_text = ""
    verify_text = ""
    verify_hash = ""

    hash_a = ""
    hash_b = ""

    selected_algorithm = "SHA256"

    error = ""

    if request.method == "POST":

        action = request.form.get("action")

        if action == "generate":

            input_text = request.form.get("input_text", "").strip()
            selected_algorithm = request.form.get("algorithm")

            if not input_text:
                error = "Please enter some text."

            else:
                generated_hash = generate_hash(
                    input_text,
                    selected_algorithm
                )

        elif action == "verify":

            verify_text = request.form.get("verify_text", "")
            verify_hash = request.form.get("verify_hash", "")
            selected_algorithm = request.form.get("algorithm")

            calculated = generate_hash(
                verify_text,
                selected_algorithm
            )

            if calculated.lower() == verify_hash.lower():

                verify_result = "MATCH ✅"

            else:

                verify_result = "NOT MATCH ❌"

        elif action == "compare":

            hash_a = request.form.get("hash_a", "").strip()
            hash_b = request.form.get("hash_b", "").strip()

            if hash_a.lower() == hash_b.lower():

                compare_result = "IDENTICAL ✅"

            else:

                compare_result = "DIFFERENT ❌"


        elif action == "file":

            uploaded_file = request.files.get("uploaded_file")

            selected_algorithm = request.form.get(
                "algorithm",
                "SHA256"
            )

            if uploaded_file and allowed_file(uploaded_file.filename):

                filename = secure_filename(uploaded_file.filename)

                save_path = os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )

                uploaded_file.save(save_path)

                generated_hash = generate_file_hash(
                    save_path,
                    selected_algorithm
                )

                delete_uploaded_file(save_path)

            else:

                error = "Invalid file selected."

    return render_template(
        "index.html",
        algorithms=SUPPORTED_ALGORITHMS.keys(),

        generated_hash=generated_hash,
        verify_result=verify_result,
        compare_result=compare_result,

        input_text=input_text,
        verify_text=verify_text,
        verify_hash=verify_hash,

        hash_a=hash_a,
        hash_b=hash_b,

        selected_algorithm=selected_algorithm,

        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)