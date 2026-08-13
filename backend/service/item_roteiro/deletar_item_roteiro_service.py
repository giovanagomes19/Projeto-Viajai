from repositories.item_roteiro_repository import ItemRoteiroRepository


class DeletarItemRoteiroService:

    @staticmethod
    def executar(item_id):
        item = ItemRoteiroRepository.buscar_por_id(item_id)

        if item is None:
            return False

        ItemRoteiroRepository.deletar(item)

        return True