from .config import app, db
from .routes.games import games

app.register_blueprint(games)


with app.app_context():
    db.create_all()
