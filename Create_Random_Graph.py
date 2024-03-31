# import random


# def generate_random_graph(num_nodes, num_edges, allow_self_loops=True, file_path='Graph/graph_random_1.txt'):
#     with open(file_path, 'w') as file:
#         for _ in range(num_edges):
#             source = random.randint(0, num_nodes - 1)
#             if allow_self_loops:
#                 target = random.randint(0, num_nodes - 1)
#             else:
#                 target = source
#                 while target == source:
#                     target = random.randint(0, num_nodes - 1)
#             file.write(f'{source} {target}\n')

#     print(
#         f"Random graph with {num_nodes} nodes and {num_edges} edges written to '{file_path}'")


# num_nodes = 100
# num_edges = 250
# generate_random_graph(num_nodes, num_edges)

import random


def generate_random_graph(num_nodes, num_edges, allow_self_loops=True, file_path='Graph/graph_random_1.txt'):
    if num_edges < num_nodes - 1:  # Ensuring minimum edges to avoid isolated nodes
        print("Increasing the number of edges to ensure no isolated nodes.")
        num_edges = num_nodes - 1

    edges = set()

    # Ensure at least one outgoing edge for each node to avoid isolated nodes
    for node in range(num_nodes):
        if allow_self_loops:
            target = random.randint(0, num_nodes - 1)
        else:
            potential_targets = list(range(num_nodes))
            potential_targets.remove(node)  # Remove self to avoid self-loop
            target = random.choice(potential_targets)
        edges.add((node, target))

    # Add the rest of the edges randomly
    while len(edges) < num_edges:
        source = random.randint(0, num_nodes - 1)
        if allow_self_loops:
            target = random.randint(0, num_nodes - 1)
        else:
            potential_targets = list(range(num_nodes))
            potential_targets.remove(source)  # Remove self to avoid self-loop
            target = random.choice(potential_targets)
        edges.add((source, target))

    with open(file_path, 'w') as file:
        for edge in edges:
            file.write(f'{edge[0]} {edge[1]}\n')

    print(
        f"Random graph with {num_nodes} nodes and {num_edges} edges written to '{file_path}'")


num_nodes = 100  # Number of nodes
num_edges = 250  # Number of edges
generate_random_graph(num_nodes, num_edges)
