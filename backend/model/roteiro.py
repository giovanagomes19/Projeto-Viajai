from database.database import db


class Roteiro(db.Model):
    __tablename__ = "roteiros"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    custo_estimado = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data.isoformat(),
            "custo_estimado": self.custo_estimado
        }