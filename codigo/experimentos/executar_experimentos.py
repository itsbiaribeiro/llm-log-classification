"""
Executor dos experimentos.

Executa todos os classificadores sobre um conjunto
de templates previamente minerados.
"""

import csv
from pathlib import Path

from codigo.classificadores.palavras_chave import (
    ClassificadorPalavrasChave,
)

from codigo.classificadores.tfidf import (
    ClassificadorTFIDF,
)

from codigo.classificadores.llm import (
    ClassificadorLLM,
)


class ExecutorExperimentos:

    def __init__(self):

        self.keywords = ClassificadorPalavrasChave()

        self.tfidf = ClassificadorTFIDF()

    def executar(

        self,

        arquivo_entrada: Path,

        arquivo_saida: Path,

        usar_llm=False,

    ):

        llm = None

        if usar_llm:

            llm = ClassificadorLLM()

        with open(

            arquivo_entrada,

            encoding="utf-8",

        ) as entrada:

            leitor = csv.DictReader(entrada)

            with open(

                arquivo_saida,

                "w",

                newline="",

                encoding="utf-8",

            ) as saida:

                campos = [

                    "id",

                    "template",

                    "keywords",

                    "tfidf",

                    "llm",

                ]

                writer = csv.DictWriter(

                    saida,

                    fieldnames=campos,

                )

                writer.writeheader()

                for linha in leitor:

                    template = linha["template"]

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

                            llm

                            .classificar(template)[0]

                            .value

                        )

                    writer.writerow(

                        {

                            "id": linha["id"],

                            "template": template,

                            "keywords": categoria_keywords,

                            "tfidf": categoria_tfidf,

                            "llm": categoria_llm,

                        }

                    )

        print()

        print("Experimento concluído.")
