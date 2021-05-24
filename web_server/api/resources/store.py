from os import environ
from flask_restful import Resource
from .. import db
from ..common.models import Record
from flask import request
from ..common.subscribe import MessageAnnouncer, format_sse

# instatiating announcer to be able to capture changes and check key subscribed or not
announcer = MessageAnnouncer()


class KeyValueStore(Resource):

    def get(self):
        # no validation is done, can be made more secure using marshmellow or webargs
        data = request.args
        message_to_be_passed = "Fetched"
        store = Record.query.filter_by(key=data["key"]).first()
        # exception to key not present in db
        try:
            # check if subscribed or not and send appropriate message
            if store is not None and store.key in announcer.listeners:
                msg = format_sse(data=message_to_be_passed, event=store.key)
                announcer.announce(msg=msg)
            return "{} details are {} : {}".format(
                message_to_be_passed, store.key, store.value), 200
        except:
            return "Key not found", 400

    def post(self):

        given_key = request.form.get('key')
        given_value = request.form.get('value')

        record_present = Record.query.filter_by(key=given_key).first()
        message_to_be_passed = "Stored !!"
        record = Record(
            key=given_key,
            value=given_value
        )

        if record_present:
            # pass if same value in db is sent
            if record_present.value == given_value:
                message_to_be_passed = "Unchaged !!"
                pass
            else:
                record_present.value = given_value
                db.session.add(record_present)
                db.session.commit()
                message_to_be_passed = "Updated !!"
        else:
            db.session.add(record)
            db.session.commit()
        # check if subscribed or not and send appropriate message
        if given_key in announcer.listeners:
            msg = format_sse(data=message_to_be_passed, event=given_key)
            announcer.announce(msg=msg)

        return "Successfully {} key: {}, value: {}".format(message_to_be_passed, given_key, given_value), 200

    # Optional didn't ask this one
    def delete(self):

        given_key = request.args["key"]

        record_to_be_deleted = Record.query.filter_by(key=given_key).first()
        db.session.delete(record_to_be_deleted)
        db.session.commit()
        return "Successfully Deleted!!", 201
