from flask import Flask
from resources import Resources

app = Flask(__name__)
app.register_blueprint(Resources)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )