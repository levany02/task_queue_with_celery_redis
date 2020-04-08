import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sanic import Blueprint
from sanic.response import json, redirect, text
from my_app.app_flask import create_application
from my_app.app_celery import make_celery


api = Blueprint("api")
celery = make_celery(create_application())

# @api.route('/api')
# async def bp_root(request):
#     return json({'my': 'blueprint'})


@celery.task(name="tasks.add")
def add(x, y):
    return x + y


@api.route('/test/add')
async def hello_world(request,x=1, y=2):
    x = int(request.args["one"][0])
    y = int(request.args["two"][0])
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    result = "add((x){}, (y){})".format(context['x'], context['y'])
    goto = "{}".format(context['id'])
    return json({"result":result, "goto":goto})


@api.route('/test')
async def test(request):
    url = request.app.url_for('hello_world', arg_one='one', arg_two='two') # --> '/v1/api/post/5'
    return redirect(url)


@api.route("/test/result/<task_id>")
def show_result(request, task_id):
    print("--------------------", task_id)
    print("--------------------", type(task_id))
    retval = add.AsyncResult(task_id).get(timeout=1.0)
    print("--------------------", retval)
    return json({"result": retval})
