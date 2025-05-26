from bisect import bisect_right
from sys import stdin

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def add(self, i, val):
        i += 1  
        while i <= self.size:
            self.tree[i] += val
            i += i & (-i) 
    
    def sum(self, i):
        i += 1  
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i) 
        return result

def process_queries(queries):
    coords = set()
    for query in queries:
        x = int(query[1])
        coords.add(x)
    
    coords = sorted(coords)
    coord_to_idx = {x: i for i, x in enumerate(coords)}
    
    t = FenwickTree(len(coords))
    
    result = []
    for query in queries:
        op, x = query[0], int(query[1])
        if op == '+':
            i = coord_to_idx[x]
            t.add(i, x)
        else:
            pos = bisect_right(coords, x)
            if pos == 0:
                result.append(0)
            else:
                result.append(t.sum(pos - 1))
    
    return result

def read_input():
    queries = []
    for line in stdin:
        line = line.strip()
        if line:
            queries.append(line.split())
        else:
            break
    return queries

if __name__ == "__main__":
    queries = read_input()
    results = process_queries(queries)
    for res in results:
        print(res)