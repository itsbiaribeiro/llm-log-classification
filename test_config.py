from config import DADOS_EMPRESA
from codigo.infraestrutura.arquivos import listar_arquivos_log

arquivos = listar_arquivos_log(DADOS_EMPRESA)

print("Arquivos encontrados:")

for arquivo in arquivos:
    print(arquivo.name)
