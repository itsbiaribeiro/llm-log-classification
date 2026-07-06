"""
Calcula Accuracy, Precision, Recall e F1-score.
"""

import pandas as pd

from sklearn.metrics import (

    accuracy_score,

    precision_recall_fscore_support,

)


class GeradorMetricas:

    def calcular(

        self,

        arquivo_resultado,

    ):

        df = pd.read_csv(
            arquivo_resultado,
            sep=";",
        )

        metodos = [

            "keywords",

            "tfidf",

            "llm",

        ]

        for metodo in metodos:

            if metodo == "llm":

                if df["llm"].isna().all():

                    continue

            y_true = df["categoria_real"]

            y_pred = df[metodo]

            accuracy = accuracy_score(
                y_true,
                y_pred,
            )

            precision, recall, f1, _ = (
                precision_recall_fscore_support(

                    y_true,

                    y_pred,

                    average="weighted",

                    zero_division=0,

                )
            )

            print()

            print(metodo.upper())

            print(f"Accuracy : {accuracy:.4f}")

            print(f"Precision: {precision:.4f}")

            print(f"Recall   : {recall:.4f}")

            print(f"F1-score : {f1:.4f}")
