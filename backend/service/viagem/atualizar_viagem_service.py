from datetime import date

from repositories.viagem_repository import ViagemRepository


class AtualizarViagemService:

    @staticmethod
    def executar(viagem_id, dados):
        viagem = ViagemRepository.buscar_por_id(viagem_id)

        if viagem is None:
            return None

        viagem.destino = dados.get("destino", viagem.destino)

        if "data_inicio" in dados:
            viagem.data_inicio = date.fromisoformat(dados["data_inicio"])

        if "data_fim" in dados:
            viagem.data_fim = date.fromisoformat(dados["data_fim"])

        viagem.orcamento_total = dados.get(
            "orcamento_total",
            viagem.orcamento_total
        )

        ViagemRepository.atualizar()

        return viagem