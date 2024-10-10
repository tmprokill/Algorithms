from math import inf

binary_sum = lambda a,b : bin(int(a, 2) + int(b, 2))

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

def int_task(nums: list[int]):
    binary_representation = [decimalToBinary(i) for i in nums]
    maxLength = len(max(binary_representation, key = len))
    for i in range(len(binary_representation)):
        diff = maxLength - len(binary_representation[i])
        if (diff != 0):
            binary_representation[i] = ("0" * diff) + binary_representation[i]
        binary_representation[i] = ''.join(sorted(binary_representation[i]))

    goal = sum(i == '1' for i in binary_representation[2])
    for i in range(binary_representation[0]):
        for j in range(binary_representation[1]):
            currSum = binary_sum(binary_representation[i] + binary_representation[j])
            if sum(i == '1' for i in currSum) == goal:
                return currSum
   


row = list(map(int,input().split(' ')))

int_task(row)