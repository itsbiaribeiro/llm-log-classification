# Arquitetura do Projeto

## 1. Visão Geral

Este projeto tem como objetivo investigar o uso de Large Language Models (LLMs) para a classificação automática de categorias de falhas em logs de sistemas distribuídos.

A pesquisa possui caráter experimental e compara abordagens tradicionais de classificação textual com modelos baseados em LLMs utilizando dois conjuntos de dados distintos: um dataset público (HDFS) e logs reais de produção previamente anonimizados.

O projeto foi desenvolvido seguindo princípios de Engenharia de Software Experimental, buscando garantir reprodutibilidade, organização e rastreabilidade entre implementação, experimentos e artigo científico.

---

# 2. Objetivos

## Objetivo Geral

Avaliar a eficácia de Large Language Models na classificação automática de categorias de falhas presentes em logs de sistemas distribuídos.

## Objetivos Específicos

* Caracterizar automaticamente os conjuntos de dados utilizados.
* Anonimizar logs industriais preservando informações relevantes para classificação.
* Construir um pipeline reproduzível de pré-processamento.
* Comparar LLMs com métodos tradicionais.
* Avaliar quantitativamente e qualitativamente os resultados.

---

# 3. Perguntas de Pesquisa

RQ1. Large Language Models são capazes de classificar automaticamente categorias de falhas em logs de produção?
RQ2. Como o desempenho dos Large Language Models se compara às abordagens tradicionais baseadas em palavras-chave e TF-IDF?
RQ3. Quais são as principais vantagens e limitações da utilização de Large Language Models na classificação automática de logs de sistemas distribuídos?


---

# 4. Pipeline Experimental

Conjuntos de Dados

↓

Caracterização

↓

Anonimização (somente logs empresariais)

↓

Pré-processamento

↓

Construção das Categorias

↓

Rotulagem

↓

Classificação

↓

Avaliação

↓

Discussão dos Resultados

---

# 5. Conjuntos de Dados

## Dataset Público

* HDFS Log Dataset

## Dataset Empresarial

* Arquivos .log e .out provenientes de ambiente real de produção
* Dados anonimizados antes do processamento

---

# 6. Métodos Avaliados

* Baseline por palavras-chave
* TF-IDF
* LLM Zero-Shot
* LLM Few-Shot

---

# 7. Métricas

* Acurácia
* Precisão
* Revocação
* F1-score

---

# 8. Linguagem

Todo o código, documentação e artigo serão desenvolvidos em português.

---

# 9. Princípios do Projeto

* Código limpo
* Reprodutibilidade
* Modularização
* Rastreabilidade entre código e artigo
* Separação clara entre dados brutos, dados processados e resultados
