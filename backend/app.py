from flask import Flask
from flask_cors import CORS

from database.database import db
from model.usuario import Usuario
from model.viagem import Viagem
from model.roteiro import Roteiro
from model.item_roteiro import ItemRoteiro

from routes.usuario_routes import usuario_routes
from routes.viagem_routes import viagem_routes
from routes.roteiro_routes import roteiro_routes
from routes.item_roteiro_routes import item_roteiro_routes


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///viajai.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

CORS(app)

app.register_blueprint(usuario_routes)
app.register_blueprint(viagem_routes)
app.register_blueprint(roteiro_routes)
app.register_blueprint(item_roteiro_routes)


@app.route("/")
def home():
    return {"message": "API ViaJai funcionando!"}


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)