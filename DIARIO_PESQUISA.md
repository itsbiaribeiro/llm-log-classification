Decisão:

Utilizar HDFS e logs reais.

Justificativa:

Aumentar a validade externa do estudo.

-----------------------------------------
Decisão:

Não utilizar "causa raiz".

Justificativa:

O estudo realiza classificação de categorias de falhas e não reconstrução da cadeia causal.
-----------------------------------------
Anonimizar os logs antes do processamento.

Motivo:

Preservar informações confidenciais.
-----------------------------------------
arquivo empresa:
Descoberta	 -   Impacto
Arquivo com mais de 1,3 milhão de linhas	Necessidade de processamento eficiente

Logs Java estruturados	Facilita extração de atributos

Presença de timestamps	Permite análises temporais

Níveis de severidade	Possibilita caracterização do conjunto

Uso do New Relic	Indica ambiente de produção monitorado