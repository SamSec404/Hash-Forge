from flask import Flask, render_template
from config import UPLOAD_FOLDER, MAX_CONTENT_LENGTH

from Routes import (
    generate_bp,
    verify_bp,
    compare_bp,
    file_hash_bp,
    history_bp,
    delete_history_bp,
    clear_history_bp
)

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

app.register_blueprint(generate_bp)
app.register_blueprint(verify_bp)
app.register_blueprint(compare_bp)
app.register_blueprint(file_hash_bp)
app.register_blueprint(history_bp)
app.register_blueprint(delete_history_bp)
app.register_blueprint(clear_history_bp)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

    
