#Verificador de Qualidade de Dados

##Descrição:

O projeto consiste em um pipeline em Python voltado para validação e governança de dados. Ele permite ler dados de diferentes fontes (CSV, API ou banco de dados), aplicar regras de qualidade, gerar relatórios de inconsistências e garantir que seus dados estejam confiáveis para análise ou carregamento em sistemas.

Este projeto funciona como um mini framework de qualidade de dados, ideal para automatizar validações e acompanhar a saúde dos dados.

##Funcionalidades:

Extrair: lê dados de arquivos CSV, APIs ou bancos de dados.

Transformar: padroniza valores, valida campos obrigatórios, formatos e ranges.

Carregar: salva os dados validados em um DataFrame confiável ou em um SQLite.

Dicionarização de regras: permite definir regras de validação de forma centralizada em Python.

Relatório de qualidade: fornece estatísticas sobre erros, duplicidades e inconsistências.
