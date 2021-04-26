
from collections import deque

n, m = map(int, input().split())
in_degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q = deque()
result = []

def sortRange():
    
    for _ in range(n):
        print(q)
        print(graph)
        if not q:
            return
        
        target = q.popleft()
        result.append(target)
        
        for j in graph[target]:
            in_degree[j] -= 1
            if not in_degree[j]:
                q.append(j)

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

sortRange()
print(*result)

# 3 2
# 1 3
# 2 3

