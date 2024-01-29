from flask import Flask
from models import storage
from views.app_views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(err):
    """handler"""
    return {"error": "Not found"}, 404

@app.errorhandler(400)
def page_not_found(err):
    """handler"""
    msg = err.description
    return msg, 400


if __name__ == "__main__":
    app.run(debug=True)
