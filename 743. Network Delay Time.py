class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
                graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N+1)}
        dist[K] = 0
        
        visited = [False] * (N+1)
        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not visited[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            if cand_node < 0:
                break
            visited[cand_node] = True
            for v, w in graph[cand_node]:
                dist[v] = min(dist[v], dist[cand_node] + w)
        ans = max(dist.values())
        return ans if ans < float('inf') else - 1