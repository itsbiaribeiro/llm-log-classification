from pathlib import Path
import pandas as pd

ENTRADA = Path("resultados/experimentos/empresa_templates.csv")
SAIDA = Path("resultados/experimentos/empresa_templates_falhas.csv")

PALAVRAS_FALHA = [

    "error",
    "exception",
    "fail",
    "failed",
    "fault",
    "timeout",
    "denied",
    "invalid",
    "cannot",
    "unable",
    "not found",
    "does not exist",
    "soap",
    "sql",
    "ora-",
    "nullpointer",
    "illegal",
    "rollback",
    "rollbackexception",
    "unavailable",
    "refused",
    "authentication",

]

df = pd.read_csv(ENTRADA)

mascara = df["template"].str.lower().apply(

    lambda texto: any(

        palavra in texto

        for palavra in PALAVRAS_FALHA

    )

)

falhas = df[mascara]

falhas.to_csv(

    SAIDA,

    index=False,

)

print()
print("TEMPLATES DE FALHA")
print()

print(f"Templates encontrados: {len(falhas)}")

print()

print(falhas.head(30))
