from matplotlib import pyplot

def plot_solution(cities, solution, fig):
    plot_x_coords = []
    plot_y_coords = []
    for index in range(0, len(solution)):
        current_node = cities[solution[index] - 1]

        plot_x_coords.append(int(current_node.get_xcoord()))
        plot_y_coords.append(int(current_node.get_ycoord()))

    plot_x_coords.append(cities[solution[0]].get_xcoord())
    plot_y_coords.append(cities[solution[0]].get_ycoord())

    pyplot.clf()
    pyplot.plot(plot_x_coords,plot_y_coords, marker='o')
    fig.canvas.draw()