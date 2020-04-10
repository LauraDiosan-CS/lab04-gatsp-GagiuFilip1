from random import randint


def generate_permutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


class Chromosome:
    def __init__(self, parameters=None):
        self.__parameters = parameters
        self.__representation = generate_permutation(
            self.__parameters['noNodes'])  # generate random chromosome which will contain each node id
        self.__fitness = 0.0

    @property
    def representation(self):
        return self.__representation

    @property
    def fitness(self):
        return self.__fitness

    @representation.setter
    def representation(self, value=None):
        if value is None:
            value = []
        self.__representation = value

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, second_chromosome):
        pos1, pos2 = self.get_random_ordered_positions()
        k = 0
        new_representation = self.__representation[pos1: pos2]
        for el in second_chromosome.__representation[pos2:] + second_chromosome.__representation[:pos2]:
            if el not in new_representation:
                if len(new_representation) < self.__parameters['noNodes'] - pos1:
                    new_representation.append(el)
                else:
                    new_representation.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__parameters)
        offspring.representation = new_representation
        return offspring

    def mutation(self):
        # insert mutation
        pos1, pos2 = self.get_random_ordered_positions()
        el = self.__representation[pos2]
        del self.__representation[pos2]
        self.__representation.insert(pos1 + 1, el)

    def get_random_ordered_positions(self):
        pos1 = randint(0, self.__parameters['noNodes'] - 1)
        pos2 = randint(0, self.__parameters['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        return pos1, pos2

    def __str__(self):
        return "\nChromosome: " + str(self.__representation) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__representation == c.__repres and self.__fitness == c.__fitness

    def __lt__(self, other):
        return self.fitness < other.fitness
