###### implementing one max #########

from simple_genetic_algorithm import *

#objective function
def onemax(x):
    return -sum(x)

n_iter = 100
n_bits = 20
n_pop = 100
crossover_rate = 0.9
mutation_rate = 1.0 / n_bits

#genetic algorithm search
best, score = genetic_algorithm(onemax, n_bits, n_pop, n_iter, crossover_rate, mutation_rate)

print("Done!!")
print("f(%s) = %f" % (best, score))