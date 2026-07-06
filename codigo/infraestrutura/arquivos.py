"""
Manipulação de arquivos e diretórios.
"""

from pathlib import Path

from config import EXTENSOES_LOG


def criar_diretorio(caminho: Path) -> None:
    """
    Cria um diretório caso ele não exista.
    """

    caminho.mkdir(parents=True, exist_ok=True)


def listar_arquivos_log(diretorio: Path) -> list[Path]:
    """
    Retorna todos os arquivos de log encontrados no diretório informado.
    """

    arquivos = []

    for arquivo in diretorio.iterdir():

        if arquivo.is_file() and arquivo.suffix.lower() in EXTENSOES_LOG:
            arquivos.append(arquivo)

    return sorted(arquivos)
