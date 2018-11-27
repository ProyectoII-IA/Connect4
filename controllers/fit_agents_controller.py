# Package: model.game
# Description: structure of board

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Jonathan Martinez C.
# E-mail: jonathan.gerad@hotmail.com
# Version: 0.0.0

# IMPORT SECTION
import argparse
from model.genetics.genetics_algorithm_by_agent import GeneticAlgorithmByAgent
from model.genetics.genetics_algorithm import GeneticAlgorithm


class Fit_Agents_Controller():

    def __init__(self):
        self.population = 0
        self.generations = 0
        self.limiter = 0
        self.mutation = 0
        self.config_agents()
        #self.genectic2 = GeneticAlgorithm()

    # Methods-------------------------
    # @Method: GET_CONFIG
    # @Description: Return the configurations of population, generations,
    #               limiter and mutation
    def get_config(self):
        return [self.population, self.generations, self.limiter, self.mutation]

    # Methods-------------------------
    # @Method: CONFIG_AGENTS
    # @Description: Take the values from console and parse the values of
    #               generations and generation_survivor
    def config_agents(self):
        parser = argparse.ArgumentParser(description='Configuración del ' +
                                                     'Algoritmo Genético.')
        parser.add_argument("-p", "--population", type=int,
                            help="Define la población inicial")
        parser.add_argument("-g", "--generations", type=int,
                            help="Cantidad de generaciones")
        parser.add_argument("-l", "--limiter", type=int,
                            help="Cantidad de individuos que pasan de una población a otra")
        parser.add_argument("-m", "--mutation", type=float,
                            help="Define la probabilidad de mutación")
        args = parser.parse_args()
        self.population = args.population
        self.generations = args.generations
        self.limiter = args.limiter
        self.mutation = args.mutation

    def get_agent(self):
        parameters = self.get_config()
        self.genectic1 = GeneticAlgorithmByAgent(parameters[0],parameters[1])
        print('"'+ str(self.genectic1.get_winner_information(parameters[2],parameters[3])) + '"')
