from pathlib import Path

from codigo.experimentos.executar_experimentos import (
    ExecutorExperimentos,
)

executor = ExecutorExperimentos()

executor.executar(

    Path("resultados/experimentos/hdfs_templates.csv"),

    Path("resultados/experimentos/resultado_hdfs.csv"),

    usar_llm=False,

)
