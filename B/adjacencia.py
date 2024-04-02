if __name__ == "__main__":
  N, K = map(int, input().split())

  if K > (N + 1) // 2:
    print("NAO")
  else:
    print("SIM")
