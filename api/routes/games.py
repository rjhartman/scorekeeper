
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


@app.route("/games", methods=["PUT"])
def update_game():
    schema = GameSchema()
    if not request.is_json:
        abort(400, "Must supply a JSON body.")
    try:
        result = GameSchema().load(request.json)
    except ValidationError as err:
        abort(400, jsonify(err.messages))

    patch = Game(**result)
    if not patch.id:
        abort(400, "Must provide id in request body")

    # we could put a check in here to make sure that the id exists in the db
    # and abort if it's not found
    # right now merge() will attempt to update an existing instance if it finds
    # a matching id. else returns a new instance

    updated_game = db.session.merge(patch)
    db.session.commit()
    return schema.jsonify(updated_game), 200
