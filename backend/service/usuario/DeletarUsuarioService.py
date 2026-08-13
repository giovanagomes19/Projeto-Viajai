from repositories.usuario_repository import UsuarioRepository


class DeletarUsuarioService:

    @staticmethod
    def executar(usuario_id):
        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if usuario is None:
            return False

        UsuarioRepository.deletar(usuario)

        return True