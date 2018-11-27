# Package: tests.model_tests.startegies
# Description: tests of position class

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Mariana Rojas S. 
# E-mail: mari.semeraro27@gmail.com
# Version: 0.0.0 

# IMPORT SECTION
from model.strategies.position import Number

def test_increase_strategy():
    """ Check that increase_strategy function is working correctly
    """
    number = Number(1)
    strategy = 2
    strategy_false = 3
    number.increase_strategy(2)
    assert(strategy == number.strategies_number)
    assert(strategy_false != number.strategies_number)

def test_increase_amount():
    """ Check that increase_amount function is working correctly
    """
    number = Number(1)
    amount = 5
    amount_false = 3
    number.increase_amount(5)
    assert(amount == number.amount)
    assert(amount_false != number.amount)