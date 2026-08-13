from repositories.viagem_repository import ViagemRepository


class BuscarViagemService:

    @staticmethod
    def executar(viagem_id):
        return ViagemRepository.buscar_por_id(viagem_id)