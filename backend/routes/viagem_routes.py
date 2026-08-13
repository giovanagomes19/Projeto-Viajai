from flask import Blueprint

from controller.viagem_controller import ViagemController


viagem_routes = Blueprint("viagem_routes", __name__)


viagem_routes.route("/viagens", methods=["POST"])(
    ViagemController.criar
)

viagem_routes.route("/viagens", methods=["GET"])(
    ViagemController.listar
)

viagem_routes.route("/viagens/<int:viagem_id>", methods=["GET"])(
    ViagemController.buscar
)

viagem_routes.route("/viagens/<int:viagem_id>", methods=["PUT"])(
    ViagemController.atualizar
)

viagem_routes.route("/viagens/<int:viagem_id>", methods=["DELETE"])(
    ViagemController.deletar
)