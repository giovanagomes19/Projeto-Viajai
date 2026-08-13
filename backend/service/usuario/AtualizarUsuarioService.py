from repositories.usuario_repository import UsuarioRepository


class AtualizarUsuarioService:

    @staticmethod
    def executar(usuario_id, dados):
        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if usuario is None:
            return None

        usuario.nome = dados.get("nome", usuario.nome)
        usuario.email = dados.get("email", usuario.email)
        usuario.preferencias = dados.get(
            "preferencias",
            usuario.preferencias
        )
        usuario.orcamento_max = dados.get(
            "orcamento_max",
            usuario.orcamento_max
        )

        UsuarioRepository.atualizar()

        return usuario