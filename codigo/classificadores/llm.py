"""
Classificador baseado em Large Language Models (LLMs).

Utiliza a API da OpenAI para classificar templates
de logs utilizando a taxonomia unificada do projeto.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from codigo.dominio.categorias import CategoriaFalha

load_dotenv()


class ClassificadorLLM:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def classificar(
        self,
        texto: str,
    ) -> tuple[CategoriaFalha, float]:

        prompt = f"""
Você é especialista em Engenharia de Software.

Classifique o template abaixo em apenas UMA categoria.

Categorias possíveis:

- Infrastructure Error
- Configuration Error
- Data Error
- Business Rule Error
- Security Error
- Unknown

Responda SOMENTE com o nome da categoria.

Template:

{texto}
"""

        resposta = self.client.chat.completions.create(

            model="gpt-5-mini",

            messages=[

                {
                    "role": "system",
                    "content": (
                        "Você é especialista em análise de logs "
                        "e classificação de falhas."
                    ),
                },

                {
                    "role": "user",
                    "content": prompt,
                },

            ],

        )

        categoria = (
            resposta.choices[0]
            .message.content.strip()
        )

        print("Resposta:", categoria)

        mapa = {

            "Infrastructure Error":
                CategoriaFalha.INFRASTRUCTURE_ERROR,

            "Configuration Error":
                CategoriaFalha.CONFIGURATION_ERROR,

            "Data Error":
                CategoriaFalha.DATA_ERROR,

            "Business Rule Error":
                CategoriaFalha.BUSINESS_RULE_ERROR,

            "Security Error":
                CategoriaFalha.SECURITY_ERROR,

            "Unknown":
                CategoriaFalha.UNKNOWN,

        }

        categoria = mapa.get(

            categoria,

            CategoriaFalha.UNKNOWN,

        )

        return categoria, 1.0


if __name__ == "__main__":

    llm = ClassificadorLLM()

    categoria, confianca = llm.classificar(

        "error loading xml configuration"

    )

    print()

    print(categoria.value)

    print(confianca)
