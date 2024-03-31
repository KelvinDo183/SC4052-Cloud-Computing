from utils import read_graph_from_file
import networkx as nx
import matplotlib.pyplot as plt
from utils import read_graph_from_file


def visualize_graph(G, image_path):
    nx_graph = nx.DiGraph()
    for source, targets in G.items():
        for target in targets:
            nx_graph.add_edge(source, target)

    plt.figure(figsize=(8, 6))
    nx.draw(nx_graph, with_labels=True, node_color='skyblue', node_size=700,
            edge_color='k', linewidths=1, font_size=15, arrows=True)
    plt.title('Graph Visualization')

    plt.savefig(image_path)
    print(f"Graph image saved as '{image_path}'")
    plt.show()


if __name__ == '__main__':
    file_path = 'Graph/graph_random_1.txt'

    image_path = 'Graph/Graph_Random_1.png'

    G, N = read_graph_from_file(file_path)
    visualize_graph(G, image_path)
