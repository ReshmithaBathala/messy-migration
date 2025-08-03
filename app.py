from flask import Flask
from db import close_db
from routes import users_bp, auth_bp
from config import FLASK_PORT, DEBUG

app = Flask(__name__)

# Register blueprints
app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)

# Teardown
app.teardown_appcontext(close_db)

@app.route('/')
def home():
    return {"message": "User Management System"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=DEBUG)