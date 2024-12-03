import numpy as np
from or_tools.tsp import optimize_routes
from modules.visualization import plot_nodes
from scipy.spatial import distance_matrix

nodes = np.random.randint(1, 100, size=(100, 2))
nodes = np.unique(nodes, axis=0)
# nodes = np.array(
#     [
#         [94, 20],
#         [47, 28],
#         [35, 36],
#         [26, 83],
#         [29, 39],
#         [72, 11],
#         [44, 63],
#         [72, 9],
#         [63, 74],
#         [4, 61],
#         [5, 52],
#         [80, 38],
#         [39, 79],
#         [32, 31],
#         [84, 40],
#         [20, 14],
#         [19, 52],
#         [41, 40],
#         [5, 84],
#         [24, 95],
#     ]
# )
depot = 0

distances = np.round(1000 * distance_matrix(nodes, nodes)).astype(
    int
)  # Or tool solver uses integer. Therefore, multiply by 1000 and round

routes = optimize_routes(distances, depot)

plot_nodes(nodes, routes[0])
