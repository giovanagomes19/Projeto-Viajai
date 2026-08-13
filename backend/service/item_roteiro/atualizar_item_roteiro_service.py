from repositories.item_roteiro_repository import ItemRoteiroRepository


class AtualizarItemRoteiroService:

    @staticmethod
    def executar(item_id, dados):
        item = ItemRoteiroRepository.buscar_por_id(item_id)

        if item is None:
            return None

        item.descricao = dados.get("descricao", item.descricao)
        item.ordem = dados.get("ordem", item.ordem)

        ItemRoteiroRepository.atualizar()

        return item