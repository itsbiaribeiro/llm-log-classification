"""
Executa os experimentos utilizando os três classificadores.

Entrada:
    hdfs_templates_rotulado.csv

Saída:
    resultado_experimento.csv
"""

from pathlib import Path
import csv

from codigo.classificadores.palavras_chave import (
    ClassificadorPalavrasChave,
)

from codigo.classificadores.tfidf import (
    ClassificadorTFIDF,
)

from codigo.classificadores.llm import (
    ClassificadorLLM,
)


class ExecutorAvaliacao:

    def __init__(self):

        self.keywords = ClassificadorPalavrasChave()

        self.tfidf = ClassificadorTFIDF()

        self.llm = None

    def executar(
        self,
        arquivo_entrada: Path,
        arquivo_saida: Path,
        usar_llm=False,
    ):

        if usar_llm:

            self.llm = ClassificadorLLM()

        with open(
            arquivo_entrada,
            encoding="utf-8",
        ) as entrada:

            leitor = csv.DictReader(
                entrada,
                delimiter=";",
            )

            with open(
                arquivo_saida,
                "w",
                newline="",
                encoding="utf-8",
            ) as saida:

                campos = [

                    "id",
                    "template",
                    "categoria_real",
                    "keywords",
                    "tfidf",
                    "llm",

                ]

                writer = csv.DictWriter(
                    saida,
                    fieldnames=campos,
                    delimiter=";",
                )

                writer.writeheader()

                for linha in leitor:

                    template = linha["template"]

                    categoria_real = linha["categoria_real"]

                    categoria_keywords = (
                        self.keywords
                        .classificar(template)
                        .value
                    )

                    categoria_tfidf = (
                        self.tfidf
                        .classificar(template)[0]
                        .value
                    )

                    categoria_llm = ""

                    if usar_llm:

                        categoria_llm = (
                            self.llm
                            .classificar(template)[0]
                            .value
                        )

                    writer.writerow(

                        {

                            "id": linha["id"],

                            "template": template,

                            "categoria_real": categoria_real,

                            "keywords": categoria_keywords,

                            "tfidf": categoria_tfidf,

                            "llm": categoria_llm,

                        }

                    )

        print()
        print("Experimento concluído.")
