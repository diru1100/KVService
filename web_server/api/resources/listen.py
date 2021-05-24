from flask_restful import Resource
import flask
from .store import announcer
from flask import request
from .. import db
from ..common.models import Record
import sys


class Listener(Resource):

    def get(self):

        given_key = request.args["key"]
        record = Record.query.filter_by(key=given_key).first()
        if record is None:
            return "Record not found", 400

        def stream():

            messages = announcer.listen(given_key)  # returns a queue.Queue
            while True:
                msg = messages.get()  # blocks until a new message arrives
                yield msg

        return flask.Response(stream(), mimetype='text/event-stream')
