from collections import deque

def min_steps(goal: int):
    queue = deque([(1, 0)])
    visited = set([1])
    parentNodeArray = [-1] * (goal)

    current = 0
    steps = 0
    nextValues = [0, 0, 0]
    while queue:
        current, steps = queue.popleft()
        
        if current == goal:
            curr = current
            path = [current]
            while(curr != 1):
                path.append(parentNodeArray[curr - 1])
                curr = parentNodeArray[curr - 1]
            print(steps)
            path.reverse()
            print(" ".join(map(str, path)))   
            return
        
        nextValues[0] = current + 1
        nextValues[1] = current * 2
        nextValues[2] = current * 3
        for next in nextValues:
            if next <= goal and next not in visited:
                visited.add(next)
                queue.append((next, steps + 1))
                parentNodeArray[next - 1] = current
    

min_steps(int(input()))
    
