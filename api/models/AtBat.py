from ..config import db, ma
from marshmallow import fields


class AtBat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inning = db.Column(db.Integer, db.ForeignKey("inning.id"))
    batter_order = db.Column(db.Integer)


class AtBatSchema(ma.Schema):
    inning = fields.Integer()
    batter_order = fields.Integer()

    class Meta:
        fields = (
            "id",
            "inning",
            "batter_order"
        )
