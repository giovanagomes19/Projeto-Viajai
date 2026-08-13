from flask import request, jsonify

from service.usuario.CriarUsuarioService import CriarUsuarioService
from service.usuario.ListarUsuariosService import ListarUsuariosService
from service.usuario.BuscarUsuarioService import BuscarUsuarioService
from service.usuario.AtualizarUsuarioService import AtualizarUsuarioService
from service.usuario.DeletarUsuarioService import DeletarUsuarioService


class UsuarioController:

    @staticmethod
    def criar():
        dados = request.get_json()

        try:
            usuario = CriarUsuarioService.executar(dados)

            return jsonify(usuario.to_dict()), 201

        except Exception as erro:
            return jsonify({"erro": str(erro)}), 400

    @staticmethod
    def listar():
        usuarios = ListarUsuariosService.executar()

        return jsonify([
            usuario.to_dict()
            for usuario in usuarios
        ]), 200

    @staticmethod
    def buscar(usuario_id):
        usuario = BuscarUsuarioService.executar(usuario_id)

        if usuario is None:
            return jsonify({"erro": "Usuário não encontrado"}), 404

        return jsonify(usuario.to_dict()), 200

    @staticmethod
    def atualizar(usuario_id):
        dados = request.get_json()

        usuario = AtualizarUsuarioService.executar(
            usuario_id,
            dados
        )

        if usuario is None:
            return jsonify({"erro": "Usuário não encontrado"}), 404

        return jsonify(usuario.to_dict()), 200

    @staticmethod
    def deletar(usuario_id):
        sucesso = DeletarUsuarioService.executar(usuario_id)

        if not sucesso:
            return jsonify({"erro": "Usuário não encontrado"}), 404

        return jsonify({
            "mensagem": "Usuário excluído com sucesso"
        }), 200