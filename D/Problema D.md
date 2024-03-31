# Problema D

## Pavimentando a Cidade

**Nome do arquivo fonte: cidade. [c | cpp | java | py]**

Uma nova cidade foi fundada! A cidade tem N casas, mas nenhuma estrada ainda. O prefeito da cidade contratou uma empreiteira para construir estradas entre as casas, de tal forma que uma pessoa pode ir de qualquer casa a outra por uma caminho de estradas pavimentadas. O custo de pavimentar uma estrada é calculado dependendo do valor A de cada casa. O custo para pavimentar uma estrada entre a casa i e a casa j é o valor absoluto da diferença entre seus valores: (4-4,). O prefeito precisa minimizar o custo total de pavimentação das estradas.

### Entrada

A primeira linha da entrada é composta por um inteiro N (1 ≤ N ≤ 10), representando o número de casas da cidade. A linha seguinte contém N inteiros A, (1 ≤ A, ≤ 10°, para 1 ≤ i ≤ N), OS valores de cada casa.

### Saída

Seu programa deve imprimir uma única linha contendo o custo mínimo total para conectar as casas da cidade.

### Exemplos

| Entrada                    | Saída |
|----------------------------|-------|
| 2<br> 1 1                  | 0     |
| 5<br> 10 10 9 2 3          | 8     |
| 9<br> 8 12 4 10 11 1 2 5 5 | 11    |
