from numpy.random import randint
from numpy.random import rand


#no. of candidates in a population
n_pop = 0

#no. of bits in single sol.
n_bits = 0

#no. of iterations/generations
n_iter = 0

#crossover hyperparam
crossover_rate = 0

#mutation hyperparam
mutation_rate = 0


def objective(candidate):
    pass

#tournament selection
def selection(pop, scores, k = 3):
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k - 1):
        if scores[ix] < scores[selection_ix]:
            selection_ix  = ix
    
    return pop[selection_ix]

#crossover where two parents create two children
def crossover(p1, p2, crossover_rate):
    c1, c2 = p1.copy(), p2.copy()

    if rand() < crossover_rate:
        pt = randint(1, len(p1) - 2)
        
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]

    return [c1, c2]

#mutation(flipping bits) of candidates
def mutation(bitstring, mutation_rate):
    for i in range(len(bitstring)):
        if rand() < mutation_rate:
            bitstring[i] = 1 - bitstring[i] #flips bit
    



def genetic_algorithm(objective, n_bits, n_pop, n_iter, crossover_rate, mutation_rate):

    #initial population
    pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)] #population

    #keep track of best evaluation
    best, best_eval = 0, objective(pop[0])

    for gen in range(n_iter):
        #evaluate all candidates in the population
        scores = [objective(c) for c in pop]

        #check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print("->GEN: %d, new_best f(%s) = %.3f" % (gen, pop[i], scores[i]))
        
        #parents selection
        selected = [selection(pop, scores) for _ in range(n_pop)]

        #creating next generations
        children = list()

        for i in range(0, n_pop, 2):
            # get selected parents
            p1, p2 = selected[i], selected[i+1]

            #crossover and mutation
            for c in crossover(p1, p2, crossover_rate):
                #mutation
                mutation(c, mutation_rate)

                #storing for next generations
                children.append(c)
        
        #replace population
        pop = children

    return [best, best_eval]

###### implementing one max #########

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