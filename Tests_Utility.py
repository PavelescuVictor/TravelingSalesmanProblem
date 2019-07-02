import Utility
from SimulatedAnnealing import SimulatedAnnealing
# Tests Generate Random Permutation
print(Utility.generate_random_permutation(10))
print()


# Tests Rnd Number In Range
print(Utility.rnd_number(0,1))
print()


# Tests Neighbor
rnd_permutation = Utility.generate_random_permutation(10)
print(rnd_permutation)
print(Utility.generate_neighbour(rnd_permutation))
print()


# Tests acceptance probability