from collections import deque

def min_steps(goal: int):
    queue = deque([(1, 0)])
    visited = set([1])
    parentNodeDict = {
        1: -1
    }

    while queue:
        current, steps = queue.popleft()
        
        if current == goal:
            curr = current
            path = [str(current)]
            while(curr != 1):
                path.append(parentNodeDict[curr])
                curr = parentNodeDict[curr]
            print(steps)
            path.reverse()
            print(" ".join(map(str, path)))   
            return
        
        for next in (current + 1, current * 2, current * 3):
            if next <= goal and next not in visited:
                visited.add(next)
                queue.append((next, steps + 1))
                parentNodeDict[next] = current
    

min_steps(int(input()))
    
