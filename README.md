# Análise de Finanças e Lógica

Este repositório contém um caso dividido em três partes, envolvendo manipulação de dados financeiros, uma análise de regressão logística e um exercício de lógica relacionado ao xadrez.

## Parte 1: Debêntures Positivo

Na primeira parte, manipulamos a base de dados "CasePositivo" contendo informações das debêntures da Positivo (POSI12 e POSI13). As etapas incluem:

- Acrescentar uma coluna com o valor de mercado total diário de cada debênture na curva.
- Eliminar a coluna da taxa de compra.
- Concatenar o preço dos ativos POSI12 e POSI13 de acordo com a data.
- Utilizar a taxa indicativa de cada debênture para adicionar uma coluna com o valor presente diário de um pagamento fictício de R$ 100 milhões daqui a 3 anos.
- Montar um gráfico com o preço unitário indicativo e taxa indicativa diária.

## Parte 2: Regressão Logística NTN-B 35 e IFIX

Na segunda parte, realizamos uma análise de regressão logística em Python para entender como a variação da taxa da NTN-B 2035 explica o Dividend Yield do IFIX.

## Parte 3: Lógica - Xadrez

A terceira parte envolve um exercício de lógica relacionado ao xadrez. Inclui a implementação de uma função `marque_atacadas(tab)` que marca as regiões atacadas com um X em um tabuleiro de xadrez. Além disso, um programa é fornecido para imprimir o tabuleiro com a posição inicial das rainhas e, em seguida, com as posições atacadas.
