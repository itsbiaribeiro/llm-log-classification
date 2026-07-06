"""
Responsável pela exportação dos resultados da exploração.
"""

import csv
import json
from pathlib import Path


def exportar_estatisticas_csv(
    resultado,
    caminho_saida: Path,
):
    """
    Exporta as estatísticas dos arquivos para CSV.
    """

    caminho_saida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        caminho_saida,
        "w",
        newline="",
        encoding="utf-8",
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(
            [
                "arquivo",
                "linhas",
                "tamanho_mb",
                "info",
                "warn",
                "error",
                "debug",
                "trace",
                "fatal",
                "exceptions",
                "stack_traces",
            ]
        )

        for arquivo in resultado.arquivos:

            writer.writerow(
                [
                    arquivo.nome,
                    arquivo.linhas,
                    round(arquivo.tamanho_mb, 2),
                    arquivo.info,
                    arquivo.warn,
                    arquivo.error,
                    arquivo.debug,
                    arquivo.trace,
                    arquivo.fatal,
                    arquivo.excecoes,
                    arquivo.stack_traces,
                ]
            )


def exportar_resumo_json(
    resultado,
    caminho_saida: Path,
):
    """
    Exporta um resumo do dataset em JSON.
    """

    caminho_saida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    resumo = {
        "dataset": resultado.nome,
        "arquivos": resultado.total_arquivos,
        "linhas": resultado.total_linhas,
        "tamanho_mb": round(
            resultado.tamanho_total_mb,
            2,
        ),
        "info": resultado.info,
        "warn": resultado.warn,
        "error": resultado.error,
        "debug": resultado.debug,
        "trace": resultado.trace,
        "fatal": resultado.fatal,
        "exceptions": resultado.excecoes,
        "stack_traces": resultado.stack_traces,
    }

    with open(
        caminho_saida,
        "w",
        encoding="utf-8",
    ) as jsonfile:

        json.dump(
            resumo,
            jsonfile,
            indent=4,
            ensure_ascii=False,
        )


def exportar_templates_csv(
    templates,
    caminho_saida: Path,
):
    """
    Exporta os templates minerados para CSV.
    """

    caminho_saida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        caminho_saida,
        "w",
        newline="",
        encoding="utf-8",
    ) as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow(
            [
                "id",
                "template",
                "ocorrencias",
            ]
        )

        for indice, template in enumerate(
            templates,
            start=1,
        ):

            writer.writerow(
                [
                    indice,
                    template.texto,
                    template.ocorrencias,
                ]
            )
