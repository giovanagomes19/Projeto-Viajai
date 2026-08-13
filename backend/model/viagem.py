from database.database import db


class Viagem(db.Model):
    __tablename__ = "viagens"

    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(150), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    orcamento_total = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "destino": self.destino,
            "data_inicio": self.data_inicio.isoformat(),
            "data_fim": self.data_fim.isoformat(),
            "orcamento_total": self.orcamento_total
        }