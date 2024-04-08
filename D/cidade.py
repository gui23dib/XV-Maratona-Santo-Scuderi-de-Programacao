if __name__ == '__main__':
  N = int(input())
  values = sorted(list(map(int, input().split())))

  custo_total: int = 0
  for i in range(1, N):
    custo_total += abs(values[i] - values[i-1])

  print(custo_total)