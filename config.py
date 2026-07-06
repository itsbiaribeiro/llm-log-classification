from pathlib import Path


RAIZ_PROJETO = Path(__file__).resolve().parent

DADOS_BRUTOS = RAIZ_PROJETO / "dados" / "brutos"

DADOS_EMPRESA = DADOS_BRUTOS / "empresa"

DADOS_HDFS = DADOS_BRUTOS / "hdfs"

DADOS_ANONIMIZADOS = (
    RAIZ_PROJETO
    / "dados"
    / "anonimizados"
)

DADOS_EMPRESA_ANONIMIZADOS = (
    DADOS_ANONIMIZADOS
    / "empresa"
)

DADOS_PROCESSADOS = (
    RAIZ_PROJETO
    / "dados"
    / "processados"
)

DADOS_ROTULADOS = (
    RAIZ_PROJETO
    / "dados"
    / "rotulados"
)

RESULTADOS = (
    RAIZ_PROJETO
    / "resultados"
)

RESULTADOS_EXPLORACAO = (
    RESULTADOS
    / "exploracao"
)

RESULTADOS_EXPERIMENTOS = (
    RESULTADOS
    / "experimentos"
)

RESULTADOS_FIGURAS = (
    RESULTADOS
    / "figuras"
)

RESULTADOS_TABELAS = (
    RESULTADOS
    / "tabelas"
)

EXTENSOES_LOG = (
    ".log",
    ".out",
)
