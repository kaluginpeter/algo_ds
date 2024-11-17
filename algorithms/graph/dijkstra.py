import heapq


def dijkstra_all_paths(
    source: any, vertexes: iter, paths: iter
) -> dict[any, int]:
    """
    Function that return all shortest path from source to any other nodes.
    Graph should be weighted and contain only positive weight.
    Use Dijkstra to find shortest path.
    If node can't be destinated by source, value of path will be float('inf').
    Params:
    - source: any start vertex Should be hashible
    - vertexes: iterable contains all nodes in weighted graph
    - paths: iterable contains pack of path (source, destination, weight)
    - return: dict of pairs <edge, distance>, where distance is the shortest path from start source.
    Time Complexity: O(ElogE), where E is the edges in graph
    Memory Complexity: O(ElogE), where E is the edges in graph
    """
    distances: dict[any, int] = dict()
    bound: int = float('inf')
    for vertex in vertexes:
        distances[vertex] = bound
    adj_list: dict[any, list[tuple[any, any]]] = dict()
    for path in paths:
        vertex, destination, weight = path
        if vertex not in adj_list:
            adj_list[vertex] = list()
        adj_list[vertex].append((weight, destination))
    min_heap: list[tuple[int, int]] = [(0, source)]
    while min_heap:
        cur_dist, cur_vertex = heapq.heappop(min_heap)
        if distances[cur_vertex] <= cur_dist:
            continue
        distances[cur_vertex] = cur_dist
        for edge in adj_list.get(cur_vertex, []):
            next_dist: int = cur_dist + edge[0]
            next_vertex: any = edge[1]
            if next_dist < distances[next_vertex]:
                heapq.heappush(min_heap, (next_dist, next_vertex))
    return distances


def dijkstra_shortest_path(
    source: any, destination: any, paths: iter
) -> int:
    """
    Function that return shortest path from source to destination.
    Graph should be weighted in contain only positive weight.
    Use Dijkstra to find shortest path.
    If vertex can't be destinated by source, function return float('inf')
    Params:
    - source: any, starting vertex. Should be hashible
    - desination: any, destination vertex. Should be hashible
    - paths: iter, iterable containing (source, destination, weight)
    - return: int minimum distance from source to destination.
    Time Complexity: O(ElogE), where E is the edges in graph
    Memory Complexity: O(ElogE), where E is the edges in graph
    """
    adj_list: dict[any, list[tuple[int, int]]] = dict()
    for path in paths:
        vertex, edge, weight = path
        if vertex not in adj_list:
            adj_list[vertex] = list()
        adj_list[vertex].append((weight, edge))
    min_heap: list[tuple[int, int]] = [(0, source)]
    seen: set[any] = set()
    while min_heap:
        cur_dist, cur_vertex = heapq.heappop(min_heap)
        if cur_vertex in seen:
            continue
        if cur_vertex == destination:
            return cur_dist
        seen.add(cur_vertex)
        for edge in adj_list.get(cur_vertex, []):
            next_dist = cur_dist + edge[0]
            next_vertex = edge[1]
            if next_vertex not in seen:
                heapq.heappush(min_heap, (next_dist, next_vertex))
    return float('inf')
