graph = {}

graph["start"] = {}
graph["a"] = {}
graph["b"] = {}
graph["fin"] = {}

graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"]["fin"] = 1
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {} 
parents["a"] = "start" 
parents["b"] = "start" 
parents["fin"] = None

processed = []

def search():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neigbours = graph[node]
        for n in neigbours.keys():
            new_cost = cost + neigbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
            print(costs)
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

search()

print(costs)

