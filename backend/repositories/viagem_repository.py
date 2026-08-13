from database.database import db
from model.viagem import Viagem


class ViagemRepository:

    @staticmethod
    def criar(viagem):
        db.session.add(viagem)
        db.session.commit()
        return viagem

    @staticmethod
    def listar():
        return Viagem.query.all()

    @staticmethod
    def buscar_por_id(viagem_id):
        return Viagem.query.get(viagem_id)

    @staticmethod
    def atualizar():
        db.session.commit()

    @staticmethod
    def deletar(viagem):
        db.session.delete(viagem)
        db.session.commit()