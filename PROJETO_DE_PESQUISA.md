# PROJETO_DE_PESQUISA.md

# Título Provisório

Avaliação Experimental de Large Language Models para Classificação Automática de Categorias de Falhas em Logs de Sistemas Distribuídos

---

# Problema de Pesquisa

A análise de logs é uma das principais atividades no processo de manutenção de sistemas distribuídos. Entretanto, a crescente quantidade de registros gerados por aplicações modernas dificulta sua inspeção manual.

Métodos tradicionais baseados em regras ou similaridade textual apresentam limitações quando confrontados com mensagens heterogêneas e não estruturadas.

Recentemente, Large Language Models (LLMs) passaram a ser utilizados em diferentes tarefas relacionadas à Engenharia de Software, porém ainda existem poucos estudos que avaliam seu desempenho especificamente na classificação automática de categorias de falhas em logs utilizando simultaneamente conjuntos de dados públicos e logs reais de produção.

---

# Hipótese

LLMs apresentam desempenho superior aos métodos tradicionais na classificação automática de categorias de falhas, especialmente em cenários contendo mensagens de log heterogêneas.

---

# Objetivo Geral

Avaliar experimentalmente o desempenho de Large Language Models na classificação automática de categorias de falhas em logs de sistemas distribuídos.

---

# Objetivos Específicos

* Caracterizar os conjuntos de dados.
* Anonimizar os logs industriais.
* Construir um pipeline reproduzível.
* Implementar métodos tradicionais.
* Implementar abordagens baseadas em LLMs.
* Comparar os métodos experimentalmente.
* Analisar quantitativamente e qualitativamente os resultados.

---

# Contribuições Esperadas

C1 — Pipeline experimental reproduzível para classificação de logs.

C2 — Comparação entre métodos tradicionais e LLMs.

C3 — Avaliação em datasets públicos e industriais.

C4 — Processo estruturado de caracterização, anonimização e preparação de logs para experimentos.

---

# Perguntas de Pesquisa

RQ1

Qual é o desempenho de LLMs na classificação automática de categorias de falhas?

RQ2

Como os LLMs se comparam aos métodos tradicionais?

RQ3

Os resultados obtidos em HDFS permanecem consistentes quando avaliados em logs reais?

RQ4 (Candidata)

Quais características dos logs influenciam o desempenho dos diferentes métodos?

---

# Artigos-base

1. LLM-Based Automated Diagnosis of Integration Test Failures at Google

2. LogExpert: Log-based Recommended Resolutions Generation using Large Language Models

3. Order Matters: An Empirical Study on Large Language Models

4. Mining Historical Test Logs to Predict Bugs and Localize Faults

---

# Datasets

Dataset Público

* HDFS

Dataset Empresariais

* Logs reais (.log e .out)

---

# Baselines

* Palavras-chave
* TF-IDF

---

# Métodos Avaliados

* LLM Zero-Shot
* LLM Few-Shot

---

# Métricas

* Acurácia
* Precisão
* Revocação
* F1-score

---

# Critérios de Qualidade

* Código documentado.
* Reprodutibilidade.
* Modularização.
* Experimentos automatizados.
* Resultados reproduzíveis.
* Rastreabilidade entre código e artigo.
