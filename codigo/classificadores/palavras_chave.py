"""
Classificador baseado em palavras-chave.
"""

from codigo.dominio.categorias import CategoriaFalha


class ClassificadorPalavrasChave:

    def __init__(self):

        self.regras = {

            CategoriaFalha.INFRASTRUCTURE_ERROR: [

                "timeout",
                "rollback",
                "rolled back",
                "transaction",
                "connection refused",
                "connection reset",
                "socket",
                "host unreachable",
                "network",
                "resource",
                "heap",
                "memory",
                "outofmemory",
                "disk",
                "checksum",

            ],

            CategoriaFalha.CONFIGURATION_ERROR: [

                "xml",
                "configuration",
                "config",
                "file",
                "does not exist",
                "not found",
                "invalid configuration",

            ],

            CategoriaFalha.DATA_ERROR: [

                "ora-",
                "sql",
                "constraint",
                "serialization",
                "deserialize",
                "parse",
                "listvaluesnotfound",
                "listvaluesnotfoundexception",

            ],

            CategoriaFalha.BUSINESS_RULE_ERROR: [

                "workflow",
                "treateventwitherrors",
                "passescondition",
                "validation",
                "business",
                "rule",

            ],

            CategoriaFalha.SECURITY_ERROR: [

                "permission denied",
                "access denied",
                "authentication",
                "unauthorized",
                "forbidden",

            ],
        }

    def classificar(
        self,
        texto: str,
    ) -> CategoriaFalha:

        texto = texto.lower()

        for categoria, palavras in self.regras.items():

            for palavra in palavras:

                if palavra in texto:

                    return categoria

        return CategoriaFalha.UNKNOWN


if __name__ == "__main__":

    classificador = ClassificadorPalavrasChave()

    exemplos = [

        "error loading xml",

        "file does not exist",

        "workflow validation failed",

        "permission denied",

        "rollback transaction",

        "ORA-00001",

        "mensagem desconhecida",

    ]

    for exemplo in exemplos:

        categoria = classificador.classificar(exemplo)

        print(exemplo)

        print(" -> ", categoria.value)

        print()
