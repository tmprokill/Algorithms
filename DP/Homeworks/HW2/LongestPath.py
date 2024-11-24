from collections import deque

def findLongestPath(n, edges):
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for b, e in edges:
        adj[b].append(e)
        in_degree[e] += 1

    topo_order = []
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    dp = [0] * (n + 1)
    for node in topo_order:
        for neighbor in adj[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + 1)

    return max(dp)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(findLongestPath(n, edges))
