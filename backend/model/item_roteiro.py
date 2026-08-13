from database.database import db


class ItemRoteiro(db.Model):
    __tablename__ = "itens_roteiro"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    ordem = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "ordem": self.ordem
        }