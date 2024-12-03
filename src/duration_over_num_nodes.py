import numpy as np
from or_tools.tsp import optimize_routes
from modules.visualization import plot_durations
from scipy.spatial import distance_matrix
import time
from tqdm import tqdm

depot = 0
min_num_nodes = 10
max_num_nodes = 200
step = 10
trials_per_num_nodes = 9

nodes_list = list(range(min_num_nodes, max_num_nodes + step, step))

mean_durations = []
max_durations = []
min_durations = []
upper_quartiles = []
lower_quartiles = []
for num_nodes in tqdm(nodes_list):
    duration_list = []
    for _ in range(trials_per_num_nodes):
        start = time.process_time()
        nodes = np.random.randint(1, 1000, size=(num_nodes, 2))
        nodes = np.unique(nodes, axis=0)

        distances = np.round(1000 * distance_matrix(nodes, nodes)).astype(
            int
        )  # Or tool solver uses integer. Therefore, multiply by 1000 and round

        routes = optimize_routes(distances, depot, print_solution_to_console=False)
        end = time.process_time()
        duration = end - start
        duration_list.append(duration)

    quartiles = np.percentile(duration_list, [25, 50, 75])

    mean_durations.append(quartiles[1])
    max_durations.append(max(duration_list))
    min_durations.append(min(duration_list))
    upper_quartiles.append(quartiles[2])
    lower_quartiles.append(quartiles[0])

plot_durations(
    mean_durations,
    max_durations,
    min_durations,
    upper_quartiles,
    lower_quartiles,
    nodes_list,
)
