#깊이있는 탐색
#대상노드에 해당하는 전체 노드를 하위 목록으로 탐색하는 방법이다

def DFS_with_adj_list(graph, root):
    
    visited = []
    stack = [root]

    while stack:
        # print(stack)
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            print(graph)
            print(graph[n])
            # print(set(visited))
            stack += graph[n] - set(visited)
    return visited


graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

print(DFS_with_adj_list(graph_list, root_node))

