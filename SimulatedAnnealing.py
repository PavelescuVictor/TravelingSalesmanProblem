from Utility import generate_neighbour, generate_random_permutation, rnd_number, acceptance_probability
from math import exp
from copy import deepcopy

from PlotUtility import plot_solution
from matplotlib import pyplot
import time

class SimulatedAnnealing:

    def __init__(self, repo):
        self.repository = repo

    def simulated_annealing(self, temp, temp_min, alpha, max_iterations):
        total_iterations = 0
        # Token to use the plot
        use_plot_token = False
        # First permutation
        old_permutation = generate_random_permutation(self.repository.get_repo_size())
        old_cost = round(self.repository.evaluation(old_permutation),2)
        print(old_cost)
        print(old_permutation)

        # Best permutation overall
        best_permutation = old_permutation
        best_cost = round(self.repository.evaluation(old_permutation),2)

        # Start permutation value
        start_value = round(self.repository.evaluation(old_permutation),2)

        # Create plot
        if use_plot_token is True:
            fig = pyplot.figure( figsize=(12, 8))
            fig.show()
            plot_solution(self.repository.get_repo_storage(), old_permutation, fig)

        while temp > temp_min:
            #print(temp)
            i = 1
            while i <= max_iterations:
                # Generate new neighbour
                aux_permutation = deepcopy(old_permutation)
                new_permutation = generate_neighbour(aux_permutation)
                new_cost = round(self.repository.evaluation(new_permutation),2)

                # Save best solution
                if new_cost < best_cost:
                    best_permutation = deepcopy(new_permutation)
                    best_cost = new_cost

                # Calculate probability of acceptance
                delta = new_cost - old_cost
                ap = acceptance_probability(delta, temp)
                print("Total Iterations: {} -- Old Cost: {} -- New Cost: {} -- Delta: {} -- Temperature: {} -- Ap value: {}".format(total_iterations, old_cost, new_cost, delta, temp, ap))

                if delta < 0:
                    old_permutation = new_permutation
                    old_cost = new_cost
                    if use_plot_token is True:
                        plot_solution(self.repository.get_repo_storage(), old_permutation, fig)
                        pyplot.pause(0.01)

                elif ap > rnd_number(0,1):
                    old_permutation = new_permutation
                    old_cost = new_cost
                    if use_plot_token is True:
                        plot_solution(self.repository.get_repo_storage(), old_permutation, fig)
                        pyplot.pause(0.000000000001)
                total_iterations = total_iterations + 1
                i = i + 1
            temp = temp * alpha
            total_iterations = total_iterations + 1
        if use_plot_token is True:
            pyplot.draw()
            time.sleep(5)
        print("Start distance value: {}".format(start_value))
        print("Best distance value: {}".format(best_cost))
        return "Start distance value:{}\nBest distance value:{}\n".format(start_value, best_cost)