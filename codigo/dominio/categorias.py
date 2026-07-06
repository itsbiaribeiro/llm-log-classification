"""
Categorias unificadas de falhas utilizadas
nos experimentos do projeto.

A taxonomia foi definida para permitir a
comparação entre diferentes domínios de logs.
"""

from enum import Enum


class CategoriaFalha(Enum):
    """
    Taxonomia unificada de causas de falha.
    """

    INFRASTRUCTURE_ERROR = "Infrastructure Error"

    CONFIGURATION_ERROR = "Configuration Error"

    DATA_ERROR = "Data Error"

    BUSINESS_RULE_ERROR = "Business Rule Error"

    SECURITY_ERROR = "Security Error"

    UNKNOWN = "Unknown"
