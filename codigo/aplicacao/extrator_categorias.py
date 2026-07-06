"""
Transformar templates em categorias de falhas.
"""

from codigo.dominio.categorias import CategoriaFalha
from codigo.dominio.modelos import (
    CategoriaLog,
    TemplateLog,
)


class ExtratorCategorias:

    def extrair(
        self,
        templates: list[TemplateLog],
    ) -> list[CategoriaLog]:

        categorias = []

        for template in templates:

            categoria = self.identificar_categoria(
                template.texto
            )

            categorias.append(

                CategoriaLog(
                    template=template,
                    categoria=categoria,
                )

            )

        return categorias

    def identificar_categoria(
        self,
        texto: str,
    ) -> CategoriaFalha:

        texto = texto.lower()

        # Falhas de rede

        if any(

            palavra in texto

            for palavra in [

                "connection refused",

                "connection reset",

                "socket",

                "network",

                "host unreachable",

                "timeout",

            ]

        ):

            return CategoriaFalha.NETWORK_FAILURE

        # Permissão

        if any(

            palavra in texto

            for palavra in [

                "permission denied",

                "access denied",

                "unauthorized",

                "authentication",

            ]

        ):

            return CategoriaFalha.PERMISSION_ERROR

        # Disco

        if any(

            palavra in texto

            for palavra in [

                "disk",

                "checksum",

                "corrupt",

                "bad block",

            ]

        ):

            return CategoriaFalha.DISK_FAILURE

        # Recursos

        if any(

            palavra in texto

            for palavra in [

                "outofmemory",

                "memory",

                "heap",

                "gc overhead",

            ]

        ):

            return CategoriaFalha.RESOURCE_EXHAUSTION

        # Dados

        if any(

            palavra in texto

            for palavra in [

                "parse",

                "serialization",

                "deserialize",

                "invalid",

                "malformed",

            ]

        ):

            return CategoriaFalha.DATA_CORRUPTION

        return CategoriaFalha.UNKNOWN
