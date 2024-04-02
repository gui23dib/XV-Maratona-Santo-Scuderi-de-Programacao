def codificando(bincode_matriz: list) -> str:
  caracteres_count = {'0': 0, '1': 0}
    
  for linha in bincode_matriz:
    for bit in linha:
      caracteres_count[bit] += 1

  caractere_mais_frequente = '*' if caracteres_count['0'] < caracteres_count['1'] else 'o'
  caractere_menos_frequente = '*' if caractere_mais_frequente == 'o' else 'o'

  if caracteres_count['0'] == caracteres_count['1']:
    caractere_mais_frequente = 'o' if bincode_matriz[0][0] == '0' else '*' 
    caractere_menos_frequente = '*' if bincode_matriz[0][0] == '0' else 'o'
  
  for i in range(len(bincode_matriz)):
    for j in range(len(bincode_matriz)):
      if bincode_matriz[i][j] == '0': bincode_matriz[i][j] = caractere_menos_frequente
      else: bincode_matriz[i][j] = caractere_mais_frequente

  return bincode_matriz


if __name__ == "__main__":
  N = int(input())

  matriz_binaria = []
  for i in range(N):
    matriz_binaria.append(list(str(input())))

  for resultado in codificando(matriz_binaria):
    print(*resultado, sep='')