from database.database import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    preferencias = db.Column(db.String(500))
    orcamento_max = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "preferencias": self.preferencias,
            "orcamento_max": self.orcamento_max
        }