from datetime import date

from model.roteiro import Roteiro
from repositories.roteiro_repository import RoteiroRepository


class CriarRoteiroService:

    @staticmethod
    def executar(dados):
        roteiro = Roteiro(
            data=date.fromisoformat(dados["data"]),
            custo_estimado=dados.get("custo_estimado")
        )

        return RoteiroRepository.criar(roteiro)