from SimulatedAnnealing import SimulatedAnnealing
from Utility import read_from_file, print_distance_matrix
from Repository import Repository
from Classes.Table import Table
from GeneticAlgorithm import GeneticAlgorithm

import time

class UserInterface:

    def __init__(self):
        self.repository = Repository()
        self.sa = SimulatedAnnealing(self.repository)
        self.ga = GeneticAlgorithm(self.repository)
        self.table = Table('')

    def main_menu(self):
        print("\n0.Exit program.")
        print("1.Read from file.")
        print("2.Read from keyboard.")
        print("3.Print distance matrix.")
        print("4.Simulated Annealing(SA).")
        print("5.Tabu Search(TS).")
        print("6.Genetic Algorithm.")

    def get_sa(self):
        return self.sa

    def get_ga(self):
        return self.ga

    def get_repository(self):
        return self.repository

    def set_repository(self, repo):
        self.repository = repo

    def set_sa(self, sa):
        self.sa = sa

    def set_ga(self, ga):
        self.ga = ga

if __name__ == "__main__":
    # Create an instance of the Backpack class.
    ui = UserInterface()
    loop_token = 1
    while loop_token:
        ui.main_menu()
        try:
            opt = int(input('Insert number of the option choosed: '))
        except ValueError:
            print("\nThe option is not a valid number.")
        else:
            if opt == 1:
                #file_name = input('Insert the name of the file (type: name.txt): ')
                file_name = "kroA100.tsp"
                #file_name = "ch150.tsp"
                if file_name[-4:] == ".tsp":
                    ui.set_repository(read_from_file(file_name, ui.get_repository()))
                else:
                    print("The name doesn't follow the type specified (type: name.txt).")
            elif opt == 2:
                print("2")
            elif opt == 3:
                print_distance_matrix(ui.get_repository())
            elif opt == 4:
                sa = SimulatedAnnealing(ui.get_repository())
                ui.set_sa(sa)
                try:
                    T = int(input('Insert temperature value: '))
                    T_min = float(input('Insert minimum temperature value: '))
                    alpha = float(input('Insert alpha value: '))
                    iterations = int(input('Insert number of iterations: '))
                    '''
                    T = 10
                    T_min = 0.00001
                    alpha = 0.9999
                    iterations = 10
                    '''
                    text_file = open("Tests.txt", "a")
                    text_file.write("Test:\n")
                    text_file.write("\n")
                    #T = 100
                    #T_min = 0.001
                    #alpha = 0.9
                    #iterations = 100
                    text_file.write("T: %s\n" %T)
                    text_file.write("T_min: %s\n" %T_min)
                    text_file.write("Alpha: %s\n" %alpha)
                    text_file.write("Iterations: %s\n" %iterations)
                except ValueError:
                    print("\n Inputs are not valid.")
                else:
                    start_time = time.time()
                    print(ui.get_sa().simulated_annealing(T, T_min, alpha, iterations))
                    text_file.write("Results:\n %s\n" %ui.get_sa().simulated_annealing(T, T_min, alpha, iterations))
                    text_file.write("--- %s ---" % (time.time() - start_time))
                    print("--- %s seconds --- \n\n" % (time.time() - start_time))
                    text_file.close()
            elif opt == 5:
                try:
                    number_eval = int(input('How many evaluations?: '))
                except ValueError:
                    print("\nThat's not a valid number.")
                else:
                    start_time = time.time()
                    print("5")
                    #best = ui.steepest_ascent_hill_climbing(number_eval, '00000000000000000000', 0)
                    print("--- %s seconds ---" % (time.time() - start_time))
            elif opt == 6:
                ga = GeneticAlgorithm(ui.get_repository())
                ui.set_ga(ga)
                number_generations = 1000
                population_size = 50
                crossover_probability = 100
                mutation_probability =  1
                text_file = open("TestsGA.txt", "a")
                text_file.write("Test:\n")
                text_file.write("\n")
                text_file.write("number generations: %s\n" % number_generations)
                text_file.write("population size: %s\n" % population_size)
                text_file.write("crossover probability: %s\n" % crossover_probability)
                text_file.write("mutation probability: %s\n" % mutation_probability)
                # best_so_far_distance = ui.ga.genetic_algorithm_initalization(population_size, number_generations, crossover_probability, mutation_probability)
                # text_file.write("best so far distance: %s\n" % best_so_far_distance)
                # text_file.close()
                best = 200000
                avg = 0
                for i in range(0,10):
                    print(i)
                    best_so_far_distance = ui.ga.genetic_algorithm_initalization(population_size, number_generations, crossover_probability, mutation_probability)
                    text_file.write("distance: %s\n" % best_so_far_distance)
                    avg = avg + best_so_far_distance
                    if best_so_far_distance < best:
                        best = best_so_far_distance
                avg = avg/10
                text_file.write("avg distance: %s\n" % avg)
                text_file.write("best distance: %s\n" % best)
                text_file.close()
            elif opt == 0:
                loop_token = 0
                print("\nExiting program.")
            else:
                print("\nThat is not a valid option.")
