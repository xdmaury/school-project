from app import app


@app.route("/api/student")
def index():
    return 'ok'