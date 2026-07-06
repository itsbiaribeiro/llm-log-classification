from codigo.avaliacao.avaliador import Avaliador
from codigo.dominio.modelos import ResultadoClassificacao

dados = [

    ResultadoClassificacao(
        texto="connection refused",
        categoria_real="Network Failure",
        categoria_predita="Network Failure",
        metodo="Palavras-chave",
    ),

    ResultadoClassificacao(
        texto="permission denied",
        categoria_real="Permission Error",
        categoria_predita="Permission Error",
        metodo="Palavras-chave",
    ),

    ResultadoClassificacao(
        texto="disk error",
        categoria_real="Disk Failure",
        categoria_predita="Unknown",
        metodo="Palavras-chave",
    ),
]

avaliador = Avaliador()

metricas = avaliador.avaliar(dados)

print()

print("===== MÉTRICAS =====")

for chave, valor in metricas.items():

    print(f"{chave:12}: {valor:.4f}")
