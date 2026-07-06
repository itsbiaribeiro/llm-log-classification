"""
Anonimização de logs.
"""

import re
from pathlib import Path

from codigo.dominio.modelos import PadraoAnonimizacao


class Anonimizador:

    def __init__(self):

        self.padroes = [

            PadraoAnonimizacao(
                "IP",
                r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                "<IP>",
            ),

            PadraoAnonimizacao(
                "EMAIL",
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                "<EMAIL>",
            ),

            PadraoAnonimizacao(
                "URL",
                r"https?://\S+",
                "<URL>",
            ),

            PadraoAnonimizacao(
                "UUID",
                (
                    r"[0-9a-fA-F]{8}-"
                    r"[0-9a-fA-F]{4}-"
                    r"[0-9a-fA-F]{4}-"
                    r"[0-9a-fA-F]{4}-"
                    r"[0-9a-fA-F]{12}"
                ),
                "<UUID>",
            ),
        ]

    def anonimizar_linha(
        self,
        linha: str,
    ) -> str:

        for padrao in self.padroes:

            linha = re.sub(
                padrao.regex,
                padrao.substituto,
                linha,
            )

        return linha

    def anonimizar_arquivo(
        self,
        entrada: Path,
        saida: Path,
    ):

        saida.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            entrada,
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as origem, open(
            saida,
            "w",
            encoding="utf-8",
        ) as destino:

            for linha in origem:

                destino.write(
                    self.anonimizar_linha(linha)
                )
