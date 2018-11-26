# Package: model.genetics
# Description: 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4 
# Author : Katerine Molina S. 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION
from config.config import Config as cf 
from model.genetics.game_genetics import GameGenetics
from model.game.agent import Agent
import random as rd
import numpy as np
import itertools

 

class IndividualByAgent:
    #Fields----------------------
    agent = ""
    won_games = 0
    total_games  = 0
    
    #Constructor-----------------
    def __init__(self,agent1):
        self.agent = agent1 # first 0 represents each win time the second amount of wins
        won_game = 0

    #Methods---------------------


    # @Method:MUTATION_CROSSOVER
    # @Description: cross the individual with another when mutation was activated
    # @return: two individuals instance
    def mutate_agent(self):
        probabilities = self.agent.strategies
        strategy  =  rd.randint(0,3) # Choose 1 strategy to change
        probabilities[strategy] = probabilities[strategy]+cf.MUTATION_AMOUNT 
        return self.agent.set_strategies(probabilities)

    def get_won_games_agent(self,agent,agent_opp,counter=cf.WON_GAMES_LOOP): # for getting winner
        won_games = 0 
        tie_games = 0
        agent.set_symbols(1,2)
        agent_opp.set_symbols(2,1)
        while counter > 0:
            game = GameGenetics(agent,agent_opp)
            winner = game.play_game()
            if winner == cf.WINNER_1:
                won_games+=1
            elif winner ==cf.TIE:
                tie_games+=1
            counter-=1
        return won_games,tie_games

    # @Method:GET_FIRST_BEST_AGENT
    # @Description: Get the first combination that won his parents
    # @return: Individual object
    def get_first_best_agent(self,agent_possibilities,agent_cross,min_games = cf.MIN_GAMES):
        for strategies in agent_possibilities:
            agent = Agent(1,2,True)
            agent.strategies =list(strategies)
            #parent 1
            game_1,ties = self.get_won_games_agent(agent,self.agent)
            game_2,ties = self.get_won_games_agent(agent,agent_cross.agent)
            if game_1>=min_games and game_2>=min_games:
                return IndividualByAgent(agent)
        # If doesn't exist any good agent  return any parent
        if self.won_games >= agent_cross.won_games:
            return IndividualByAgent(self.agent)
        else:
            return IndividualByAgent(agent_cross.agent1)

    # @Method:SIMPLE_CROSSOVER
    # @Description: cross the individual with another getting the winners first and the loser in separeted individuals
    # @return: two individuals instance
    def simple_crossover(self,agent_cross,optimal=False):
        probabilities_1 = self.agent.strategies
        probabilities_2 = agent_cross.agent.strategies
        agent_possibilities = list(itertools.product(probabilities_1,probabilities_2,probabilities_1,probabilities_2))
        rd.shuffle(agent_possibilities)
        agent_possibilities = agent_possibilities[:cf.CROSSOVER_LIMITER] 
        #agent_possibilities = np.array(np.meshgrid(probabilities_1,probabilities_2))
        if not optimal:
            return self.get_first_best_agent(agent_possibilities,agent_cross)
        #else:
         #   return self.get_optimal_best_agent(agent_possibilities)
    
    def crossover_agents(self,array_agent,mutation=cf.MUTATION_PROBABILITY):
        array_child = []
        for agent in array_agent:
            array_child.append(self.crossover(agent,mutation))
        return array_child   


    # @Method:CROSSOVER
    # @Description: cross the individual with another 
    # @return: two individuals instance  
    def crossover(self,agent_cross,mutation_probability= cf.MUTATION_PROBABILITY,optimal =False):
        if agent_cross == None:
            return self
        new_individual = self.simple_crossover(agent_cross,optimal)
        if mutation_probability  > self.get_random_number(): # random return 0 to 0.99 number
            new_individual.mutate_agent()
            return new_individual
        else:
            return new_individual
    
    # @Method:FIT_AGENTS
    # @Description: fit both agents getting the best winner
    # @return: win percent 
    def fit_agent(self,array_agent):
        for agent in array_agent:
            winner,ties = self.get_won_games_agent(self.agent,agent.agent,1)
            if winner == 1:
                self.won_games +=1 
            elif ties <= 0:
                agent.won_games +=1
            agent.total_games+=1
            self.total_games+=1 
        return array_agent

    def get_fitness_value(self):
        return self.won_games/self.total_games

    # @Method:To_String
    # @Description: print agents information
    # @return: string 
    def to_string(self):
        return "Agent" + str(self.agent.strategies)
    

    def get_random_number(self):
        return rd.random()
            



    
