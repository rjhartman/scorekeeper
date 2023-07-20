from .config import app, db
from .routes.games import games
from .routes.innings import innings

app.register_blueprint(games)
app.register_blueprint(innings)


with app.app_context():
    db.create_all()
