from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory
import os
from werkzeug.utils import secure_filename
from model import process_resume  # ✅ FIXED IMPORT

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'super-secret-key-change-this-in-production'

# Create upload folder
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------- AUTH PAGES ----------------
@app.route('/view/<filename>')
def view_file(filename):
    return send_from_directory(
        directory=app.config["UPLOAD_FOLDER"],
        path=filename,
        as_attachment=False
    )
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Login feature coming soon!", "info")
        return redirect(url_for('index'))
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        flash("Signup feature coming soon!", "info")
        return redirect(url_for('index'))
    return render_template("signup.html")


@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- MAIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        job_description = request.form.get("job_description", "").strip()

        if not job_description:
            flash("Please enter a job description.", "danger")
            return redirect(url_for('index'))

        job_desc = job_description

        files = request.files.getlist("resumes")

        if not files or files[0].filename == "":
            flash("Please upload at least one resume.", "danger")
            return redirect(url_for('index'))

        for file in files:
            if file and file.filename != "" and allowed_file(file.filename):
                try:
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                    file.save(filepath)

                    # ✅ CALL MODEL
                    data = process_resume(job_desc, filepath)

                    results.append({
                        "name": file.filename,
                        "score": data["score"],
                        "matched": data["matched"],
                        "missing": data["missing"]
                    })

                except Exception as e:
                    flash(f"Error processing {file.filename}: {str(e)}", "danger")
                    continue

        # ✅ SORT RESULTS
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        if not results:
            flash("No valid resumes were processed.", "warning")

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)