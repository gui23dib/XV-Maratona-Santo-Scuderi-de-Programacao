def dfs(grafo, inicio, visitados):
  visitados.add(inicio)

  for n in grafo[inicio]:
    if n not in visitados:
      dfs(grafo, n, visitados)

if __name__ == '__main__':
  grafo_cidades = {i: [] for i in range(1, 5)}

  for _ in range(3):
    a, b = map(int, input().split())
    grafo_cidades[a].append(b)
    grafo_cidades[b].append(a)

  visitados = set()
  dfs(grafo_cidades, 1, visitados)

  if len(visitados) == 4 and all(len(grafo_cidades[i]) <= 2 for i in grafo_cidades):
    print('SIM')
  else:
    print('NAO')

