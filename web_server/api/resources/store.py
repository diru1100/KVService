from flask_restful import Resource
from .. import db
from ..common.models import Record
from flask import request


class KeyValueStore(Resource):

    def get(self):
        # no validation is done, can be made more secure using marshmellow or webargs
        data = request.args
        store = Record.query.filter_by(key=data["key"]).first()
        return {store.key: store.value}, 200

    def post(self):

        given_key = request.form.get('key')
        given_value = request.form.get('value')
        record = Record(
            key=given_key,
            value=given_value
        )
        db.session.add(record)
        db.session.commit()
        return "Successfully Stored!!", 201

    def delete(self):

        given_key = request.get_data().decode("utf-8")

        record_to_be_deleted = Record.query.filter_by(key=given_key).first()
        db.session.delete(record_to_be_deleted)
        db.session.commit()
        return "Successfully Deleted!!", 201
