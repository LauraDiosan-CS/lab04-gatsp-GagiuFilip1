import copy
import heapq
from random import randint

from Chromosome import Chromosome


class GA:
    def __init__(self, parameters, problem_parameters):
        self.parameters = parameters
        self.problem_parameters = problem_parameters
        self.population = heapq
        self.initialize_population()
        self.set_fitness_values()

    def initialize_population(self):
        chromosomes = []
        for _ in range(self.parameters['popSize']):
            chromosomes.append(Chromosome(self.problem_parameters))
        heapq.heapify(chromosomes)
        self.population = chromosomes

    def set_fitness_values(self):
        new_chromosomes = []
        for _ in range(self.parameters['popSize']):
            chromosome = heapq.heappop(self.population)
            chromosome.fitness = self.problem_parameters['fitness_function'](chromosome.representation,
                                                                             self.problem_parameters)
            new_chromosomes.append(chromosome)
        heapq.heapify(new_chromosomes)
        self.population = new_chromosomes

    def best_chromosome(self):
        return heapq.heappop(copy.copy(self.population))

    def worst_chromosome(self):
        best = self.best_chromosome()
        aux = copy.copy(self.population)
        for _ in range(self.parameters['popSize']):
            chromosome = heapq.heappop(aux)
            if chromosome.fitness > best.fitness:
                best = chromosome
        return best

    def get_chromosome_at_position(self, position):
        auxiliary = copy.copy(self.population)
        for i in range(self.parameters['popSize']):
            chromosome = heapq.heappop(auxiliary)
            if position == i:
                return chromosome

    def selection_function(self):
        pos1 = randint(0, self.parameters['popSize'] - 1)
        pos2 = randint(0, self.parameters['popSize'] - 1)
        if self.get_chromosome_at_position(pos1).fitness < self.get_chromosome_at_position(pos2).fitness:
            return pos1
        else:
            return pos2

    def apply_next_gen(self):
        new_population = []
        heapq.heapify(new_population)
        for _ in range(self.parameters['popSize']):
            p1 = self.get_chromosome_at_position(self.selection_function())
            p2 = self.get_chromosome_at_position(self.selection_function())
            off = p1.crossover(p2)
            off.mutation()
            heapq.heappush(new_population, off)

        self.population = new_population
        self.set_fitness_values()
