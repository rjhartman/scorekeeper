from ..config import db, ma
from marshmallow import fields


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String)
    away_team = db.Column(db.String)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    innings = db.relationship("Inning", backref="game")


class GameSchema(ma.Schema):

    home_team = fields.Str()
    away_team = fields.Str()
    date = fields.Date()
    start_time = fields.Time()
    end_time = fields.Time()

    class Meta:
        fields = (
            "id",
            "home_team",
            "away_team",
            "date",
            "start_time",
            "end_time",
        )
