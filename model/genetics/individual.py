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
import random as rd

 

class Individual:
    #Fields----------------------
    agent_1 = ""
    agent_2 = ""
    
    #Constructor-----------------
    def __init__(self,agent1,agent1_wins,agent2,agent2_wins):
        self.agent_1 = [agent1,0,agent1_wins] # first 0 represents each win time the second amount of wins
        self.agent_2 = [agent2,0,agent2_wins]

    #Methods---------------------

    # tools methods--------------
    def get_winner_agent(self):
        if self.agent_1[1] > self.agent_2[1]:
            return self.agent_1
        else:
            return self.agent_2

    def get_loser_agent(self):
        if self.agent_1[1] <= self.agent_2[1]:
            return self.agent_1
        else:
            return self.agent_2

    # @Method:MUTATION_CROSSOVER
    # @Description: cross the individual with another when mutation was activated
    # @return: two individuals instance
    def mutation_crossover(self,agent_winner_1,agent_winner_2,agent_loser_1,agent_loser_2):
        new_individual_1 = Individual(agent_winner_1[0],agent_winner_1[2]+agent_winner_1[1],agent_loser_2[0],agent_loser_2[2]+agent_loser_2[1])
        new_individual_2 = Individual(agent_winner_2[0],agent_winner_2[2]+agent_winner_2[1],agent_loser_1[0],agent_loser_1[2]+agent_loser_1[1])
        return new_individual_1,new_individual_2

    # @Method:SIMPLE_CROSSOVER
    # @Description: cross the individual with another getting the winners first and the loser in separeted individuals
    # @return: two individuals instance
    def simple_crossover(self,agent_winner_1,agent_winner_2,agent_loser_1,agent_loser_2):
        new_individual_1 = Individual(agent_winner_1[0],agent_winner_1[2]+agent_winner_1[1] ,agent_winner_2[0],agent_winner_2[2]+agent_winner_2[1])
        new_individual_2 = Individual(agent_loser_1[0],agent_loser_1[2]+agent_loser_1[1],agent_loser_2[0],agent_loser_2[2]+agent_loser_2[1])
        return new_individual_1,new_individual_2

    # @Method:CROSSOVER
    # @Description: cross the individual with another 
    # @return: two individuals instance  
    def crossover(self,individual_2):
        agent_winner_1 = self.get_winner_agent()
        agent_winner_2 = individual_2.get_winner_agent()
        agent_loser_1  = self.get_loser_agent()
        agent_loser_2  = individual_2.get_loser_agent()
        if cf.MUTATION_PROBABILITY > self.get_random_number(): # random return 0 to 0.99 number
            return self.mutation_crossover(agent_winner_1,agent_winner_2,agent_loser_1,agent_loser_2)
        else:
            return self.simple_crossover(agent_winner_1,agent_winner_2,agent_loser_1,agent_loser_2)
    
    # @Method:FIT_AGENTS
    # @Description: fit both agents getting the best winner
    # @return: win percent 
    def fit_agents(self):
        counter = cf.FIT_LOOP
        while counter > 0:
            game = GameGenetics(self.agent_1[0],self.agent_2[0])
            winner = game.play_game()
            if winner == cf.WINNER_1:
                self.agent_1[1] += 1
            elif winner == cf.WINNER_2:
                self.agent_2[1] += 1
            else: # TIE means Both agents are good
                self.agent_1[1]+=1
                self.agent_2[1]+=1
            counter-=1 
        max_winner = max(self.agent_1[1],self.agent_2[1])
        return max_winner/cf.FIT_LOOP

    # @Method:To_String
    # @Description: print agents information
    # @return: string 
    def to_string(self):
        return "Agent 1" + str(self.agent_1[0].strategies)+" Agent 2 "+ str(self.agent_2[0].strategies)
    

    def get_random_number(self):
        return rd.random()
            



    
