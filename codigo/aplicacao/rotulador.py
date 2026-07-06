"""
Rotulagem dos logs.
"""


class Rotulador:
    """
    Classe base para rotulagem.
    """

    def rotular(self, mensagem: str):
        raise NotImplementedError(
            "Rotulador ainda não implementado."
        )
