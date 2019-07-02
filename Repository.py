from Classes.City import City
from math import sqrt

class Repository:

    def __init__(self):
        self.repo_storage = []
        self.repo_size = 0
        self.repo_distance_matrix = []

    def add_city(self, city):
        self.repo_storage.append(city)

    def set_repo_size(self, size):
        self.repo_size = size

    def create_distance_matrix(self):
        for i in range(0, int(self.repo_size)):
            row = []
            for j in range(i + 1, int(self.repo_size)):
                row.append(self.distance_between_two_cities(self.get_element_by_index(i), self.get_element_by_index(j)))
            self.repo_distance_matrix.append(row)

    def evaluation(self, permutation):
        total_distance = 0
        #print(permutation)
        for i in range(0, len(permutation)):
            if i == len(permutation) - 1:
                firs_city_index = permutation[i]
                second_city_index = permutation[0]
            else:
                firs_city_index = permutation[i]
                second_city_index = permutation[i + 1]
            #print("{} -- {}".format(firs_city_index, second_city_index))
            a = self.get_element_by_index(firs_city_index - 1)
            b = self.get_element_by_index(second_city_index - 1)
            if firs_city_index < second_city_index:
                distance = self.repo_distance_matrix[firs_city_index - 1][second_city_index - firs_city_index - 1]
                #print("City a:{} -- City b:{} -- Row:{} -- Column:{} -- Distance:{}".format(firs_city_index, second_city_index, firs_city_index, second_city_index - firs_city_index, round(distance, 2)))
            else:
                distance = self.repo_distance_matrix[second_city_index - 1][firs_city_index - second_city_index - 1]
                #print("City a:{} -- City b:{} -- Row:{} -- Column:{} -- Distance:{}".format(firs_city_index, second_city_index, second_city_index, firs_city_index - second_city_index, round(distance, 2)))
            total_distance = total_distance + distance
        return total_distance


    def distance_between_two_cities(self, a, b):
        return sqrt((b.get_xcoord() - a.get_xcoord())**2 + (b.get_ycoord() - a.get_ycoord())**2)

    def get_element_by_index(self, index):
        return self.repo_storage[index]

    def get_repo_storage(self):
        return self.repo_storage

    def get_repo_size(self):
        return self.repo_size

    def get_repo_distance_matrix(self):
        return self.repo_distance_matrix