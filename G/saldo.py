if __name__ == '__main__':
  N = int(input())

  soma_total: int = 0
  saldo_inicial: int = 0

  for i in range(N):
    soma_total += int(input())
    if(soma_total < 0):
      saldo_inicial += abs(soma_total)
      soma_total = 0

  print(saldo_inicial)
