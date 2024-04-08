if __name__ == '__main__':
  N = int(input())
  senha1 = list(map(int, input().split()))
  senha2 = list(map(int, input().split()))

  sequencias_possiveis = set()

  for i in range(2 ** N):
    sequencia = []
    for j in range(N):
      #print(i, j, format(i, "b"), format(j, "b"), (i >> j) & 1)
      if (i >> j) & 1:
        sequencia.append(senha1[j])
      else:
        sequencia.append(senha2[j])
      
    sequencias_possiveis.add(tuple(sequencia))

  print(len(sequencias_possiveis))
