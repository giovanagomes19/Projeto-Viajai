from model.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository


class CriarUsuarioService:

    @staticmethod
    def executar(dados):
        usuario = Usuario(
            nome=dados["nome"],
            email=dados["email"],
            preferencias=dados.get("preferencias"),
            orcamento_max=dados.get("orcamento_max")
        )

        return UsuarioRepository.criar(usuario)