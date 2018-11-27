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
        self.generations = 0
        self.generation_survivor = 0
        self.config_agents()
        #self.genectic2 = GeneticAlgorithm()

    # Methods-------------------------
    # @Method: GET_CONFIG
    # @Description: Return the configurations of generations and
    #               generation_survivor take from console
    def get_config(self):
        return [self.generations, self.generation_survivor]

    # Methods-------------------------
    # @Method: CONFIG_AGENTS
    # @Description: Take the values from console and parse the values of
    #               generations and generation_survivor
    def config_agents(self):
        parser = argparse.ArgumentParser(description='Configuración del ' +
                                                     'Algoritmo Genético.')
        parser.add_argument("-ge", "--generations", type=int,
                            help="Define la cantidad de generaciones")
        parser.add_argument("-gs", "--generation-survivor", type=int,
                            help="Cantidad de sobrevivientes por generación")
        args = parser.parse_args()
        self.generations = args.generations
        self.generation_survivor = args.generation_survivor

    def get_agent(self):
        parameters = self.get_config()
        self.genectic1 = GeneticAlgorithmByAgent(parameters[0],parameters[1])
