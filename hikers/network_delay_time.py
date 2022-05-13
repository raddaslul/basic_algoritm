from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
        # 최단경로 알고리즘인 다익스트라 알고리즘으로 풀 수 있다

        graph = defaultdict(list)

        # 출발지를 key로 하고 도착지와 소요시간을 tuple 형태로 value 값을 가지는 dict 구현
        for u, v, w in times:
            graph[u].append((v, w))
        print(graph)

        # 시작점에서 '정점'까지의 소요 시간과 도착지점을 저장
        Q = [(0, k)]
        distance = defaultdict(int)

        while Q:
            time, destination = heapq.heappop(Q)
            print(time, destination)
            # distance에 목적지까지 걸리는 시간이 없다면 해당 데이터를 저장
            if destination not in distance:
                distance[destination] = time
                print(distance)
                for v, w in graph[destination]:
                    time_spent = time + w   # 현재까지 걸린시간에 앞으로 걸릴 시간을 더해서 저장
                    heapq.heappush(Q, (time_spent, v))
                    print(Q)

        # 주어진 도착지점을 모두 돌았다면 가장 오래 걸린 시간을 리턴
        if len(distance) == n:
            return max(distance.values())

        return -1

    result = networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
    print(result)
