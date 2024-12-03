import numpy as np
import matplotlib.pyplot as plt


def plot_nodes(nodes, route=None):
    # Assign indices to nodes
    indices = np.arange(len(nodes))

    # Plot the nodes
    plt.figure(figsize=(8, 6))
    plt.scatter(nodes[:, 0], nodes[:, 1], color="blue", s=100, edgecolors="black")

    # Annotate each node with its index
    for idx, (x, y) in zip(indices, nodes):
        plt.text(x + 0.1, y + 0.1, str(idx), fontsize=12, color="red")

    # If a route is provided, plot the route
    if route is not None:
        # Ensure the route is a complete loop by appending the start node at the end
        complete_route = np.append(route, route[0])
        # Get the coordinates of the nodes in the order of the route
        route_nodes = nodes[complete_route]
        # Plot the route
        plt.plot(route_nodes[:, 0], route_nodes[:, 1], "r-", linewidth=2, label="Route")
        # Mark the start and end points
        plt.scatter(
            nodes[route[0], 0],
            nodes[route[0], 1],
            color="green",
            s=150,
            label="Start/End",
        )
        plt.legend()

    # Add labels and title
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Nodes for Traveling Salesman Problem")
    plt.grid(True)
    plt.show()


def plot_durations(
    mean_durations,
    max_durations,
    min_durations,
    upper_quartiles,
    lower_quartiles,
    nodes_list,
):
    """
    Plots the mean durations with number of nodes on x-axis and durations on y-axis.
    Mean durations are plotted as a line.
    The area between min and max durations is shaded to indicate variability.

    Parameters:
    - mean_durations: list of mean durations
    - max_durations: list of maximum durations
    - min_durations: list of minimum durations
    """
    # Check that all lists are the same length
    if not (len(mean_durations) == len(max_durations) == len(min_durations)):
        raise ValueError("All duration lists must have the same length.")

    # x-axis: number of nodes
    x = nodes_list

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot mean durations
    ax.plot(x, mean_durations, label="Mean Duration", color="blue")
    ax.plot(
        x, upper_quartiles, label="Upper Quartile", color="blue", linestyle="dashed"
    )
    ax.plot(
        x, lower_quartiles, label="Lower Quartile", color="blue", linestyle="dashed"
    )

    # Shade between min and max durations
    ax.fill_between(
        x,
        min_durations,
        max_durations,
        color="blue",
        alpha=0.2,
        label="Min-Max Duration",
    )

    # Add labels and title
    ax.set_xlabel("Number of Nodes")
    ax.set_ylabel("Duration")
    ax.set_title("TSP Algorithm Durations vs Number of Nodes")

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()
