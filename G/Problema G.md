# Problema G

## Saldo Inicial

**Nome do arquivo fonte: saldo. [c | cpp | java | py]**

Os bancos geralmente cobram taxas de saque a descoberto se você tentar sacar mais dinheiro
de sua conta do que o disponível em seu saldo atual.
Dada uma sequência de depósitos e saques (e supondo que cada depósito e saque seja refletido imediatamente em seu saldo), determine o saldo inicial mínimo (não negativo) necessário para garantir que não serão cobradas taxas de saque a descoberto ao longo da sequência.

### Entrada

A primeira linha de entrada contém um único inteiro N (1 ≤ N ≤ 1.000), que é o número de transações. Cada uma das próximas N linhas contém um único inteiro T (-10° ≤ T ≤ 10°, T != 0). Estas são as transações, na ordem em que ocorrem. Um número positivo representa um depósito, um número negativo representa um saque. Não ocorrem duas transações simultaneamente.

### Saída

Seu programa deve produzir um único número inteiro não negativo, que é o saldo mínimo não negativo com o qual você deve começar em sua conta para evitar quaisquer taxas de saque a descoberto.

### Exemplos

| Entrada                                                 | Saída |
|---------------------------------------------------------|-------|
| 3<br> 3<br> -5<br> 3                                    | 2     |
| 5<br> 8<br> -7<br> 2<br> -3<br> 1                       | 0     |
| 8<br> -5<br> 10<br> -6<br> -2<br> 1<br> -4<br> 3<br> -3 | 6     |
