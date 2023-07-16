from ..config import db, ma
from marshmallow import fields


class Innning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.Integer, db.ForeignKey("game.id"))
    inning_no = db.Column(
        db.Integer,
    )


class InningSchema(ma.Schema):
    game = fields.Integer()

    class Meta:
        fields = (
            "id",
            "home_team",
            "away_team",
            "date",
            "start_time",
            "end_time",
        )
