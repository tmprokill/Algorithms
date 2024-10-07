from math import inf

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

def int_task(nums: list[int]):
    binary_representation = [decimalToBinary(i) for i in nums]
    maxLength = len(max(binary_representation, key = len))
    for i in range(len(binary_representation)):
        diff = maxLength - len(binary_representation[i])
        if (diff != 0):
            binary_representation[i] = ("0" * diff) + binary_representation[i]
    
    minValue = inf
    print(int(binary_representation[1], 2))

row = list(map(int,input().split(' ')))

int_task(row)