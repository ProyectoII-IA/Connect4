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


def main():
    controller = Fit_Agents_Controller()
    controller.get_agent()

if __name__ == "__main__":
    main()


