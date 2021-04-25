from queue import Queue


q = Queue(maxsize=0)
q.put(0)
stark = [1,2,3]
get_pop = stark.pop()
print(get_pop)