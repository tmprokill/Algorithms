from math import inf

binary_sum = lambda a,b : bin(int(''.join(a), 2) + int(''.join(b), 2))[2:]

def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1

def rindexOnSub(binary: list[str], value: str, end_index: int) -> int:
    for i in range(end_index, -1, -1):
        if binary[i] == value:
            return i
    
    return -1

def decimalToBinary(n): 
    return list(bin(n).replace("0b", ""))

def shiftNulls(binary: list[str]):
    rightmost_one_index = rindex(binary, '1')

    change = -1
    for i in range(rightmost_one_index - 1, -1, -1):
        if binary[i] == '0' and binary[i + 1] == '1':
            binary[i], binary[i + 1] = binary[i + 1], binary[i]
            change = 0
            break
    if change == -1:
        return change
    return binary

def int_task(nums: list[int]):
    binary_representation = [decimalToBinary(i) for i in nums]
    maxLength = len(max(binary_representation, key = len))
    for i in range(len(binary_representation)):
        diff = maxLength - len(binary_representation[i])
        if (diff != 0):
            binary_representation[i] = ["0" * diff] + binary_representation[i]
        binary_representation[i] = sorted(binary_representation[i])
    
    goal = sum(i == '1' for i in binary_representation[2])
    currSum = binary_sum(binary_representation[0], binary_representation[1])
    countOfOnesInSum = sum(i == '1' for i in currSum)

    if countOfOnesInSum == goal and len(currSum) == len(binary_representation[2]):
        return int(currSum, 2)
    
    while True:
        rightmost_one_index_0 = rindexOnSub(binary_representation[0], '1', len(binary_representation[0]) - 1)
        rightmost_one_index_1 = rindexOnSub(binary_representation[1], '1', len(binary_representation[1]) - 1)

        firstIndex = rindexOnSub(binary_representation[0], '0', rightmost_one_index_0 - 1)
        secondIndex = rindexOnSub(binary_representation[1], '0', rightmost_one_index_1 - 1)

        if firstIndex > secondIndex:
            result = shiftNulls(binary_representation[0])
        else:
            result = shiftNulls(binary_representation[1])

        if result == -1:
            break  
        
        currSum = binary_sum(binary_representation[0], binary_representation[1])
        countOfOnesInSum = sum(i == '1' for i in currSum)

        if countOfOnesInSum == goal:
            return int(currSum, 2)

    return -1
row = list(map(int,input().split(' ')))

print(int_task(row))