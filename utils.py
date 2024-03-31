def read_graph_from_file(file_path):
    G = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Adjust split() based on the file format
            source, target = map(int, line.strip().split())
            if source not in G:
                G[source] = []
            G[source].append(target)
    N = len(set(G.keys()) | set(
        [node for sublist in G.values() for node in sublist]))
    return G, N
