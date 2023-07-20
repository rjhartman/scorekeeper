from ..config import db, ma
from marshmallow import fields


class Inning(db.Model):
    __tablename__ = "innings"
    id = db.Column(db.Integer, primary_key=True)
    inning_no = db.Column(db.Integer)  # > 0
    half = db.Column(db.String)  # ["top", "botttom"]
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))


class InningSchema(ma.Schema):
    inning_no = fields.Integer()
    half = fields.String()
    game_id = fields.Integer()

    class Meta:
        fields = (
            "id",
            "game_id",
            "inning_no",
            "half"
        )
