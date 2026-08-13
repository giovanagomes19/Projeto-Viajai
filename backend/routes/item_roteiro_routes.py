from flask import Blueprint

from controller.item_roteiro_controller import ItemRoteiroController


item_roteiro_routes = Blueprint(
    "item_roteiro_routes",
    __name__
)


item_roteiro_routes.route(
    "/itens-roteiro",
    methods=["POST"]
)(ItemRoteiroController.criar)

item_roteiro_routes.route(
    "/itens-roteiro",
    methods=["GET"]
)(ItemRoteiroController.listar)

item_roteiro_routes.route(
    "/itens-roteiro/<int:item_id>",
    methods=["GET"]
)(ItemRoteiroController.buscar)

item_roteiro_routes.route(
    "/itens-roteiro/<int:item_id>",
    methods=["PUT"]
)(ItemRoteiroController.atualizar)

item_roteiro_routes.route(
    "/itens-roteiro/<int:item_id>",
    methods=["DELETE"]
)(ItemRoteiroController.deletar)