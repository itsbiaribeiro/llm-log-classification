"""
Classificador baseado em TF-IDF.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from codigo.dominio.categorias import CategoriaFalha


class ClassificadorTFIDF:

    def __init__(
        self,
        textos_treinamento,
        categorias_treinamento,
    ):

        self.vectorizer = TfidfVectorizer()

        self.textos = [
            str(texto).lower()
            for texto in textos_treinamento
        ]

        self.categorias = []

        for categoria in categorias_treinamento:

            if isinstance(
                categoria,
                CategoriaFalha,
            ):
                self.categorias.append(categoria)

            else:
                self.categorias.append(
                    CategoriaFalha(categoria)
                )

        self.matriz = self.vectorizer.fit_transform(
            self.textos
        )

    def classificar(
        self,
        texto,
    ):

        texto = texto.lower()

        vetor = self.vectorizer.transform(
            [texto]
        )

        similaridades = cosine_similarity(
            vetor,
            self.matriz,
        )[0]

        # Evita recuperar o próprio template
        for i, texto_base in enumerate(self.textos):

            if texto.strip().lower() == texto_base.strip().lower():

                similaridades[i] = -1

        indice = similaridades.argmax()

        confianca = float(
            similaridades[indice]
        )

        if confianca < 0.20:

            return (
                CategoriaFalha.UNKNOWN,
                confianca,
            )

        return (
            self.categorias[indice],
            confianca,
        )


if __name__ == "__main__":

    print(
        "O TF-IDF deve ser utilizado pelo avaliar.py"
    )
