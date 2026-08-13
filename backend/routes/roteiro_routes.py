from flask import Blueprint

from controller.roteiro_controller import RoteiroController


roteiro_routes = Blueprint("roteiro_routes", __name__)


roteiro_routes.route("/roteiros", methods=["POST"])(
    RoteiroController.criar
)

roteiro_routes.route("/roteiros", methods=["GET"])(
    RoteiroController.listar
)

roteiro_routes.route("/roteiros/<int:roteiro_id>", methods=["GET"])(
    RoteiroController.buscar
)

roteiro_routes.route("/roteiros/<int:roteiro_id>", methods=["PUT"])(
    RoteiroController.atualizar
)

roteiro_routes.route("/roteiros/<int:roteiro_id>", methods=["DELETE"])(
    RoteiroController.deletar
)