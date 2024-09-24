from math import inf

def permute(nums: list[int], m: int):
    if m == 0:
        return [[]]
    
    result = []
    for i in range(len(nums)):
        num = nums[i]
        remaining = nums[:i] + nums[i+1:]
        for perm in permute(remaining, m - 1):
            result.append([num] + perm)
    
    return result
        

def charging(n: int, m: int, values: list[int]) -> int:
    if(m == n):
        print(0)
        values.sort()
        print(" ".join(map(str, values)))
        return

    result = inf
    lisssst = permute(values, m)
    for item in lisssst:
        minDistanceMultiple = 0
        for i in range(len(values)):
            minDistanceSingle = inf
            for j in range(len(item)):
               minDistanceSingle = min(minDistanceSingle, abs(item[j] - values[i]))
            minDistanceMultiple += minDistanceSingle
        result = min(result, minDistanceMultiple)
    print(result)

firstRow = list(map(int, input().split(' ')))
secondRow = list(map(int, input().split(' ')))

charging(firstRow[0], firstRow[1], secondRow)