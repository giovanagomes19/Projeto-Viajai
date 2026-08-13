from repositories.viagem_repository import ViagemRepository


class ListarViagensService:

    @staticmethod
    def executar():
        return ViagemRepository.listar()