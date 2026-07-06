"""
Avaliação dos classificadores.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from codigo.dominio.modelos import ResultadoClassificacao


class Avaliador:

    def avaliar(
        self,
        resultados: list[ResultadoClassificacao],
    ) -> dict:

        y_real = [
            r.categoria_real
            for r in resultados
        ]

        y_pred = [
            r.categoria_predita
            for r in resultados
        ]

        metricas = {

            "accuracy": accuracy_score(
                y_real,
                y_pred,
            ),

            "precision": precision_score(
                y_real,
                y_pred,
                average="weighted",
                zero_division=0,
            ),

            "recall": recall_score(
                y_real,
                y_pred,
                average="weighted",
                zero_division=0,
            ),

            "f1_score": f1_score(
                y_real,
                y_pred,
                average="weighted",
                zero_division=0,
            ),
        }

        return metricas
