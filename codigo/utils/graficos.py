"""
Geração de gráficos utilizados no artigo.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from codigo.dominio.modelos import EstatisticasDataset


def grafico_niveis_log(
    estatisticas: EstatisticasDataset,
    caminho_saida: Path,
) -> None:
    """
    Gera um gráfico de barras com a distribuição
    dos níveis de log.
    """

    caminho_saida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    niveis = [
        "INFO",
        "WARN",
        "ERROR",
        "DEBUG",
        "TRACE",
        "FATAL",
    ]

    valores = [
        estatisticas.info,
        estatisticas.warn,
        estatisticas.error,
        estatisticas.debug,
        estatisticas.trace,
        estatisticas.fatal,
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(niveis, valores)

    plt.title("Distribuição dos níveis de log")

    plt.xlabel("Nível")

    plt.ylabel("Quantidade")

    plt.tight_layout()

    plt.savefig(caminho_saida)

    plt.close()
