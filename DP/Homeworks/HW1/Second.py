import math

memo = {

}

def calculate_groups(n: int, k: int):
    if(n <= k):
        return 1
    if(n in memo):
        return memo[n]
    
    first = math.ceil(n/2)
    second = math.floor(n/2)

    result = calculate_groups(first, k) + calculate_groups(second, k)

    memo[n] = result

    return result

what = list(map(int, input().split()))
print(calculate_groups(what[0], what[1]))