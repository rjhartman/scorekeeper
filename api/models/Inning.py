from ..config import db, ma
from marshmallow import fields


class Innning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.Integer, db.ForeignKey("game.id"))
    inning_no = db.Column(db.Integer)
    half = db.Column(db.String)


class InningSchema(ma.Schema):
    game = fields.Integer()
    inning_no = fields.Integer()
    half = fields.String()

    class Meta:
        fields = (
            "id",
            "game",
            "inning_no",
            "half"
        )
