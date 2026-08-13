from database.database import db
from model.roteiro import Roteiro


class RoteiroRepository:

    @staticmethod
    def criar(roteiro):
        db.session.add(roteiro)
        db.session.commit()
        return roteiro

    @staticmethod
    def listar():
        return Roteiro.query.all()

    @staticmethod
    def buscar_por_id(roteiro_id):
        return Roteiro.query.get(roteiro_id)

    @staticmethod
    def atualizar():
        db.session.commit()

    @staticmethod
    def deletar(roteiro):
        db.session.delete(roteiro)
        db.session.commit()