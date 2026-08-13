from flask import Blueprint

from controller.usuario_controller import UsuarioController


usuario_routes = Blueprint("usuario_routes", __name__)


usuario_routes.route("/usuarios", methods=["POST"])(
    UsuarioController.criar
)

usuario_routes.route("/usuarios", methods=["GET"])(
    UsuarioController.listar
)

usuario_routes.route("/usuarios/<int:usuario_id>", methods=["GET"])(
    UsuarioController.buscar
)

usuario_routes.route("/usuarios/<int:usuario_id>", methods=["PUT"])(
    UsuarioController.atualizar
)

usuario_routes.route("/usuarios/<int:usuario_id>", methods=["DELETE"])(
    UsuarioController.deletar
)