import sys
import heapq

def Dijkstra(start):
    table[start] = 0
    heapq.heappush(heap,(0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        if table[now] < cost:
            continue
        for w, next_node in graph[now]:
            next_cost = w + cost
            if next_cost < table[next_node]:
                table[next_node] = next_cost
                heapq.heappush(heap,(next_cost,next_node))


input = sys.stdin.readline
inf = sys.maxsize
start_n = 0
V = int(input())
E = int(input())
map(int,(V,E))
table = [inf]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


Dijkstra(start_n)
print('0',end=' ')
for i in range(1,V):
    print("inf" if table[i] == inf else table[i],end = ' ')
