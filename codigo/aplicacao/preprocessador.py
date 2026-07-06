"""
Pré-processamento dos logs.
"""

import re
from pathlib import Path


class Preprocessador:

    def preprocessar_linha(
        self,
        linha: str,
    ) -> str:
        """
        Realiza o pré-processamento de uma linha de log.
        """

        linha = linha.lower()

        linha = linha.replace("\t", " ")

        linha = re.sub(r"\s+", " ", linha)

        return linha.strip()

    def preprocessar_arquivo(
        self,
        entrada: Path,
        saida: Path,
    ) -> None:
        """
        Processa um arquivo linha a linha.
        """

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

                linha = self.preprocessar_linha(linha)

                if linha:

                    destino.write(linha + "\n")
