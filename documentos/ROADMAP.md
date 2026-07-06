# ROADMAP_PESQUISA.md

# FASE 0 — Fundamentação Científica

## Objetivo

Construir a base teórica do projeto e identificar as lacunas da literatura que justificam a pesquisa.

---

## Artigos-base

☐ Artigo 1 — LLM-Based Automated Diagnosis of Integration Test Failures at Google

Objetivo da leitura

* Compreender como os autores utilizam LLMs para diagnóstico.
* Identificar metodologia experimental.
* Identificar métricas utilizadas.
* Identificar ameaças à validade.

---

☐ Artigo 2 — LogExpert

Objetivo da leitura

* Compreender a utilização de LLMs na análise de logs.
* Identificar o pipeline proposto.
* Identificar limitações.

---

☐ Artigo 3 — Order Matters

Objetivo da leitura

* Compreender estratégias de prompting.
* Definir Zero-Shot e Few-Shot do projeto.

---

## Produtos Esperados

✓ Fundamentação Teórica

✓ Trabalhos Relacionados

✓ Justificativa da metodologia

✓ Definição dos experimentos

✓ Seleção das métricas

✓ Identificação da lacuna de pesquisa

# Projeto

**Avaliação Experimental de Large Language Models para Classificação Automática de Categorias de Falhas em Logs de Sistemas Distribuídos**

---

# Objetivo Geral

Desenvolver um pipeline experimental reproduzível para avaliar o desempenho de Large Language Models na classificação automática de categorias de falhas em logs de sistemas distribuídos, comparando-os com métodos tradicionais em conjuntos de dados públicos e industriais.

---

# Perguntas de Pesquisa

## RQ1

Large Language Models são capazes de classificar automaticamente categorias de falhas em logs de produção?

Status: OK

---

## RQ2

Como o desempenho dos Large Language Models se compara às abordagens tradicionais baseadas em palavras-chave e TF-IDF?

Status: OK

---

## RQ3

Quais são as principais vantagens e limitações da utilização de Large Language Models na classificação automática de logs de sistemas distribuídos?

Status: OK

---

# FASE 1 — Planejamento

* [x] Definir tema
* [x] Definir objetivo
* [x] Definir perguntas de pesquisa
* [x] Definir arquitetura
* [x] Finalizar roadmap

---

# FASE 2 — Caracterização dos Dados

Objetivo

Caracterizar automaticamente os conjuntos de dados.

Entradas

* Logs reais (.log/.out)
* HDFS

Artefatos esperados

* Estatísticas gerais
* CSV
* JSON
* Figuras
* Tabela do artigo

---

# FASE 3 — Anonimização

Objetivo

Anonimizar os logs industriais preservando informações relevantes para classificação.

Artefatos

* Logs anonimizados
* Relatório de anonimização
* Seção correspondente do artigo


---

# FASE 4 — Pré-processamento

Objetivo

Padronizar os logs para os experimentos.

Artefatos

* Dados processados
* Estatísticas
* Figura do pipeline

---

# FASE 5 — Construção da Taxonomia

Objetivo

Definir as categorias de falhas utilizadas na classificação.

Artefatos

* Documento da taxonomia
* Exemplos por categoria
* Critérios de rotulagem

---

# FASE 6 — Rotulagem

Objetivo

Construir o conjunto de avaliação.

Artefatos

* Dataset rotulado
* Guia de rotulagem


---

# FASE 7 — Implementação dos Métodos

## Baseline 1

Palavras-chave

☐

## Baseline 2

TF-IDF

☐

## Método 3

LLM Zero-Shot

☐

## Método 4

LLM Few-Shot

☐

---

# FASE 8 — Avaliação Experimental

Objetivo

Executar todos os experimentos.

Métricas

* Acurácia
* Precisão
* Revocação
* F1-score

Artefatos

* Tabelas
* Matrizes de confusão
* Gráficos

Status

☐

---

# FASE 9 — Discussão

Objetivo

Interpretar os resultados.

Análises previstas

* Comparação entre métodos
* Comparação entre HDFS e logs reais
* Análise de erros
* Limitações

Status

☐

---

# FASE 10 — Artigo

Seções

☐ Resumo

☐ Introdução

☐ Fundamentação Teórica

☐ Trabalhos Relacionados

☐ Metodologia

☐ Implementação

☐ Resultados

☐ Discussão

☐ Ameaças à Validade

☐ Conclusão

☐ Referências

☐ Revisão bibliográfica final

---

# Critério de Conclusão

Um módulo será considerado concluído somente quando possuir:

✓ Código implementado

✓ Testes executados

✓ Artefatos gerados

✓ Texto correspondente no artigo

✓ Documentação atualizada
