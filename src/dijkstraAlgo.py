import queue as Q
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

adj = [[] for i in range (n+1)]
DIST = [1e9]*(n+1)


def dijkstra(src):

    q = Q.PriorityQueue()
    q.put((0, src))
    DIST[src]=0

    while not q.empty():
        pp = q.get()
        here = pp[1]
        dist = pp[0]

        if DIST[here] < dist:
            continue

        for i in adj[here]:
            cost = dist + i[1]
            if DIST[i[0]] > cost:
                DIST[i[0]] = cost
                q.put((cost, i[0]))


while m:
    m -= 1
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

dijkstra(start)

for i in range (1,n+1):
    if DIST[i] is 1e9:
        print("INF")
    else:
        print(DIST[i])
