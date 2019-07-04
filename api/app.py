import redis
from flask import Flask, jsonify
from flask import request
from redis import Redis
from rq import Queue, Connection

from api.tasks import countdown_task


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Countdown API'

    @app.route('/countdown', methods=['POST'])
    def countdown():
        """
        curl -i -H "Content-Type: application/json" -X POST -d '{"minutes":"1"}' http://127.0.0.1:5000/countdown
        :return:
        """
        if not request.get_json() or 'minutes' not in request.get_json():
            response_object = {
                "Error": "Wrong parameters, 'minutes' not set"
            }
            return jsonify(error=response_object), 400

        # todo use a string timer code like 5s = 5 seconds, 10m = 10 minutes
        request_json_data = request.get_json()
        minutes = request_json_data["minutes"]

        conn1 = Redis('localhost', 6379)
        with Connection(conn1):
            q = Queue('default')
            task = q.enqueue(countdown_task, minutes)

        response_object = {
            'status': 'success',
            'data': {
                'task_id': task.get_id(),
                'minutes': minutes
            }
        }

        return jsonify(response_object), 200

    return app
