from repositories.item_roteiro_repository import ItemRoteiroRepository


class BuscarItemRoteiroService:

    @staticmethod
    def executar(item_id):
        return ItemRoteiroRepository.buscar_por_id(item_id)