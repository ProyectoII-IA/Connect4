# Package: tests.model_tests.startegies
# Description: Genetics Algorithml tests 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina Sanchez 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION 

from model.genetics.genetics_algorithm import GeneticAlgorithm
from model.genetics.individual import Individual
from model.game.agent import Agent
from config.config import Config as cf
from model.genetics.game_genetics import GameGenetics 
import random as rd
# Fake agents

agent_1 = ["agent1",0,1]
agent_2 = ["agent2",0,2]

test_individual = Individual("agent1",0,"agent2",0)
test_individual_1 = Individual("agent1_1",0,"agent2_1",0)

population = 10
test_genetics = GeneticAlgorithm(population)

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
    array_real.append(GeneticAlgorithm.get_random_probabilities)
    GeneticAlgorithm.get_random_probabilities = lambda _: [0.80,0.80,0.80,0.80]
    population = 5 
    test_genetics.init_population(population)
    assert(len(test_genetics.population)== population)


#GET_WINNER_FROM_GENERATION TEST------------------------------

def test_get_winner_generation():
    array_real.append(Individual.fit_agents)
    array_real.append(Individual.get_winner_agent)
    #Fake agent
    agent = Agent(1,2)
    agent.strategies = "STRATEGIES" 
    # Change functions
    Individual.fit_agents = lambda _: 1
    Individual.get_winner_agent = lambda _: [agent,0,0]

    test_genetics.population[0] = Individual(agent,0,agent,0)
    result = test_genetics.get_winner_from_generation()
    assert(result=="STRATEGIES" )

    #recovery methods
    Individual.get_winner_agent = array_real.pop()
    Individual.fit_agents = array_real.pop()

# GET_WINNER_INFORMTION-------------------------------

def test_get_winner_information():
    array_real.append(Individual.fit_agents)
    array_real.append(Individual.crossover)
    array_real.append(GeneticAlgorithm.get_winner_from_generation)
    array_real.append(GeneticAlgorithm.crossover_function)
    temp_config = cf.GENERATION_AMOUNT

    Individual.fit_agents = lambda _: 1
    Individual.crossover = lambda x,y: x
    GeneticAlgorithm.get_winner_from_generation = lambda _: "WINNER"
    GeneticAlgorithm.crossover_function = lambda x,y: "Agent"
    cf.GENERATION_AMOUNT = 1 

    test_genetics.init_population(5)
    result = test_genetics.get_winner_information()

    assert(result == "WINNER")

    GeneticAlgorithm.crossover_function = array_real.pop()
    GeneticAlgorithm.get_winner_from_generation = array_real.pop()
    Individual.crossover = array_real.pop()
    Individual.fit_agents = array_real.pop()
    cf.GENERATION_AMOUNT = temp_config


# CROSSOVER_FUNCTION_TEST------------------------------------

def test_crossover_function():

    test_genetics.population.clear()
    test_genetics.crossover_function(("individual1","individual2"))

    assert(test_genetics.population[0]=="individual1")
    assert(test_genetics.population[1]=="individual2")
    assert(len(test_genetics.population)==2)









    

    
