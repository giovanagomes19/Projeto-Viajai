from repositories.viagem_repository import ViagemRepository


class DeletarViagemService:

    @staticmethod
    def executar(viagem_id):
        viagem = ViagemRepository.buscar_por_id(viagem_id)

        if viagem is None:
            return False

        ViagemRepository.deletar(viagem)

        return True