import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sanic import Sanic
import setting


def create_application():
    app = Sanic(__name__)
    app.config.from_object(setting)
    return app