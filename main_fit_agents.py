# Package: 
# Description: Main of the fit agents

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Authors : Jonathan Martinez C., Katherine Molina S., Mariana Rojas Semeraro
# E-mail: jonathan.gerad@hotmail.com, kanatalia95@gmail.com, mari.semeraro27@gmail.com
# Version: 0.0.0

# IMPORT SECTION
from controllers.fit_agents_controller import Fit_Agents_Controller
from datetime import datetime


<<<<<<< HEAD
def main():
    controller = Fit_Agents_Controller()
    controller.get_agent()
=======
    genetic = GeneticAlgorithmByAgent(10,1) # Population
    strategies = genetic.get_winner_information(5,0.10) #limiter and mutation probability
    print(strategies)
>>>>>>> 0e2edc295cf7ecf06ffc5ded5da950eb93a03829

if __name__ == "__main__":
    main()


