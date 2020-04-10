from GA import GA
from utils import Utils


def main():
    test_data = ["150p_eil51.txt", "50p_easy_01_tsp.txt", "50p_medium_01_tsp.txt", "50p_hard_01_tsp.txt",
                 "100p_fricker26.txt"]
    for file in test_data:
        print("STARTED THE NETWORK FROM FILE " + file + " \n")
        if file == "150p_eil51.txt":
            network = Utils.read_city(file)
        else:
            network = Utils.read_network(file)

        algorithm_properties = {
            'popSize': 50,
            'noGen': 100
        }

        parameters = {
            'fitness_function': Utils.modularity,
            'noNodes': network['noNodes'],
            'matrix': network['matrix']
        }

        ga = GA(algorithm_properties, parameters)
        best = None
        for g in range(algorithm_properties['noGen']):
            ga.apply_next_gen()
            bestChromo = ga.best_chromosome()
            worstChromo = ga.worst_chromosome()
            if best is None or best.fitness > bestChromo.fitness:
                best = bestChromo
            print('Best solution in generation ' + str(g) + ' is: x = ' + str(
                bestChromo.representation) + ' f(x) = ' + str(
                bestChromo.fitness))
            print(
                'Worst solution in generation ' + str(g) + ' is: x = ' + str(
                    worstChromo.representation) + ' f(x) = ' + str(
                    worstChromo.fitness))
            print()
        f = open(file + "_solution", "w")
        road = ""
        for gene in best.representation:
            road += str(gene) + " "
        f.write(str(len(best.representation)) + "\n" + road + "\n" + str(best.fitness))
        f.close()


main()
