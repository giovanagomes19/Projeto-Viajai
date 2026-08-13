from repositories.usuario_repository import UsuarioRepository


class BuscarUsuarioService:

    @staticmethod
    def executar(usuario_id):
        return UsuarioRepository.buscar_por_id(usuario_id)