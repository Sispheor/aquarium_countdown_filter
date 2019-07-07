import os

from flask import Flask, jsonify
from flask import request
from redis import Redis
from rq import Queue, Connection

from api.tasks import countdown_task
from utils.interval_string import IntervalString


def create_app():
    app = Flask(__name__)

    meross_device = os.getenv('MEROSS_DEVICE', None)
    meross_channel = os.getenv('MEROSS_CHANNEL', None)
    meross_email = os.getenv('MEROSS_EMAIL', None)
    meross_password = os.getenv('MEROSS_PASSWORD', None)

    @app.route('/')
    def index():
        return 'Countdown API'

    @app.route('/countdown', methods=['POST'])
    def countdown():
        """
        curl -i -H "Content-Type: application/json" -X POST -d '{"interval":"10s"}' http://127.0.0.1:5000/countdown
        :return:
        """
        if not request.get_json() or 'interval' not in request.get_json():
            response_object = {
                "Error": "Wrong parameters, 'interval' not set"
            }
            return jsonify(error=response_object), 400

        # todo use a string timer code like 5s = 5 seconds, 10m = 10 minutes
        request_json_data = request.get_json()
        interval = request_json_data["interval"]

        seconds = IntervalString.get_second_from_sting(interval)

        if seconds is not None:
            conn1 = Redis('redis', 6379)
            with Connection(conn1):
                q = Queue('default')
                task = q.enqueue(countdown_task, meross_device, meross_channel, meross_email, meross_password, seconds)

            response_object = {
                'status': 'success',
                'data': {
                    'task_id': task.get_id(),
                    'interval': interval
                }
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                "Error": "Wrong parameters, 'interval' is not valid."
            }
            return jsonify(error=response_object), 400

    return app
