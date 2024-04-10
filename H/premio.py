if __name__ == 'main':
  S, N = map(int, input().split())

  items = []
  for _ in range(N):
    V, W, K = map(int, input().split())
    items.append((V, W, K))

  cesta = [[0] * (S + 1) for _ in range(N + 1)]

  for i in range(1, N + 1):
    for j in range(1, S + 1):
      Vi, Wi, Ki = items[i - 1]
      if Wi <= j:

        for k in range(min(Ki, j // Wi) + 1):
          cesta[i][j] = max(cesta[i][j], cesta[i - 1][j - k * Wi] + k * Vi)

      cesta[i][j] = max(cesta[i][j], cesta[i - 1][j])

  print(cesta[N][S])