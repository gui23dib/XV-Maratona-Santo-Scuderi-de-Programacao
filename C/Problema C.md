# Problema C

## Codificando Matrizes

**Nome do arquivo fonte: adjacencia. [c | cpp | java | py]**

O fazendeiro Jailton Bono (JB) está ensinando números binários às vacas dele e clas aprenderam rapidamente que números binários têm apenas os dígitos 0 e 1. JB ficou muito feliz com os resultados obtidos, e então ele decidiu ensiná-las como criar matrizes binárias quadradas.
Entretanto, as vacas ficaram entediadas depois da segunda aula. JB ficou um pouco triste e pensou, e se eu ensinasse minhas vacas a codificar matrizes binárias com outros símbolos?
JB sabe que suas vacas não são muito inteligentes. Por essa razão ele definiu duas regras simples para codificar matrizes binárias:

1. O bit mais frequente será codificado com o símbolo '*' e o símbolo menos frequente será codificado com o símbolo 'o';
2. No caso de empate, o bit localizado no canto superior esquerdo da matriz será codificado com o '*' e o bit complementar será codificado com o símbolo 'o'.

Aparentemente, as vacas entenderam as regras. Entretanto, JB não tem certeza e quer avaliar a habilidade das vacas. Escreva um programa para codificar uma matriz binária usando as regras propostas por JB.

### Entrada

A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100) representado a dimensão da matriz. As N linhas seguintes contêm N dígitos binários, '0' ou '1' sem espaços.

### Saída

Seu programa deve imprimir a matriz obtida através do mecanismo de codificação proposto por JB.

### Exemplos

| Entrada                                                             | Saída                                                                                  |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 6<br> 111000<br> 001010<br> 110010<br> 001101<br> 001110<br> 111111 | <br> \*\*\*ooo<br> oo\*o\*o<br> \*\*oo\*o<br> oo\*\*o\*<br> oo\*\*\*o<br> \*\*\*\*\*\* |
| 2<br> 00<br> 11                                                     | <br> \*\*<br> oo                                                                       |
