from model.genetics.genetics_algorithm import GeneticAlgorithm

def main():

    genetic = GeneticAlgorithm()
    strategies = genetic.get_winner_information()
    print(strategies)



if __name__ == "__main__":
    main()


