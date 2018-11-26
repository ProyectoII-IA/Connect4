
class Config:
    #Genetics configuration 
    MUTATION_PROBABILITY = 0.10
    FIT_LOOP = 4
    POPULATION_AMOUNT = 100
    GENERATION_AMOUNT = 10

    MUTATION_AMOUNT =  0.05 #increase in the case of mutation 
    LIMITER = 100 
    CROSSOVER_LIMITER = 200

    WON_GAMES_LOOP = 1 #use only odd number to avoid ties
    MIN_GAMES = 1

    #genetics flags
    WINNER_1 = 1
    WINNER_2 = 2
    TIE = 0

    #strategies flags
    SEQUENTIAL = 0
    CENTER = 1 
    HORIZONTAL = 2
    BLOCKING2 = 3