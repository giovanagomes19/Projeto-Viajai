from flask import request, jsonify

from service.roteiro.criar_roteiro_service import CriarRoteiroService
from service.roteiro.listar_roteiros_service import ListarRoteirosService
from service.roteiro.buscar_roteiro_service import BuscarRoteiroService
from service.roteiro.atualizar_roteiro_service import AtualizarRoteiroService
from service.roteiro.deletar_roteiro_service import DeletarRoteiroService


class RoteiroController:

    @staticmethod
    def criar():
        dados = request.get_json()

        try:
            roteiro = CriarRoteiroService.executar(dados)
            return jsonify(roteiro.to_dict()), 201
        except Exception as erro:
            return jsonify({"erro": str(erro)}), 400

    @staticmethod
    def listar():
        roteiros = ListarRoteirosService.executar()

        return jsonify([
            roteiro.to_dict()
            for roteiro in roteiros
        ]), 200

    @staticmethod
    def buscar(roteiro_id):
        roteiro = BuscarRoteiroService.executar(roteiro_id)

        if roteiro is None:
            return jsonify({"erro": "Roteiro não encontrado"}), 404

        return jsonify(roteiro.to_dict()), 200

    @staticmethod
    def atualizar(roteiro_id):
        dados = request.get_json()

        roteiro = AtualizarRoteiroService.executar(
            roteiro_id,
            dados
        )

        if roteiro is None:
            return jsonify({"erro": "Roteiro não encontrado"}), 404

        return jsonify(roteiro.to_dict()), 200

    @staticmethod
    def deletar(roteiro_id):
        sucesso = DeletarRoteiroService.executar(roteiro_id)

        if not sucesso:
            return jsonify({"erro": "Roteiro não encontrado"}), 404

        return jsonify({
            "mensagem": "Roteiro excluído com sucesso"
        }), 200