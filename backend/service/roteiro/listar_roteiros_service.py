from repositories.roteiro_repository import RoteiroRepository


class ListarRoteirosService:

    @staticmethod
    def executar():
        return RoteiroRepository.listar()