def dijkstra(g, start):
    nodes = list(g.keys())
    v = [start]
    p = {start: {start: []}}
    d = {start: 0}
    pre = next = start
    nodes.remove(start)

    for a in range(len(nodes)):
        dist = float('inf')
        for i in v:
            for node in nodes:
                new = g[start][i] + g[i][node]
                if new <= dist:
                    dist = new
                    next = node
                    pre = i
                    g[start][node] = new

        d[next] = dist

        p[start][next] = [a for a in p[start][pre]]
        p[start][next].append(next)

        v.append(next)
        nodes.remove(next)

    return d, p


if __name__ == '__main__':
    g = {"s": {"s": 0, "y": 20, "z": 10, "x": 50, "w": 2},
         "y": {"s": 10, "y": 0, "z": 40, "x": 20, "w": float('inf')},
         "z": {"s": 20, "y": 10, "z": 0, "x": 10, "w": float('inf')},
         "x": {"s": 30, "y": 50, "z": 20, "x": 0, "w": float('inf')},
         "w": {"s": float('inf'), "y": 1, "z": float('inf'), "x": float('inf')},
         }

    distance, path = dijkstra(g, 's')
    print(distance)
    print(path)
