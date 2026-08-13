from database.database import db
from model.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def criar(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def listar():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(usuario_id):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def atualizar():
        db.session.commit()

    @staticmethod
    def deletar(usuario):
        db.session.delete(usuario)
        db.session.commit()