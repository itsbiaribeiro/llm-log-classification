"""
Geração de figuras.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import confusion_matrix

# CAMINHOS

PASTA_EXPERIMENTOS = Path(
    "resultados/experimentos"
)

PASTA_FIGURAS = Path(
    "resultados/figuras"
)

PASTA_FIGURAS.mkdir(
    parents=True,
    exist_ok=True,
)

ARQUIVO_METRICAS = (
    PASTA_EXPERIMENTOS
    / "metricas_empresa.csv"
)

ARQUIVO_RESULTADO = (
    PASTA_EXPERIMENTOS
    / "resultado_empresa.csv"
)

ARQUIVO_TEMPLATES = (
    PASTA_EXPERIMENTOS
    / "empresa_templates_rotulado.csv"
)

metricas = pd.read_csv(
    ARQUIVO_METRICAS,
    sep=";",
)

resultado = pd.read_csv(
    ARQUIVO_RESULTADO,
    sep=";",
)

templates = pd.read_csv(
    ARQUIVO_TEMPLATES,
    sep=";",
)

print("Arquivos carregados com sucesso.")

# COMPARAÇÃO DA ACCURACY

plt.figure(figsize=(7, 5))

plt.bar(

    metricas["metodo"],

    metricas["accuracy"],

)

plt.title(
    "Accuracy dos Classificadores"
)

plt.xlabel("Método")

plt.ylabel("Accuracy")

plt.ylim(0, 1.05)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(

    PASTA_FIGURAS /

    "comparacao_accuracy.png",

    dpi=300,

)

plt.close()

print("Figura gerada.")

# COMPARAÇÃO DAS MÉTRICAS

metricas_plot = metricas.set_index(
    "metodo"
)

metricas_plot = metricas_plot[

    [

        "accuracy",

        "precision",

        "recall",

        "f1_score",

    ]

]

plt.figure(figsize=(9, 5))

metricas_plot.plot(

    kind="bar",

)

plt.title(
    "Comparação entre os Classificadores"
)

plt.xlabel("Método")

plt.ylabel("Valor")

plt.ylim(0, 1.05)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(

    PASTA_FIGURAS /

    "comparacao_metricas.png",

    dpi=300,

)

plt.close()

print("Figura gerada.")

# DISTRIBUIÇÃO DAS CATEGORIAS

plt.figure(figsize=(8, 5))

contagem = (
    templates["categoria_real"]
    .value_counts()
    .sort_values(ascending=False)
)

plt.bar(
    contagem.index,
    contagem.values,
)

plt.title(
    "Distribuição das Categorias de Falha"
)

plt.xlabel("Categoria")

plt.ylabel("Quantidade de Templates")

plt.xticks(rotation=20, ha="right")

for indice, valor in enumerate(contagem.values):

    plt.text(
        indice,
        valor + 0.05,
        str(valor),
        ha="center",
    )

plt.tight_layout()

plt.savefig(
    PASTA_FIGURAS /
    "distribuicao_categorias.png",
    dpi=300,
)

plt.close()

print("Figura gerada.")

# MATRIZ DE CONFUSÃO

if "llm" in resultado.columns:

    categorias = sorted(
        resultado["categoria_real"].unique()
    )

    matriz = confusion_matrix(

        resultado["categoria_real"],

        resultado["llm"],

        labels=categorias,

    )

    plt.figure(figsize=(8, 6))

    plt.imshow(matriz)

    plt.title(
        "Matriz de Confusão - LLM"
    )

    plt.colorbar()

    plt.xticks(
        range(len(categorias)),
        categorias,
        rotation=45,
        ha="right",
    )

    plt.yticks(
        range(len(categorias)),
        categorias,
    )

    plt.xlabel(
        "Categoria Predita"
    )

    plt.ylabel(
        "Categoria Real"
    )

    for i in range(len(categorias)):

        for j in range(len(categorias)):

            plt.text(

                j,

                i,

                matriz[i, j],

                ha="center",

                va="center",

            )

    plt.tight_layout()

    plt.savefig(

        PASTA_FIGURAS /

        "matriz_confusao_llm.png",

        dpi=300,

    )

    plt.close()

    print("Figura gerada.")
