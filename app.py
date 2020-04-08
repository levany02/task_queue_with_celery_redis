# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_app.app_sanic import create_application
from v1 import v1
# from my_app.app_celery import make_celery


def run():
    app = create_application()
    app.blueprint(v1)
    # make_celery(my_app)
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == '__main__':
    run()