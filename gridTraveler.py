def gridTraveler(m,n, memo):
    if memo is None: memo = {}
    if (m,n) in memo: return memo[(m,n)]
    if m < 1 or n < 1: return 0
    if m == 1 and n ==1: return 1
    memo[(m,n)] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[(m,n)]


if __name__ == '__main__':
    print(gridTraveler(18,18))  #2333606220