from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello5 from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"