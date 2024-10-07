mod = 10**9 + 7

def matrix(n: int, m: int, default):
    return [[default for _ in range(m)] 
        for _ in range(n)]

def multiply(incidenceMatrix, secondIncidenceMatrix, n):
    resultMatrix = matrix(n,n,0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultMatrix[i][j] = (resultMatrix[i][j] + incidenceMatrix[i][k] * secondIncidenceMatrix[k][j]) % (mod)
    return resultMatrix

def exponentiation(incidenceMatrix, n, k):
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)] 
    while k > 0:
        if k % 2 == 1:
            result = multiply(result, incidenceMatrix, n)
        incidenceMatrix = multiply(incidenceMatrix, incidenceMatrix, n)
        k //= 2

    return result     

def all_path(n: int, k: int, incidenceList: list[int]):
    incidenceMatrix = matrix(n, n, 0)
    for i in incidenceList:
        incidenceMatrix[i[0] - 1][i[1] - 1] += 1

    return sum(exponentiation(incidenceMatrix, n,  k)[0]) % (mod)


meow = list(map(int,input().split(' ')))
tempIncidence = []
for i in range(meow[1]):
    tempIncidence.append(list(map(int, input().split(' '))))
    
print(all_path(meow[0], meow[2], tempIncidence))