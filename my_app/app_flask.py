import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
import setting


def create_application():
    app = Flask(__name__)
    app.config.from_object(setting)
    return app