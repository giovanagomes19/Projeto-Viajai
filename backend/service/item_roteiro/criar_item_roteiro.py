from model.item_roteiro import ItemRoteiro
from repositories.item_roteiro_repository import ItemRoteiroRepository


class CriarItemRoteiroService:

    @staticmethod
    def executar(dados):
        item = ItemRoteiro(
            descricao=dados["descricao"],
            ordem=dados["ordem"]
        )

        return ItemRoteiroRepository.criar(item)