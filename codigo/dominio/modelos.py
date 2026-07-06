"""
Modelos de domínio do projeto.
"""

from dataclasses import dataclass, field
from pathlib import Path

from codigo.dominio.categorias import CategoriaFalha


@dataclass
class PadraoAnonimizacao:

    nome: str

    regex: str

    substituto: str


@dataclass
class EstatisticasArquivo:

    caminho: Path

    nome: str

    linhas: int = 0

    tamanho_mb: float = 0.0

    info: int = 0
    warn: int = 0
    error: int = 0
    debug: int = 0
    trace: int = 0
    fatal: int = 0

    excecoes: int = 0

    stack_traces: int = 0

    possui_timestamp: bool = False

    primeira_linha: str = ""

    ultima_linha: str = ""


@dataclass
class EstatisticasDataset:

    nome: str

    arquivos: list[EstatisticasArquivo] = field(default_factory=list)

    total_arquivos: int = 0

    total_linhas: int = 0

    tamanho_total_mb: float = 0.0

    info: int = 0
    warn: int = 0
    error: int = 0
    debug: int = 0
    trace: int = 0
    fatal: int = 0

    excecoes: int = 0
    stack_traces: int = 0


@dataclass
class TemplateLog:
    """
    Representa um template de log identificado
    durante a mineração.
    """

    texto: str

    ocorrencias: int = 0


@dataclass
class CategoriaLog:
    """
    Representa um template associado
    a uma categoria de falha.
    """

    template: TemplateLog

    categoria: CategoriaFalha

    confianca: float = 1.0


@dataclass
class ResultadoClassificacao:
    """
    Representa o resultado produzido
    por um classificador.
    """

    texto: str

    categoria_real: str

    categoria_predita: str

    metodo: str

    confianca: float = 1.0
