from flask import Flask

from resources import Resources
from error_handler import ErrorHandler

app = Flask(__name__)
app.register_blueprint(Resources)
ErrorHandler(app)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )