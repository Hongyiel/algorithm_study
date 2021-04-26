# 상호배타적 집합(Disjoint-Set)알고리즘
# 여러 노드가 존재할 때, 선택한 두 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘이다

# 일반적으로 유니온파인드를 사용하게 될 경우, 평균적으로 트리의 높이만큼 탐색하는 O(logN)이지만, 
# 트리를 형성하는 과정에서 사향트리(Skewed Tree)가 될 수 있으며, 
# 이렇게 될 경우 시간 복잡도는 O(n)이 되어버린다.

# 해결방안: 경로 압축(Path Compression)
# 시간 복잡도: O(logN)
# https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html


# 좀더 자세한 설명 
#https://ssungkang.tistory.com/entry/Algorithm-%EC%9C%A0%EB%8B%88%EC%98%A8-%ED%8C%8C%EC%9D%B8%EB%93%9CUnion-Find


# 제일 깔끔한 설명 (강추)
# https://velog.io/@woo0_hooo/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-union-find-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98


# set find function

# merge elements that includes

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')