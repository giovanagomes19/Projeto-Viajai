from repositories.usuario_repository import UsuarioRepository


class ListarUsuariosService:

    @staticmethod
    def executar():
        return UsuarioRepository.listar()