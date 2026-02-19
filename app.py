from flask import Flask, render_template, request, abort
from indexer import CodeIndexer
import os

app = Flask(__name__)

# Change this if you want to scan a specific folder
PROJECT_DIR = os.getcwd()

indexer = CodeIndexer(PROJECT_DIR)
code_index = indexer.build_index()


@app.route("/")
def home():
    return render_template("index.html", results=None)


@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = indexer.search(query) if query else []
    return render_template("index.html", results=results, query=query)


@app.route("/file")
def view_file():
    filepath = request.args.get("path")

    if not filepath:
        abort(404)

    # Security check
    safe_path = os.path.abspath(filepath)
    if not safe_path.startswith(PROJECT_DIR):
        abort(403)

    if os.path.exists(safe_path):
        with open(safe_path, "r", encoding="utf-8") as f:
            content = f.read()
        return render_template("file.html", content=content, path=safe_path)

    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
