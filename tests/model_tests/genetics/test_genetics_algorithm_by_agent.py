# Package: tests.model_tests.startegies
# Description: Genetics Algorithm by agent tests

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina Sanchez 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION 

from model.genetics.genetics_algorithm_by_agent import GeneticAlgorithmByAgent
from model.genetics.individual_by_agent import IndividualByAgent
from model.game.agent import Agent
from config.config import Config as cf
from model.genetics.game_genetics import GameGenetics 
import random as rd
# Fake agents

agent_1 = Agent(1,2)
agent_2 = Agent(1,2)

test_individual = IndividualByAgent(agent_1)
test_individual_1 = IndividualByAgent(agent_2)

population = 10
generation = population
test_genetics = GeneticAlgorithmByAgent(population,generation)

array_stubs = []
array_real = []

# GET_RANDOM_PROBABILITIES_TEST--------------------------------

def test_get_random_probabilities():
    array_real.append(rd.random)
    rd.random = lambda: 0.80
    array_probabilities = [0.80,0.80,0.80,0.80]
    result_1 = test_genetics.get_random_probabilities()
    assert(result_1 == array_probabilities)
    rd.random = array_real.pop()

# INIT_POPULATION_TEST----------------------------------------

def test_init_population():
    array_real.append(GeneticAlgorithmByAgent.get_random_probabilities)
    GeneticAlgorithmByAgent.get_random_probabilities = lambda _: [0.80,0.80,0.80,0.80]
    population = 5 
    test_genetics.init_population(population)
    assert(len(test_genetics.population)== population)


# FITNESS_FUNCTION TEST-----------------------------------------------------------


def test_fitness_function_success():
    array_real.append(IndividualByAgent.fit_agent)
    array_real.append(IndividualByAgent.get_fitness_value)

    array_agent = [test_individual,test_individual_1]
    IndividualByAgent.fit_agent = lambda x,y: y
    IndividualByAgent.get_fitness_value = lambda _: 0.5
    
    test_genetics.population = array_agent
    result = test_genetics.fitness_function()

    assert(len(result)==2)
    assert(result[0]==(0.5,test_individual))

    IndividualByAgent.get_fitness_value = array_real.pop()
    IndividualByAgent.fit_agent = array_real.pop()


# CROSSOVER_FUNCTION---------------------------------------------------

def test_crossover_function_success():
    array_real.append(IndividualByAgent.crossover_agents)
    IndividualByAgent.crossover_agents = lambda x,y,z: [test_individual]
    test_genetics.population = [test_individual]
    test_genetics.next_population.clear()
    test_genetics.crossover_function(test_individual,0)
    assert(len(test_genetics.population)==0)
    assert(len(test_genetics.next_population)==1)
    assert(test_genetics.next_population[0]== test_individual)

    IndividualByAgent.crossover_agents = array_real.pop()


# GET WINNER INFORMATION------------------------------------------------

def test_get_winner_information():
    array_real.append(GeneticAlgorithmByAgent.crossover_function)
    array_real.append(GeneticAlgorithmByAgent.fitness_function)
    array_real.append(GeneticAlgorithmByAgent.get_winner_from_generation)

    GeneticAlgorithmByAgent.crossover_function = lambda x,y,z: test_individual
    GeneticAlgorithmByAgent.fitness_function = lambda _:[(0.6,test_individual),(0.5,test_individual_1)]
    GeneticAlgorithmByAgent.get_winner_from_generation = lambda _: "GOOD WINNER" 

    population  = [test_individual,test_individual_1]
    test_genetics.population = population
    test_genetics.generation = 1
    result = test_genetics.get_winner_information(1)

    assert(result == "GOOD WINNER")
    assert(len(test_genetics.population) == 1) # limit population
    assert(test_genetics.population[0]==test_individual) # select the best individual

    GeneticAlgorithmByAgent.get_winner_from_generation = array_real.pop()
    GeneticAlgorithmByAgent.fitness_function = array_real.pop()
    GeneticAlgorithmByAgent.crossover_function = array_real.pop()









    

    
