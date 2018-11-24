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

 
    def __init__(self,population_a = cf.POPULATION_AMOUNT):
        self.init_population(population_a)

    def get_random_probabilities(self):
        array_probabilities = []
        for index in range(4):
            new_probability = round(rd.random(),2)
            array_probabilities.append(new_probability)
        return array_probabilities

    def init_population(self,population_a):
        for index in range(population_a):
            new_agent_1 = Agent(1,2)
            new_agent_2 = Agent(2,1)  
            new_agent_1.set_strategies(self.get_random_probabilities())
            new_agent_2.set_strategies(self.get_random_probabilities())
            new_individual =  Individual(new_agent_1,0,new_agent_2,0)
            self.population.append(new_individual)

    def get_winner_from_generation(self):
        winner_individual = self.population[0]
        winner_individual.fit_agents()
        winner_agent = winner_individual.get_winner_agent()
        print(winner_agent[0].strategies)
        return winner_agent[0].strategies
   
    def crossover_function(self,sorted_array):
        p_length_half = int(cf.POPULATION_AMOUNT/2) # Only select the first middle of array
        # Clear Population variable
        self.population.clear()
        array_1 = sorted_array[:p_length_half]
        array_2 = sorted_array[1:p_length_half+1]
        for individual_1,individual_2 in zip(array_1,array_2):
            (new_ind_1, new_ind_2) = individual_1.crossover(individual_2)
            self.population.append(new_ind_1)
            self.population.append(new_ind_2)
        
    
    def get_winner_information(self):
        counter = cf.GENERATION_AMOUNT
        fitness_function = lambda x : (x.fit_agents(),x)
        clear_function = lambda x : x[1]
        while counter > 0 : 
            print("Generación:",counter)
            for i in self.population:
                print(i.to_string())
            print("----------------------------")
            #FITNESS FUNCTION
            array_fitness = list(map(fitness_function,self.population))
            #SORT BY  BEST WINNER
            sorted_fitness = sorted(array_fitness,key=lambda x: x[0],reverse=True)
            #CLEAR SORTED ARRAY
            sorted_fitness = list(map(clear_function,sorted_fitness))
            # CROSSOVER THE FIRST MIDDLE OF POPULATION
            self.crossover_function(sorted_fitness)
            counter-=1
            
        return self.get_winner_from_generation()


        
            
