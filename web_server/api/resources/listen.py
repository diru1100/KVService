from flask_restful import Resource
import flask
from .store import announcer
from flask import request


class Listener(Resource):

    def get(self):
        key = request.args["key"]

        def stream():

            messages = announcer.listen(key)  # returns a queue.Queue
            while True:
                msg = messages.get()  # blocks until a new message arrives
                yield msg

        return flask.Response(stream(), mimetype='text/event-stream')
