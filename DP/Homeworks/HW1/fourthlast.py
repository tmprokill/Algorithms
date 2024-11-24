def decimalToBinary(n):
    return list(bin(n).replace("0b", ""))

def binary_sum(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

def generate_permutations(s):
    result = []
    s = sorted(s)
    
    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
            return
        seen = set()
        for i in range(start, len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                s[start], s[i] = s[i], s[start]
                backtrack(start + 1)
                s[start], s[i] = s[i], s[start]

    backtrack(0)
    return result

def int_task(nums):
    binary_representation = [decimalToBinary(i) for i in nums]
    maxLength = len(max(binary_representation, key=len))
    
    for i in range(len(binary_representation)):
        diff = maxLength - len(binary_representation[i])
        if diff != 0:
            binary_representation[i] = ['0'] * diff + binary_representation[i]
    
    for i in range(len(binary_representation)):
        binary_representation[i] = sorted(binary_representation[i])
    
    goal = binary_representation[2].count('1')
    
    first_sorted = ''.join(binary_representation[0])
    second_sorted = ''.join(binary_representation[1])
    
    min_c_prime = float('inf')
    
    perm_a_list = generate_permutations(first_sorted)
    perm_b_list = generate_permutations(second_sorted)
    
    for a_perm in perm_a_list:
        for b_perm in perm_b_list:
            sum_bin = binary_sum(a_perm, b_perm)
            
            if sum_bin.count('1') == goal:
                if len(sum_bin) <= maxLength:
                    min_c_prime = min(min_c_prime, int(sum_bin, 2))
    
    return min_c_prime if min_c_prime != float('inf') else -1

row = list(map(int, input().split()))
print(int_task(row))