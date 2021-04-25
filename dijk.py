import heapq  # 우선순위 큐 구현을 위함
# 이 알고리즘은 최단거리를 찾는 알고리즘이라고 생각하면 된다
# 각 노드에 연결된 노드들까지 가는데 거리를 찾고
# 나온 거리를 저장 한 뒤에, 저장한 거리가 만약 새로운 노드에 해당하는 거리와 비교해서 크면 (기존 노드 거리 > 새로운 노드 거리)
# 저장되어있는 기존 노드 거리를 새로운 노드 거리로 바꾼다.
def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  print(distances)
  distances[start] = 0  # 시작 값은 0이어야 함
  print(distances)

  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
    print(current_distance, current_destination)
    print(queue)

    print("------------------------------------")
    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      print("curr len is longer than before")
      continue
    print("------------------------------------")

    for new_destination, new_distance in graph[current_destination].items():
        # dict type will comes out here
      print("this is new distance: ", new_distance)
      print("this is new destination: ", new_destination)
    #   print(new_destination, new_distance)
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      print ("this is known distance: ", distance) # 해당 노드에 대한 거리
      print ("this is new destination: ", new_destination) # 그 해당 노드
      print ("get dick on distances[new_destination]: ", distances[new_destination])
      print("###################################")
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신 (첫번째는 inf 보다 작으면 갱신 (알고있는 거리 노드가 없으면 inf겠졍?))
        distances[new_destination] = distance
        print("inside if statement's distance: ",distance)
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        print("After push")
        print(queue)
    
  return distances

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
print(dijkstra(graph, 'A'))
