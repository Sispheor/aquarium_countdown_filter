import redis
from flask.cli import FlaskGroup
from redis import Redis
from rq import Worker, Connection, Queue

from api.app import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('run_worker')
def run_worker():
    print("run worker")
    conn1 = Redis('localhost', 6379)
    with Connection(conn1):
        q1 = Queue('default')
        worker = Worker([q1])
        worker.work()


if __name__ == '__main__':
    cli()
