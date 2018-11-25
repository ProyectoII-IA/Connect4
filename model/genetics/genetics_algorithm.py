# Package: model.genetics
# Description: Genetics algorithm 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4 
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION
from config.config import Config as cf 
from model.game.agent import Agent
from model.genetics.individual import Individual
import random as rd
import numpy as np


class GeneticAlgorithm:
    # fields-----------------
    population = []

    #Constructor-------------
    def __init__(self,population_a = cf.POPULATION_AMOUNT):
        self.init_population(population_a)

    #Methods-----------------
    # @Method:GET_RANDOM_PROBABILITIES
    # @Description: return an array of 4 of random probabilities
    # @return: array of float
    def get_random_probabilities(self):
        array_probabilities = []
        for index in range(4):
            new_probability = round(rd.random(),2)
            array_probabilities.append(new_probability)
        return array_probabilities
    # @Method:INIT_POPULATION
    # @Description: Initialize the first population with individual and random probabilities
    # @return: none
    def init_population(self,population_a):
        self.population.clear()
        for index in range(population_a):
            new_agent_1 = Agent(1,2)
            new_agent_2 = Agent(2,1)  
            new_agent_1.set_strategies(self.get_random_probabilities())
            new_agent_2.set_strategies(self.get_random_probabilities())
            new_individual =  Individual(new_agent_1,0,new_agent_2,0)
            self.population.append(new_individual)

    # @Method:GET_WINNER_FROM_GENERATION
    # @Description: select the best winner for the last population
    # @return: agent with best strategies
    def get_winner_from_generation(self):
        winner_individual = self.population[0]
        winner_individual.fit_agents()
        winner_agent = winner_individual.get_winner_agent()
        print(winner_agent[0].strategies)
        return winner_agent[0].strategies

    # @Method:CROSSOVER_FUNCTION
    # @Description: crossover of the last population
    # Example, the first individual is cross with the second best individual
    # @return: update population array 
    def crossover_function(self,individual_1):
        self.population.append(individual_1[0])
        self.population.append(individual_1[1])
        return individual_1

    # @Method:GET_WINNER_INFORMATION
    # @Description: generate a good winner using genetics algorithm 
    # @return: stretagies used for the best
    def get_winner_information(self):
        counter = cf.GENERATION_AMOUNT
        fitness_function = lambda x : (x.fit_agents(),x)
        clear_function = lambda x : x[1]
        crossover_function = lambda x,y : self.crossover_function(x.crossover(y))
        p_half = int(len(self.population)/2)
        while counter > 0 : 
            print("Generación:",counter)
            #FITNESS FUNCTION
            array_fitness = list(map(fitness_function,self.population))
            #SORT BY  BEST WINNER
            sorted_fitness = sorted(array_fitness,key=lambda x: x[0],reverse=True)
            #CLEAR SORTED ARRAY
            sorted_fitness = list(map(clear_function,sorted_fitness))
            # CROSSOVER THE FIRST MIDDLE OF POPULATION
            #self.crossover_function(sorted_fitness)
            self.population.clear()
            list(map(crossover_function,sorted_fitness[:p_half], sorted_fitness[1:p_half+1]))
            counter-=1
        return self.get_winner_from_generation()


        
            
