"""
Mineração de templates de logs.
"""

from collections import Counter
from pathlib import Path
import re

from codigo.dominio.modelos import TemplateLog


PADROES_IGNORADOS = (
    "at ",
    "\tat",
    "caused by:",
    "suppressed:",
    "...",
)


class MineradorTemplates:

    def minerar_diretorio(
        self,
        diretorio: Path,
        limite: int | None = None,
    ) -> list[TemplateLog]:

        contador = Counter()

        arquivos = sorted(
            list(diretorio.glob("*.log"))
            + list(diretorio.glob("*.out"))
        )

        for caminho in arquivos:

            with open(
                caminho,
                "r",
                encoding="utf-8",
                errors="ignore",
            ) as arquivo:

                for linha in arquivo:

                    mensagem = self.extrair_mensagem(
                        linha
                    )

                    if not mensagem:
                        continue

                    template = self.normalizar(
                        mensagem
                    )

                    if len(template) < 20:
                        continue

                    contador[template] += 1

        templates = [

            TemplateLog(
                texto=texto,
                ocorrencias=ocorrencias,
            )

            for texto, ocorrencias in contador.items()

        ]

        templates.sort(
            key=lambda x: x.ocorrencias,
            reverse=True,
        )

        if limite is not None:

            return templates[:limite]

        return templates

    def extrair_mensagem(
        self,
        linha: str,
    ) -> str:

        linha = linha.strip()

        if not linha:

            return ""

        linha_lower = linha.lower()

        for padrao in PADROES_IGNORADOS:

            if linha_lower.startswith(
                padrao
            ):

                return ""

        # JSON

        if '"message":"' in linha:

            match = re.search(
                r'"message":"(.*?)"',
                linha,
            )

            if match:

                return match.group(1)

        # Logs tradicionais

        if ":" in linha:

            partes = linha.split(
                ":",
                1,
            )

            if len(partes) == 2:

                return partes[1].strip()

        return linha

    def normalizar(
        self,
        texto: str,
    ) -> str:

        texto = texto.lower()

        # Blocos HDFS

        texto = re.sub(
            r"blk_-?\d+",
            "<block>",
            texto,
        )

        # IP

        texto = re.sub(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "<ip>",
            texto,
        )

        # UUID

        texto = re.sub(
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}",
            "<uuid>",
            texto,
        )

        # Hexadecimal

        texto = re.sub(
            r"0x[a-f0-9]+",
            "<hex>",
            texto,
        )

        # Datas

        texto = re.sub(
            r"\d{4}-\d{2}-\d{2}",
            "<date>",
            texto,
        )

        # Horários

        texto = re.sub(
            r"\d{2}:\d{2}:\d{2}(?:,\d+)?",
            "<time>",
            texto,
        )

        # IDs grandes

        texto = re.sub(
            r"\b\d{5,}\b",
            "<id>",
            texto,
        )

        # Números

        texto = re.sub(
            r"\b\d+\b",
            "<num>",
            texto,
        )

        # Espaços

        texto = re.sub(
            r"\s+",
            " ",
            texto,
        )

        return texto.strip()
