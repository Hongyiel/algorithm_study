#Floyd_warshall

# 중요사항
# 플로이드 와샬 알고리즘은 다익스트라 알고리즘과 마찬가지로 최단 경로를 구할 때 사용하는 알고리즘입니다. 
# 그러나 한 지점에서 다른 특정 지점까지 최단 거리를 구하는 다익스트라 알고리즘과 달리 
# 플로이드 와샬 알고리즘은 모든 지점에서 다른 모든 지점까지의 경로를 구하는데 사용하는 알고리즘입니다.


# 중간 노드 설정 기준이다 .

# 플로이드-워셜 알고리즘은 시간 복잡도가 O(n^3)으로, 
# 그래프의 크기가 작아 세제곱 시간 알고리즘을 적용해도 
# 문제가 풀릴 때만 사용할 수 있습니다.

N = 4
INF = float('inf')
# 가중치 인접행렬
# 중요차이점: 각각의 노드에서 자른노드까지의 거리가 다르다
adj = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]

print('가중치 인접 행렬')
for row in adj:
    print(row)
print()

# 거쳐가는 정점 k를  기준으로
for k in range(N):
    # 출발 정점 i 에서
    for i in range(N):
        # 도착 정점 j 까지
        for j in range(N):
            # i에서 k를 거쳐 j 까지 가는 것과 i에서 j까지 바로가는 것중 값이 더 작은 것으로 갱신
            adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])

print('결과')
for row in adj:
    print(row)
print()


# Reference
# https://deok2kim.tistory.com/174

