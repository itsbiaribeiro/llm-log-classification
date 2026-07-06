"""
Experimento principal do artigo
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from pathlib import Path

import pandas as pd

from codigo.classificadores.palavras_chave import (
    ClassificadorPalavrasChave,
)

from codigo.classificadores.tfidf import (
    ClassificadorTFIDF,
)

# CONFIGURAÇÕES

USAR_LLM = True

if USAR_LLM:

    from codigo.classificadores.llm import (
        ClassificadorLLM,
    )

# LEITURA DO DATASET

ARQUIVO = Path(
    "resultados/experimentos/empresa_templates_rotulado.csv"
)

df = pd.read_csv(
    ARQUIVO,
    sep=";",
)

df = df.dropna(
    subset=["categoria_real"]
)

print("DATASET")
print()

print(df.head())

print()
print(f"Templates: {len(df)}")


# CLASSIFICADORES

keywords = ClassificadorPalavrasChave()

tfidf = ClassificadorTFIDF(
    df["template"].tolist(),
    df["categoria_real"].tolist(),
)

if USAR_LLM:

    llm = ClassificadorLLM()

# EXECUÇÃO

resultado = []

for _, linha in df.iterrows():

    template = str(
        linha["template"]
    )

    categoria_real = str(
        linha["categoria_real"]
    )

    # Keywords

    categoria_keywords = (
        keywords.classificar(
            template
        ).value
    )

    # TF-IDF

    categoria_tfidf, confianca = (
        tfidf.classificar(
            template
        )
    )

    categoria_tfidf = (
        categoria_tfidf.value
    )

    # LLM

    categoria_llm = ""

    if USAR_LLM:

        categoria_llm, _ = (
            llm.classificar(
                template
            )
        )

        categoria_llm = (
            categoria_llm.value
        )

    resultado.append(

        {

            "template": template,

            "categoria_real": categoria_real,

            "keywords": categoria_keywords,

            "tfidf": categoria_tfidf,

            "llm": categoria_llm,

            "confianca_tfidf": round(
                confianca,
                3,
            ),

        }

    )

resultado = pd.DataFrame(
    resultado
)

# EXPORTAÇÃO

saida = Path(
    "resultados/experimentos/resultado_empresa.csv"
)

resultado.to_csv(
    saida,
    sep=";",
    index=False,
)

print()

print("RESULTADO")

print()

print(resultado)

print()

print(
    f"Arquivo salvo em: {saida}"
)


print()
print("MÉTRICAS")

metodos = [
    "keywords",
    "tfidf",
]

if USAR_LLM:
    metodos.append("llm")

metricas = []

for metodo in metodos:

    acc = accuracy_score(
        resultado["categoria_real"],
        resultado[metodo],
    )

    prec = precision_score(
        resultado["categoria_real"],
        resultado[metodo],
        average="weighted",
        zero_division=0,
    )

    rec = recall_score(
        resultado["categoria_real"],
        resultado[metodo],
        average="weighted",
        zero_division=0,
    )

    f1 = f1_score(
        resultado["categoria_real"],
        resultado[metodo],
        average="weighted",
        zero_division=0,
    )

    print()

    print(metodo.upper())

    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall   : {rec:.4f}")
    print(f"F1-score : {f1:.4f}")

    metricas.append({

        "metodo": metodo,

        "accuracy": acc,

        "precision": prec,

        "recall": rec,

        "f1_score": f1,

    })

metricas = pd.DataFrame(metricas)

metricas.to_csv(

    "resultados/experimentos/metricas_empresa.csv",

    sep=";",

    index=False,

)

print()

print("Arquivo salvo:")

print("resultados/experimentos/metricas_empresa.csv")
