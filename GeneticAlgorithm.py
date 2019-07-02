from Utility import generate_neighbour, generate_random_permutation, rnd_number, acceptance_probability
import random

from copy import deepcopy

class GeneticAlgorithm:

    def __init__(self, repo):
        self.repository = repo
        self.best_so_far = 0

    def update_best_so_far(self, permutation):
        if self.repository.evaluation(self.best_so_far) > self.repository.evaluation(permutation):
            self.best_so_far = permutation

    def print_best_so_far(self):
        print("Best so far distance: {}".format(self.repository.evaluation(self.best_so_far)))

    def initialize_best_so_far(self, permutation):
        self.best_so_far = permutation

    def print_list(self, name, list):

        print()
        print(name)
        for i in list:
            print(self.repository.evaluation(i), '-', i)
        print()

    def print_list_tuple(self, name, list):

        print()
        print(name)
        for i in list:
            print(i[0], '-', i[1])
        print()


    def genetic_algorithm_initalization(self, population_size, number_generations, crossover_probability, mutation_probability):
        # Population initialization
        population_pool = []
        for i in range(0, population_size):
            binary_random_value = generate_random_permutation(self.repository.get_repo_size())
            population_pool.append(binary_random_value)

        index_generation = 1

        ordered_population_pool = sorted(population_pool, key=lambda permuation: self.repository.evaluation(permuation),
                                         reverse=False)

        self.initialize_best_so_far(deepcopy(ordered_population_pool[0]))

        # Generations
        for i in range(0, number_generations):
            # Printing
            #print("Generations: {}".format(i+1))
            next_generation = self.next_generation(population_size, crossover_probability, mutation_probability, population_pool)
            population_pool = deepcopy(next_generation)

        return self.repository.evaluation(self.best_so_far)

    def next_generation(self, population_size, crossover_probability, mutation_probability, population_pool):

        # Order population pool by total distance of permutation (lowest to highest)
        ordered_population_pool = sorted(population_pool, key=lambda permuation: self.repository.evaluation(permuation), reverse=False)

        # Construct roulette wheel

        roulette_wheel = []
        for i in range(len(ordered_population_pool)):
            new = (ordered_population_pool[i], 1/self.repository.evaluation(ordered_population_pool[i]))
            roulette_wheel.append(new)

        #self.print_list_tuple("Roulette Wheel", roulette_wheel)

        # Crossover pool
        crossover_pool = []
        # Selection process
        random_prob = round(random.uniform(0, int(self.repository.get_repo_size())))
        if random_prob <= crossover_probability:
            while len(crossover_pool) < population_size:
                selection_parents = []
                for i in range(0, 2):
                    rand_value = random.uniform(roulette_wheel[len(roulette_wheel) - 1][1], roulette_wheel[0][1])
                    for j in range(len(roulette_wheel) - 1, -1, -1):
                        if rand_value <= roulette_wheel[j][1]:
                            selection_parents.append(roulette_wheel[j])
                            break

                # Print parents
                #print(selection_parents[0][0], selection_parents[0][1])
                #print(selection_parents[1][0], selection_parents[1][1])

                child1 = []
                child2 = []

                seg_start = random.randint(0,int(self.repository.get_repo_size())-1)
                seg_end = random.randint(0,int(self.repository.get_repo_size())-1)
                if seg_start > seg_end:
                    aux = seg_start
                    seg_start = seg_end
                    seg_end = aux
                seg_parent1 = []
                seg_parent2 = []
                for i in range(seg_start, seg_end + 1):
                    seg_parent1.append(selection_parents[0][0][i])
                    seg_parent2.append(selection_parents[1][0][i])
                index_seg = 0
                for i in range(0, int(self.repository.get_repo_size())):
                    if i >= seg_start and i <= seg_end:
                        child1.append(seg_parent1[index_seg])
                        index_seg += 1
                    else:
                        child1.append(0)
                for i in range(0, int(self.repository.get_repo_size())):
                    if selection_parents[1][0][i] not in seg_parent1:
                        found_token = False
                        position = 0
                        while found_token == False:
                            if child1[position] == 0:
                                child1[position] = selection_parents[1][0][i]
                                found_token = True
                            else:
                                position +=1

                index_seg = 0
                for i in range(0, int(self.repository.get_repo_size())):
                    if i >= seg_start and i <= seg_end:
                        child2.append(seg_parent2[index_seg])
                        index_seg += 1
                    else:
                        child2.append(0)
                for i in range(0, int(self.repository.get_repo_size())):
                    if selection_parents[0][0][i] not in seg_parent2:
                        found_token = False
                        position = 0
                        while found_token == False:
                            if child2[position] == 0:
                                child2[position] = selection_parents[0][0][i]
                                found_token = True
                            else:
                                position +=1

                crossover_pool.append(child1)
                crossover_pool.append(child2)
        else:
            for i in range(0, len(roulette_wheel)):
                crossover_pool.append(roulette_wheel[i][0])

        #self.print_list("Crossover Pool", crossover_pool)

        #Deallocate Roulette wheel
        del roulette_wheel[:]
        del roulette_wheel

        # Mutation

        for i in range(0, population_size):
            for j in range(0, int(self.repository.get_repo_size())):
                random_prob = round(random.uniform(0, int(self.repository.get_repo_size())))
                if random_prob <= mutation_probability:
                    gene = random.randint(0,int(self.repository.get_repo_size())-1)
                    aux = crossover_pool[i][j]
                    crossover_pool[i][j] = crossover_pool[i][gene]
                    crossover_pool[i][gene] = aux

        # self.print_list("Mutation Pool", crossover_pool)

        # Order crossover_pool by total distance of permutation

        ordered_crossover_pool = sorted(crossover_pool,
                                         key=lambda permuation: self.repository.evaluation(permuation),
                                         reverse=False)

        # self.print_list("Ordered Mutation pool", crossover_pool)

        # Deallocate crossover pool

        del crossover_pool[:]
        del crossover_pool

        # Construct roulette wheeel

        roulette_wheel = []
        for i in range(len(ordered_crossover_pool)):
            new = (
            ordered_crossover_pool[i], 1/self.repository.evaluation(ordered_crossover_pool[i]))
            roulette_wheel.append(new)

        del ordered_crossover_pool[:]
        del ordered_crossover_pool

        next_generation = []

        while len(next_generation) < population_size:
            rand_value = random.uniform(roulette_wheel[len(roulette_wheel) - 1][1], roulette_wheel[0][1])
            for j in range(len(roulette_wheel) - 1, -1, -1):
                if rand_value <= roulette_wheel[j][1]:
                    next_generation.append(roulette_wheel[j][0])
                    break

        # Deallocate roulette wheel

        del roulette_wheel[:]
        del roulette_wheel

        start_avg_distance = 0
        for i in range(0, len(population_pool)):
            start_avg_distance += self.repository.evaluation(population_pool[i])
        start_avg_distance = start_avg_distance / population_size

        end_avg_distance = 0
        for i in range(0, len(next_generation)):
            end_avg_distance += self.repository.evaluation(next_generation[i])
        end_avg_distance = end_avg_distance / population_size

        ordered_next_generation = sorted(next_generation,
                                         key=lambda permuation: self.repository.evaluation(permuation),
                                         reverse=False)

        #print("Start avg distance: {}".format(start_avg_distance))
        #print("Start best distance: {}".format(self.repository.evaluation(ordered_population_pool[0])))
        #print("End avg distance: {}".format(end_avg_distance))
        #print("Current generation best distance: {}".format(self.repository.evaluation(ordered_population_pool[0])))
        #print('')

        self.update_best_so_far(deepcopy(ordered_next_generation[0]))
        #self.print_best_so_far()

        # Deallocate ordered next generation

        del ordered_next_generation[:]
        del ordered_next_generation

        return next_generation