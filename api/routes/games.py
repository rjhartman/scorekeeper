from flask import Blueprint, jsonify, request, abort
from marshmallow.exceptions import ValidationError
from ..models.Game import Game, GameSchema
from ..config import app, db

games = Blueprint("game", __name__)


@app.route("/games", methods=["POST"])
def create_game():
    if not request.is_json:
        abort(400, "Must supply a JSON body.")
    try:
        result = GameSchema().load(request.json)
    except ValidationError as err:
        abort(400, jsonify(err.messages))

    game = Game(**result)
    db.session.add(game)
    db.session.commit()
    return jsonify({"game": game.id}), 201


@app.route("/games/<int:game_id>", methods=["GET"])
def get_game(game_id):
    game = Game.query.get_or_404(game_id)
    schema = GameSchema()
    return schema.jsonify(game), 200


@app.route("/games/<int:game_id>", methods=["DELETE"])
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return "success", 204


@app.route("/games/<int:game_id>", methods=["PUT"])
def update_game(game_id):
    schema = GameSchema()
    _ = Game.query.get_or_404(game_id)
    if not request.is_json:
        abort(400, "Must supply a JSON body.")
    try:
        result = GameSchema().load(request.json)
    except ValidationError as err:
        abort(400, jsonify(err.messages))

    patch = Game(**result)
    patch.id = game_id

    updated_game = db.session.merge(patch)
    db.session.commit()
    return schema.jsonify(updated_game), 200
