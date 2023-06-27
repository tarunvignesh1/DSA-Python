# Heapq

import heapq

# by default its minheap, for maxheap, values need to be negated

minheap = []

heapq.heappush(minheap, 3)
heapq.heappush(minheap, 8)
heapq.heappush(minheap, 11)
heapq.heappush(minheap, 6)

#print(minheap[0])

#while len(minheap):
#    print(heapq.heappop(minheap))

# to heapfiy an array
arr = [2,1,4,7,9]
heapq.heapify(arr)

print(arr)
