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
from model.genetics.individual_by_agent import IndividualByAgent
import random as rd
import numpy as np
import copy
from datetime import datetime


class GeneticAlgorithmByAgent:
    # fields-----------------
    population = []

    #Constructor-------------
    def __init__(self,population_a = cf.POPULATION_AMOUNT,generation=cf.GENERATION_AMOUNT):
        self.init_population(population_a)
        self.generation = generation
        self.next_population = []

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
            new_agent = Agent(1,2)
            new_agent.set_strategies(self.get_random_probabilities())
            new_individual =  IndividualByAgent(new_agent)
            self.population.append(new_individual)

    # @Method:GET_WINNER_FROM_GENERATION
    # @Description: select the best winner for the last population
    # @return: agent with best strategies
    def get_winner_from_generation(self):
        if len(self.population)==2:
            winner = self.population[0].fit_agent([self.population[1]])
            if winner==0:
                return self.population[1].agent.strategies
        return self.population[0].agent.strategies

    # @Method:FITNESS_FUNCTION
    # @Description: apply the fitness function to all elements in the population
    # @return: agent fitness value
    def fitness_function(self):
        len_pop = len(self.population)
        for index in range(len_pop):
            individual = self.population[index]
            self.population[index+1:] = individual.fit_agent(self.population[index+1:])
        fitness_function = lambda x : (x.get_fitness_value(),x)
        array_fitness = list(map(fitness_function,self.population))
        return array_fitness

    def crossover_function(self,agent,mutation):
        self.population.remove(agent)
        self.next_population += agent.crossover_agents(self.population,mutation)
    
    # @Method:GET_WINNER_INFORMATION
    # @Description: generate a good winner using genetics algorithm 
    # @return: strategies used for the best 
    def get_winner_information(self, limiter=cf.LIMITER,mutation=cf.MUTATION_PROBABILITY,optimal=False):
        start_time = datetime.now()
        print('Initial Time: {}'.format(start_time))
        counter = self.generation
        clear_function = lambda x : x[1]
        crossover_function = lambda x : self.crossover_function(x,mutation)
        while counter > 0:
            #CROSSOVER POPULATION 
            print("Crossing population: ",counter)      
            self.next_population.clear()
            list(map(crossover_function,self.population))
            self.population.clear()
            self.population = self.next_population
            crossing_time = datetime.now()
            print('Duration: {}'.format(crossing_time - start_time))
            #FITNESS FUNCTION
            print("Applying Fitness Function: ",counter)     
            array_fitness = self.fitness_function()
            #SORT BY  BEST WINNER
            sorted_fitness = sorted(array_fitness,key=lambda x: x[0],reverse=True)
            #CLEAR SORTED ARRAY
            sorted_fitness = list(map(clear_function,sorted_fitness))
            end_time = datetime.now()
            print('Duration: {}'.format(end_time - crossing_time))
            #Limit next generation
            print("Limiting population: ",counter)     
            self.population =sorted_fitness[:limiter]
            counter-=1
        end_time = datetime.now()
        print('Total Time: {}'.format(end_time - start_time))
        return self.get_winner_from_generation()


        
            
