from Repository import Repository
from Classes.City import City
import random
from math import exp
import numpy

def read_from_file(file_name, repo):
    try:
        file = open(file_name, "r")
    except:
        print("There is no file %s" % file_name)
    else:
        file_content = file.read().splitlines()
        size = list(map(str, file_content[3].split()))[1]
        repo = Repository()
        repo.set_repo_size(size)
        for i in range(6, int(size) + 6):
            line_content = list(map(float, file_content[i].split()))
            value = line_content[1]
            weight = line_content[2]
            item = City(value, weight)
            repo.add_city(item)
        repo.create_distance_matrix()
        file.close()
        return repo

def print_distance_matrix(repo):
    indexi = 1
    for i in repo.get_repo_distance_matrix():
        string = ''
        indexj = indexi + 1
        for j in i:
            string = string + str(j) + "({},{})".format(str(indexi), str(indexj)) + "       "
            indexj = indexj + 1
        indexi = indexi + 1
        print(string)

def generate_random_permutation(size):
    return random.sample(range(1, int(size) + 1), int(size))

def acceptance_probability(delta, temp):
    e = numpy.exp(1)
    prob = e**((-delta)/temp)
    return prob

def rnd_number(start, end):
    return random.uniform(start, end)

def generate_neighbour(permutation):
    rnd_val1 = random.randint(0, len(permutation) - 1)
    rnd_val2 = random.randint(0, len(permutation) - 1)
    aux = permutation[rnd_val1]
    permutation[rnd_val1] = permutation[rnd_val2]
    permutation[rnd_val2] = aux
    return permutation
