"""
Pipeline principal da pesquisa.
"""

from config import (
    DADOS_EMPRESA,
    DADOS_HDFS,
    DADOS_EMPRESA_ANONIMIZADOS,
    RESULTADOS_EXPLORACAO,
    RESULTADOS_EXPERIMENTOS,
)

from codigo.aplicacao.explorador import ExploradorDataset
from codigo.aplicacao.anonimizador import Anonimizador
from codigo.aplicacao.minerador_templates import MineradorTemplates

from codigo.infraestrutura.arquivos import listar_arquivos_log

from codigo.infraestrutura.exportador import (
    exportar_estatisticas_csv,
    exportar_resumo_json,
    exportar_templates_csv,
)

from codigo.utils.graficos import grafico_niveis_log

# EXPLORAÇÃO


def executar_exploracao(
    nome_dataset,
    diretorio,
):

    explorador = ExploradorDataset()

    resultado = explorador.analisar_dataset(
        nome_dataset=nome_dataset,
        diretorio=diretorio,
    )

    print()
    print(f"DATASET: {resultado.nome.upper()}")

    print(f"Arquivos.......: {resultado.total_arquivos}")
    print(f"Linhas.........: {resultado.total_linhas:,}")
    print(f"Tamanho (MB)...: {resultado.tamanho_total_mb:.2f}")

    print()
    print("----- NÍVEIS DE LOG -----")

    print(f"INFO............: {resultado.info:,}")
    print(f"WARN............: {resultado.warn:,}")
    print(f"ERROR...........: {resultado.error:,}")
    print(f"DEBUG...........: {resultado.debug:,}")
    print(f"TRACE...........: {resultado.trace:,}")
    print(f"FATAL...........: {resultado.fatal:,}")

    print()
    print("----- EXCEÇÕES -----")

    print(f"Exceptions......: {resultado.excecoes:,}")
    print(f"Stack Traces....: {resultado.stack_traces:,}")

    print()

    for arquivo in resultado.arquivos:

        print("-" * 60)

        print(f"Arquivo........: {arquivo.nome}")
        print(f"Linhas.........: {arquivo.linhas:,}")
        print(f"Tamanho (MB)...: {arquivo.tamanho_mb:.2f}")

        print(f"Primeira.......: {arquivo.primeira_linha[:80]}")
        print(f"Última.........: {arquivo.ultima_linha[:80]}")

    pasta_saida = RESULTADOS_EXPLORACAO / resultado.nome.lower()

    exportar_estatisticas_csv(
        resultado,
        pasta_saida / "estatisticas.csv",
    )

    exportar_resumo_json(
        resultado,
        pasta_saida / "resumo.json",
    )

    grafico_niveis_log(
        resultado,
        pasta_saida / "niveis_log.png",
    )

    print()
    print("Artefatos exportados com sucesso!")
    print(f"Pasta: {pasta_saida}")


# ANONIMIZAÇÃO

def executar_anonimizacao():

    print()
    print("ANONIMIZAÇÃO")

    anonimizador = Anonimizador()

    arquivos = listar_arquivos_log(
        DADOS_EMPRESA,
    )

    total = 0

    for arquivo in arquivos:

        print()

        print(f"Processando {arquivo.name}...")

        destino = (
            DADOS_EMPRESA_ANONIMIZADOS
            / arquivo.name
        )

        anonimizador.anonimizar_arquivo(
            arquivo,
            destino,
        )

        print(f"OK -> {arquivo.name}")

        total += 1

    print()
    print(f"{total} arquivo(s) anonimizado(s).")


# MINERAÇÃO DE TEMPLATES

def executar_mineracao_templates():

    print()
    print("MINERAÇÃO DE TEMPLATES")

    minerador = MineradorTemplates()

    # EMPRESA

    print()
    print("Minerando templates da empresa...")

    templates_empresa = minerador.minerar_diretorio(
        DADOS_EMPRESA_ANONIMIZADOS,
        limite=100,
    )

    exportar_templates_csv(
        templates_empresa,
        RESULTADOS_EXPERIMENTOS /
        "empresa_templates.csv",
    )

    print(f"{len(templates_empresa)} templates exportados.")

    print()
    print("TOP 10 - EMPRESA")

    for template in templates_empresa[:10]:

        print(
            f"{template.ocorrencias:>6} | {template.texto}"
        )

    # HDFS

    print()
    print("Minerando templates do HDFS...")

    templates_hdfs = minerador.minerar_diretorio(
        DADOS_HDFS,
        limite=100,
    )

    exportar_templates_csv(
        templates_hdfs,
        RESULTADOS_EXPERIMENTOS /
        "hdfs_templates.csv",
    )

    print(f"{len(templates_hdfs)} templates exportados.")

    print()
    print("TOP 10 - HDFS")

    for template in templates_hdfs[:10]:

        print(
            f"{template.ocorrencias:>6} | {template.texto}"
        )

    print()
    print("Templates exportados com sucesso!")


# PIPELINE

def executar_pipeline():

    print("INICIANDO PIPELINE EXPERIMENTAL")

    # 1
    executar_exploracao(
        "Empresa",
        DADOS_EMPRESA,
    )

    # 2
    executar_exploracao(
        "HDFS",
        DADOS_HDFS,
    )

    # 3
    executar_anonimizacao()

    # 4
    executar_mineracao_templates()

    print()
    print("PIPELINE FINALIZADO")
