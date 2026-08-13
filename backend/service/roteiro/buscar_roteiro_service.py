from repositories.roteiro_repository import RoteiroRepository


class BuscarRoteiroService:

    @staticmethod
    def executar(roteiro_id):
        return RoteiroRepository.buscar_por_id(roteiro_id)