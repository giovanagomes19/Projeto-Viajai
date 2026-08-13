from repositories.item_roteiro_repository import ItemRoteiroRepository


class ListarItensRoteiroService:

    @staticmethod
    def executar():
        return ItemRoteiroRepository.listar()