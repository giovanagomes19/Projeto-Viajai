from flask import request, jsonify

from service.viagem.criar_viagem_service import CriarViagemService
from service.viagem.listar_viagens_service import ListarViagensService
from service.viagem.buscar_viagem_service import BuscarViagemService
from service.viagem.atualizar_viagem_service import AtualizarViagemService
from service.viagem.deletar_viagem_service import DeletarViagemService


class ViagemController:

    @staticmethod
    def criar():
        dados = request.get_json()

        try:
            viagem = CriarViagemService.executar(dados)
            return jsonify(viagem.to_dict()), 201
        except Exception as erro:
            return jsonify({"erro": str(erro)}), 400

    @staticmethod
    def listar():
        viagens = ListarViagensService.executar()

        return jsonify([
            viagem.to_dict()
            for viagem in viagens
        ]), 200

    @staticmethod
    def buscar(viagem_id):
        viagem = BuscarViagemService.executar(viagem_id)

        if viagem is None:
            return jsonify({"erro": "Viagem não encontrada"}), 404

        return jsonify(viagem.to_dict()), 200

    @staticmethod
    def atualizar(viagem_id):
        dados = request.get_json()

        viagem = AtualizarViagemService.executar(
            viagem_id,
            dados
        )

        if viagem is None:
            return jsonify({"erro": "Viagem não encontrada"}), 404

        return jsonify(viagem.to_dict()), 200

    @staticmethod
    def deletar(viagem_id):
        sucesso = DeletarViagemService.executar(viagem_id)

        if not sucesso:
            return jsonify({"erro": "Viagem não encontrada"}), 404

        return jsonify({
            "mensagem": "Viagem excluída com sucesso"
        }), 200