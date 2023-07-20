
from flask import Blueprint, jsonify, request, abort
from marshmallow.exceptions import ValidationError
from ..models.Game import Game
from ..models.Inning import Inning, InningSchema
from ..config import app, db

innings = Blueprint("inning", __name__)


@app.route("/innings", methods=["POST"])
def create_inning():
    if not request.is_json:
        abort(400, "Must supply a JSON body.")
    try:
        result = InningSchema().load(request.json)
    except ValidationError as err:
        abort(400, jsonify(err.messages))

    inning = Inning(**result)
    db.session.add(inning)
    db.session.commit()
    return jsonify({"inning": inning.id}), 201


@app.route("/innings", methods=["GET"])
def get_all_innings():
    game_id = request.args.get("game", type=int)
    _ = Game.query.get_or_404(game_id)
    schema = InningSchema(many=True)
    results = db.session.query(Inning).join(
        Game).filter(Game.id == game_id).all()

    return schema.jsonify(results), 200


@app.route("/innings/<int:inning_id>", methods=["GET"])
def get_inning(inning_id):
    inning = Inning.query.get_or_404(inning_id)
    schema = InningSchema()
    return schema.jsonify(inning), 200


@app.route("/innings/<int:inning_id>", methods=["DELETE"])
def delete_inning(inning_id):
    inning = Inning.query.get_or_404(inning_id)
    db.session.delete(inning)
    db.session.commit()
    return "success", 204


@app.route("/innings/<int:inning_id>", methods=["PUT"])
def update_inning(inning_id):
    schema = InningSchema()
    _ = Inning.query.get_or_404(inning_id)
    if not request.is_json:
        abort(400, "Must supply a JSON body.")
    try:
        result = InningSchema().load(request.json)
    except ValidationError as err:
        abort(400, jsonify(err.messages))

    patch = Inning(**result)
    patch.id = inning_id

    updated_inning = db.session.merge(patch)
    db.session.commit()
    return schema.jsonify(updated_inning), 200
