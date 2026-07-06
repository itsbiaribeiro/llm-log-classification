from codigo.classificadores.tfidf import ClassificadorTFIDF

classificador = ClassificadorTFIDF()

exemplos = [

    "connection refused",

    "socket timeout",

    "permission denied",

    "disk checksum error",

    "java heap space",

    "serialization error",

    "mensagem desconhecida",

]

for texto in exemplos:

    categoria, confianca = classificador.classificar(texto)

    print(f"{texto}")

    print(f"Categoria : {categoria.value}")

    print(f"Similaridade : {confianca:.3f}")

    print("-" * 50)
