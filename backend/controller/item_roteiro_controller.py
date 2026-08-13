from flask import request, jsonify

from service.item_roteiro.criar_item_roteiro_service import CriarItemRoteiroService
from service.item_roteiro.listar_itens_roteiro_service import ListarItensRoteiroService
from service.item_roteiro.buscar_item_roteiro_service import BuscarItemRoteiroService
from service.item_roteiro.atualizar_item_roteiro_service import AtualizarItemRoteiroService
from service.item_roteiro.deletar_item_roteiro_service import DeletarItemRoteiroService


class ItemRoteiroController:

    @staticmethod
    def criar():
        dados = request.get_json()

        try:
            item = CriarItemRoteiroService.executar(dados)
            return jsonify(item.to_dict()), 201
        except Exception as erro:
            return jsonify({"erro": str(erro)}), 400

    @staticmethod
    def listar():
        itens = ListarItensRoteiroService.executar()

        return jsonify([
            item.to_dict()
            for item in itens
        ]), 200

    @staticmethod
    def buscar(item_id):
        item = BuscarItemRoteiroService.executar(item_id)

        if item is None:
            return jsonify({
                "erro": "Item de roteiro nao encontrado"
            }), 404

        return jsonify(item.to_dict()), 200

    @staticmethod
    def atualizar(item_id):
        dados = request.get_json()

        item = AtualizarItemRoteiroService.executar(
            item_id,
            dados
        )

        if item is None:
            return jsonify({
                "erro": "Item de roteiro nao encontrado"
            }), 404

        return jsonify(item.to_dict()), 200

    @staticmethod
    def deletar(item_id):
        sucesso = DeletarItemRoteiroService.executar(item_id)

        if not sucesso:
            return jsonify({
                "erro": "Item de roteiro nao encontrado"
            }), 404

        return jsonify({
            "mensagem": "Item de roteiro excluido com sucesso"
        }), 200