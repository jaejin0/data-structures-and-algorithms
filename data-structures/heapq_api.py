import heapq
array = [-3, 0, 2, 1, -2, -1, 3]

heapq.heapify(array)

print(array)

heapq.heappush(array, 4)
print(array)

heapq.heappop(array)

print(array)
