from model.genetics.genetics_algorithm import GeneticAlgorithm
from model.genetics.genetics_algorithm_by_agent import GeneticAlgorithmByAgent
from datetime import datetime
def main():

    """ genetic = GeneticAlgorithm()
    strategies = genetic.get_winner_information()
    print(strategies) """

    genetic = GeneticAlgorithmByAgent(10,5) # Population
    strategies = genetic.get_winner_information(5,0.10) #limiter and mutation probability
    print(strategies)

if __name__ == "__main__":
    main()


