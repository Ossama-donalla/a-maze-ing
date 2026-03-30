graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}
visited = []
queue = ['A']

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        for e in graph[node]:
            queue.append(e)

print(visited)