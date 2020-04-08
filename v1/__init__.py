from sanic import Blueprint

from .api import api

v1 = Blueprint.group(api, url_prefix='/v1')