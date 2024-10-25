from flask import Flask
from flask_jwt_extended import JWTManager

from resources import Resources
from error_handler import ErrorHandler

app = Flask(__name__)
app.register_blueprint(Resources)

app.secret_key = "#hcs51v^o!lwfa7h%wt*2elv4ew(@5k)r!t9e@f19#ecn%s$@k"
app.config["JWT_SECRET_KEY"] = app.secret_key

ErrorHandler(app)
JWTManager(app)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )