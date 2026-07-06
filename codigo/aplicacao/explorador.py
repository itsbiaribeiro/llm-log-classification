"""
Caracterização dos datasets.
"""

from pathlib import Path

from codigo.dominio.modelos import (
    EstatisticasArquivo,
    EstatisticasDataset,
)

from codigo.infraestrutura.arquivos import listar_arquivos_log


class ExploradorDataset:
    """
    Realiza a caracterização estrutural
    de um conjunto de arquivos de log.
    """

    def analisar_dataset(
        self,
        nome_dataset: str,
        diretorio: Path,
    ) -> EstatisticasDataset:

        estatisticas = EstatisticasDataset(nome=nome_dataset)

        arquivos = listar_arquivos_log(diretorio)

        estatisticas.total_arquivos = len(arquivos)

        for arquivo in arquivos:

            resultado = self.analisar_arquivo(arquivo)

            estatisticas.arquivos.append(resultado)

            estatisticas.total_linhas += resultado.linhas
            estatisticas.tamanho_total_mb += resultado.tamanho_mb

            estatisticas.info += resultado.info
            estatisticas.warn += resultado.warn
            estatisticas.error += resultado.error
            estatisticas.debug += resultado.debug
            estatisticas.trace += resultado.trace
            estatisticas.fatal += resultado.fatal

            estatisticas.excecoes += resultado.excecoes
            estatisticas.stack_traces += resultado.stack_traces

        return estatisticas

    def obter_nivel_log(
        self,
        linha: str,
    ) -> str | None:
        """
        Identifica o nível do log independentemente do formato.
        """

        linha_maiuscula = linha.upper()

        # -------- JSON --------
        if '"LEVEL":"INFO"' in linha_maiuscula:
            return "INFO"

        if '"LEVEL":"WARN"' in linha_maiuscula:
            return "WARN"

        if '"LEVEL":"ERROR"' in linha_maiuscula:
            return "ERROR"

        if '"LEVEL":"DEBUG"' in linha_maiuscula:
            return "DEBUG"

        if '"LEVEL":"TRACE"' in linha_maiuscula:
            return "TRACE"

        if '"LEVEL":"FATAL"' in linha_maiuscula:
            return "FATAL"

        # -------- Texto --------
        for nivel in (
            "INFO",
            "WARN",
            "ERROR",
            "DEBUG",
            "TRACE",
            "FATAL",
        ):

            if f" {nivel} " in linha_maiuscula:
                return nivel

            if f" {nivel}:" in linha_maiuscula:
                return nivel

        return None

    def analisar_arquivo(
        self,
        caminho_arquivo: Path,
    ) -> EstatisticasArquivo:
        """
        Analisa um único arquivo de log.
        """

        estatisticas = EstatisticasArquivo(
            caminho=caminho_arquivo,
            nome=caminho_arquivo.name,
        )

        estatisticas.tamanho_mb = (
            caminho_arquivo.stat().st_size
            / (1024 * 1024)
        )

        with open(
            caminho_arquivo,
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as arquivo:

            for linha in arquivo:

                linha = linha.rstrip()

                if estatisticas.linhas == 0:
                    estatisticas.primeira_linha = linha

                estatisticas.ultima_linha = linha

                estatisticas.linhas += 1

                nivel = self.obter_nivel_log(linha)

                if nivel == "INFO":
                    estatisticas.info += 1

                elif nivel == "WARN":
                    estatisticas.warn += 1

                elif nivel == "ERROR":
                    estatisticas.error += 1

                elif nivel == "DEBUG":
                    estatisticas.debug += 1

                elif nivel == "TRACE":
                    estatisticas.trace += 1

                elif nivel == "FATAL":
                    estatisticas.fatal += 1

                linha_maiuscula = linha.upper()

                if "EXCEPTION" in linha_maiuscula:
                    estatisticas.excecoes += 1

                if linha.startswith("\tat") or linha.startswith("at "):
                    estatisticas.stack_traces += 1

                if estatisticas.linhas == 1:

                    if "-" in linha[:30] or ":" in linha[:30]:
                        estatisticas.possui_timestamp = True

        return estatisticas
