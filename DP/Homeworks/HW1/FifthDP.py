from math import inf, ceil

dp = []

def charging(n: int, m: int, values: list[int]) -> int:
    if(m == n):
        values.sort()
        return(0, " ".join(map(str, values)))
    
    itemsInGroup = ceil(n/m)
    
    #неправильное разбиение на группы, снова не использую дп
    groups = []
    for i in range(m):
        subgroup = []
        mult = itemsInGroup * i
        for j in range(mult, mult + itemsInGroup):
            if j < len(values):
                subgroup.append(values[j])
            else:
                break
        groups.append(subgroup)
    
    totalsum = 0
    result = []
    for group in groups:
        placementOfStation = group[len(group) // 2] 
        sumOfCurrent = sum(abs(j - placementOfStation) for j in group)

        totalsum += sumOfCurrent
        result.append(placementOfStation)

    return(totalsum, " ".join(map(str, result)))

    
firstRow = list(map(int, input().split(' ')))
secondRow = list(map(int, input().split(' ')))

res = charging(firstRow[0], firstRow[1], secondRow)
print(res[0])
print(res[1])