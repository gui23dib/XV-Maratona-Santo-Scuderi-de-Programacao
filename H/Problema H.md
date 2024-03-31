# Problema H

## Prêmio no Supermercado

**Nome do arquivo fonte: premio. [c | cpp | java | py]**

Uma dona de casa recentemente ganhou um prêmio para "comprar de graça até que sua cesta de compras não fique cheia" em um supermercado.
Esta dona de casa recebe uma cesta de compras que pode careçar um peso máximo de S quilogramas.
Existem N tipos de itens no supermercado e o I-ésimo item vale V, reais, pesa W.
quilogramas, e há K, volumes (exatamente do mesmo valor e peso) desse item i.
Por exemplo, existem N = 3 tipos de itens: carne, leite e pão; sendo: 1 pacote de came, 3 garrafas de leite e 4 pães.
Quais itens a dona de casa deve levar para maximizar o valor total dos itens em sua cesta de compras?

### Entrada

A primeira linha de entrada contém dois inteiros positivos, S (1 ≤ S≤ 10") e N (1 ≤ N≤ 100).
As próximas N linhas da entrada contêm três inteiros, onde a i-ésima linha contém Vi, (1 ≤ Vi ≤ 10*)
Wi, (1 ≤ W,≤S) e Ki, (1 ≤ K, ≤ 10°), o valor em reais, o peso em quilogramas e número de volumes do i-ésimo item, respectivamente.

### Saída

Seu programa deve imprimir um inteiro, representando o valor total máximo em reais dos itens que esta dona de casa pode levar, garantindo que o peso total não exceda S quilogramas.

### Exemplos

| Entrada                                                  | Saída |
|----------------------------------------------------------|-------|
| 15 5<br> 4 12 1<br> 2 1 1<br> 10 4 1<br> 1 1 1<br> 2 2 1 | 15    |
| 20 3<br> 5000 15 1<br> 100 1 3<br> 50 1 4                | 5400  |
