from datetime import date

from repositories.roteiro_repository import RoteiroRepository


class AtualizarRoteiroService:

    @staticmethod
    def executar(roteiro_id, dados):
        roteiro = RoteiroRepository.buscar_por_id(roteiro_id)

        if roteiro is None:
            return None

        if "data" in dados:
            roteiro.data = date.fromisoformat(dados["data"])

        roteiro.custo_estimado = dados.get(
            "custo_estimado",
            roteiro.custo_estimado
        )

        RoteiroRepository.atualizar()

        return roteiro