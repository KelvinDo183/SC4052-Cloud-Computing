import numpy as np
from utils import read_graph_from_file
import matplotlib.pyplot as plt
import time


def build_transition_matrix(G, N):
    M = np.zeros((N, N))
    for j in range(N):
        if j in G:
            links = G[j]
            if len(links) > 0:
                M[links, j] = 1 / len(links)
            else:  # Dangling node
                M[:, j] = 1 / N
        else:
            M[:, j] = 1 / N
    return M


def pagerank(M, num_iterations=100, d=0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = (d * M + (1 - d) / N)
    changes = []
    start_time = time.time()
    for i in range(num_iterations):
        v_new = M_hat @ v
        # Compute the change and track it
        change = np.linalg.norm(v_new - v, 1)
        changes.append(change)
        v = v_new
        # Break if the change is very small
        if change < 1e-6:
            break
    end_time = time.time()
    return v, changes, end_time - start_time


def pagerank_closed_form(M, d=0.85):
    start_time = time.time()
    N = M.shape[1]
    I = np.eye(N)
    ones = np.ones((N, 1))
    v = np.linalg.inv(I - d * M) @ ((1 - d) / N * ones)
    end_time = time.time()
    return v / np.linalg.norm(v, 1), end_time - start_time


def compare_pageranks(M, d=0.85, num_iterations=100):
    pr_iterative = pagerank(M, num_iterations, d)[0].flatten()

    pr_closed_form = pagerank_closed_form(M, d)[0].flatten()

    indices = np.arange(len(pr_iterative))

    plt.figure(figsize=(18, 6))

    # Iterative Method
    plt.subplot(1, 2, 1)
    plt.plot(indices, pr_iterative, 'o-', label='Iterative Method')
    plt.title('PageRank: Iterative Method')
    plt.xlabel('Node Index')
    plt.xticks(indices)
    plt.ylabel('PageRank Value')
    plt.legend()
    plt.grid(True)

    # Closed-Form Solution
    plt.subplot(1, 2, 2)
    plt.plot(indices, pr_closed_form, 's-',
             color='red', label='Closed-Form Solution')
    plt.title('PageRank: Closed-Form Solution')
    plt.xlabel('Node Index')
    plt.xticks(indices)
    plt.ylabel('PageRank Value')
    plt.legend()
    plt.grid(True)

    # Save the figure comprising both subplots
    plt.savefig('Visualisation_Results/Pagerank_Comparison.png')
    plt.show()
    return


if __name__ == '__main__':
    file_path = 'Graph/graph_random_1.txt'

    # Read the graph from the file and construct the adjacency list
    G, N = read_graph_from_file(file_path)

    # Build the transition matrix from the graph G
    M = build_transition_matrix(G, N)

    # Compute the PageRank
    pagerank_scores, changes, time_iterative = pagerank(M)
    time_closed_form = pagerank_closed_form(M)[1]
    print("PageRank scores:\n", pagerank_scores)
    print(f"Total time for iterative method: {time_iterative}s")
    print(f"Total time for closed-form method: {time_closed_form}s")
    # Visualizing convergence
    plt.figure(figsize=(10, 6))
    plt.plot(changes, marker='o', linestyle='-', color='b')
    plt.title('PageRank Convergence')
    plt.xlabel('Iteration')
    plt.ylabel('Change in PageRank')
    plt.grid(True)
    plt.savefig('Visualisation_Results/Pagerank_Convergence.png')
    plt.show()
    compare_pageranks(M)
