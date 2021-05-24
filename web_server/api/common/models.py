from .. import db
import sys
sys.path.append("..")


class Record(db.Model):
    # only model defining db schema
    key = db.Column(db.String(64), index=True, primary_key=True)
    value = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<{key}:{value}>'.format(key=self.key, value=self.value)
