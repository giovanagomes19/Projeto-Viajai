from datetime import date

from model.viagem import Viagem
from repositories.viagem_repository import ViagemRepository


class CriarViagemService:

    @staticmethod
    def executar(dados):
        viagem = Viagem(
            destino=dados["destino"],
            data_inicio=date.fromisoformat(dados["data_inicio"]),
            data_fim=date.fromisoformat(dados["data_fim"]),
            orcamento_total=dados.get("orcamento_total")
        )

        return ViagemRepository.criar(viagem)