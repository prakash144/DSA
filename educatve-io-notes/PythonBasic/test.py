import heapq

li = [12, 5, 787, 1, 23]
k = 2
n = 5
min_heap = li[:k]
heapq.heapify(min_heap)

for i in range(k, n):
    if li[i] > min_heap[0]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, li[i])
        
result = sorted(min_heap, reverse=True)

print(result)