import heapq
def distances(graphs,source):
    distances={node:float('inf') for node in graphs}
    distances[source]=0
    priority_queue=[(0,source)]
    while priority_queue:
        current_distance,current_node=heapq.heappop(priority_queue)
        if current_distance> distances[current_node]:
            continue
        for neighbour,weight in graphs[current_node]:
            distance=weight+current_distance
            if distance<distances[neighbour]:
                distances[neighbour]=distance
                heapq.heappush(priority_queue,(distance,neighbour))
    return distances