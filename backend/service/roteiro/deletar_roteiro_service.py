from repositories.roteiro_repository import RoteiroRepository


class DeletarRoteiroService:

    @staticmethod
    def executar(roteiro_id):
        roteiro = RoteiroRepository.buscar_por_id(roteiro_id)

        if roteiro is None:
            return False

        RoteiroRepository.deletar(roteiro)

        return True