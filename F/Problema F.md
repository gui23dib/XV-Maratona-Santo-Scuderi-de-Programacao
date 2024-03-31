# Problema F

## Senha Dupla

**Nome do arquivo fonte: senha. [c | cpp |java | py ]**

Um computador dos juízes da Maratona Santo Scuderi de Programação é protegido por uma senha de N dígitos - para fazer login, você normalmente precisa adivinhar exatamente os N dígitos da senha. No entanto, o programador que implementou a verificação de senha deixou um backdoor no computador - há uma segunda senha de N dígitos. Se um usuário inserir uma sequência de N dígitos e, para cada posição de dígito, o dígito inserido corresponder a pelo menos uma das duas senhas nessa mesma posição, essa sequência de N dígitos registrará o usuário no computador.
Dadas as duas senhas, conte o número de sequências distintas de N dígitos que podem ser inseridas para fazer login no computador.

### Entrada

A primeira linha da entrada contém um inteiro N (4 ≤ N ≤ 20), o número de dígitos das senhas. As duas linhas seguintes contém as duas senhas de N dígitos.

### Saída

Seu programa deve produzir um único inteiro, que é o número de sequências distintas de N dígitos que registrarão o usuário no computador dos juízes da Maratona Santo Scuderi de
Programação.

### Exemplos

| Entrada                       | Saída |
|-------------------------------|-------|
| 4<br> 1 1 1 1<br> 1 2 3 4     | 8     |
| 4<br> 2 0 3 4<br> 2 0 3 4     | 1     |
| 5<br> 1 2 3 4 5<br> 5 4 3 2 1 | 16    |
