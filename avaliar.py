from pathlib import Path

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)

from sklearn.model_selection import (
    train_test_split,
)

from codigo.classificadores.palavras_chave import (
    ClassificadorPalavrasChave,
)

from codigo.classificadores.tfidf import (
    ClassificadorTFIDF,
)

# ================================================
# CONFIGURAÇÃO
# ================================================

USAR_LLM = False

if USAR_LLM:

    from codigo.classificadores.llm import (
        ClassificadorLLM,
    )

# ================================================
# LEITURA
# ================================================

arquivo = Path(
    "resultados/experimentos/hdfs_templates_rotulado.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
)

df = df.dropna(
    subset=["categoria_real"]
)

# ================================================
# DIVISÃO TREINO / TESTE
# ================================================

treino, teste = train_test_split(

    df,

    test_size=0.20,

    random_state=42,

    shuffle=True,

)

# ================================================
# CLASSIFICADORES
# ================================================

keywords = ClassificadorPalavrasChave()

tfidf = ClassificadorTFIDF(

    treino["template"],

    treino["categoria_real"],

)

if USAR_LLM:

    llm = ClassificadorLLM()

# ================================================
# EXECUÇÃO
# ================================================

resultado = []

for _, linha in teste.iterrows():

    texto = linha["template"]

    categoria_real = linha["categoria_real"]

    categoria_keywords = (

        keywords.classificar(
            texto
        ).value

    )

    categoria_tfidf = (

        tfidf.classificar(
            texto
        )[0].value

    )

    categoria_llm = ""

    if USAR_LLM:

        categoria_llm = (

            llm.classificar(
                texto
            )[0].value

        )

    resultado.append(

        {

            "template": texto,

            "categoria_real": categoria_real,

            "keywords": categoria_keywords,

            "tfidf": categoria_tfidf,

            "llm": categoria_llm,

        }

    )

resultado = pd.DataFrame(resultado)

# ================================================
# SALVA RESULTADO
# ================================================

saida = Path(
    "resultados/experimentos/resultado_experimento.csv"
)

resultado.to_csv(

    saida,

    sep=";",

    index=False,

)

print()

print("Resultado salvo em:")

print(saida)

print()

# ================================================
# MÉTRICAS
# ================================================

for metodo in [

    "keywords",

    "tfidf",

] + (

    ["llm"]

    if USAR_LLM

    else []

):

    y_true = resultado["categoria_real"]

    y_pred = resultado[metodo]

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

    print(metodo.upper())

    print(f"Accuracy : {accuracy:.4f}")

    print(f"Precision: {precision:.4f}")

    print(f"Recall   : {recall:.4f}")

    print(f"F1-score : {f1:.4f}")

    print()
