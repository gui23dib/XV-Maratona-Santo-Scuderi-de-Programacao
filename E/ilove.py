def ilove(palavra: str) -> int:
    vogais = "aeiouAEIOU"

    for i in range(len(palavra)):
        if i % 2 == 0:
          if palavra[i] not in vogais:
            return 0
        else:
          if palavra[i] in vogais:
            return 0
      
    return 1 if len(set(palavra)) == 5 else 0

if __name__ == '__main__':
    palavra = str(input())

    print(ilove(palavra))