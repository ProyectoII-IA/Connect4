# Package: tests.model_tests.startegies
# Description: Individual tests 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina Sanchez 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION 

from model.genetics.individual import Individual

# Fake agents

agent_1 = ["agent1",0,1]
agent_2 = ["agent2",0,2]

test_individual = Individual("agent1",0,"agent2",0)
test_individual_1 = Individual("agent1_1",0,"agent2_1",0)

def test_initialize_individual():
    individual = Individual(agent_1[0],1,agent_2[0],2)
    assert(individual.agent_1==agent_1)
    assert(individual.agent_2==agent_2)

# GET WINNER AGENT TESTS------------------------------------------
def test_get_winner_agent_1():
    agent_1[1] = 4
    agent_2[1] = 2
    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2
    test_result = test_individual.get_winner_agent()
    assert(test_result == agent_1)

def test_get_winner_agent_2():
    agent_1[1] = 2
    agent_2[1] = 4
    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2
    test_result = test_individual.get_winner_agent()
    assert(test_result == agent_2)

def test_get_winner_agent_tie():
    agent_1[1] = 2
    agent_2[1] = 2
    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2
    test_result = test_individual.get_winner_agent()
    assert(test_result == agent_2) 

# GET LOSER AGENT TESTS------------------------------------------
def test_get_loser_agent_1():
    agent_1[1] = 2
    agent_2[1] = 4
    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2
    test_result = test_individual.get_loser_agent()
    assert(test_result == agent_1)

def test_get_loser_agent_2():
    agent_1[1] = 4
    agent_2[1] = 2
    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2
    test_result = test_individual.get_loser_agent()
    assert(test_result == agent_2)

def test_get_loser_agent_tie():
    agent_1[1] = 2
    agent_2[1] = 2
    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2
    test_result = test_individual.get_loser_agent()
    assert(test_result == agent_1) 

# MUTATION CROSSOVER TESTS------------------------------------------

def test_mutation_crossover():
    agent_winner = ["agent1",2,0]
    agent_loser  = ["agent2",1,0]
    agent_winner_1 = ["agent1",1,0]
    agent_loser_1 = ["agent2",0,0]
    result1, result2 = test_individual.mutation_crossover(agent_winner,agent_winner_1,agent_loser,agent_loser_1)
    agent_winner = ["agent1",0,2]
    agent_loser  = ["agent2",0,1]
    agent_winner_1 = ["agent1",0,1]
    agent_loser_1 = ["agent2",0,0]
    #crossover mutation 
    test_individual.agent_1 = agent_winner
    test_individual.agent_2 = agent_loser_1
    test_individual_1.agent_1 = agent_winner_1
    test_individual_1.agent_2 = agent_loser
    assert (result1.agent_1 == test_individual.agent_1)
    assert (result1.agent_2 == test_individual.agent_2)
    assert (result2.agent_1 == test_individual_1.agent_1)
    assert (result2.agent_2 == test_individual_1.agent_2)

# SIMPLE CROSSOVER TESTS------------------------------------------

def test_simple_crossover():
    agent_winner = ["agent1",2,0]
    agent_loser  = ["agent2",1,0]
    agent_winner_1 = ["agent1",1,0]
    agent_loser_1 = ["agent2",0,0]
    result1, result2 = test_individual.simple_crossover(agent_winner,agent_winner_1,agent_loser,agent_loser_1)
    agent_winner = ["agent1",0,2]
    agent_loser  = ["agent2",0,1]
    agent_winner_1 = ["agent1",0,1]
    agent_loser_1 = ["agent2",0,0]
    #crossover simple winner with winner
    test_individual.agent_1 = agent_winner
    test_individual.agent_2 = agent_winner_1
    test_individual_1.agent_1 = agent_loser
    test_individual_1.agent_2 = agent_loser_1
    assert (result1.agent_1 == test_individual.agent_1)
    assert (result1.agent_2 == test_individual.agent_2)
    assert (result2.agent_1 == test_individual_1.agent_1)
    assert (result2.agent_2 == test_individual_1.agent_2)


# CROSSOVER TESTS------------------------------------------

array_stubs = []
array_real = []

def create_crossover_stubs(agent_winner,agent_loser,probability):
    # Functions stubs
    get_winner_stub = lambda _: agent_winner
    array_stubs.append(get_winner_stub)
    get_winner_real = Individual.get_winner_agent
    array_real.append(get_winner_real)

    get_loser_stub = lambda _: agent_loser
    array_stubs.append(get_loser_stub)
    get_loser_real = Individual.get_loser_agent
    array_real.append(get_loser_real)

    get_random_stub = lambda _: probability
    array_stubs.append(get_random_stub)
    get_random_real = Individual.get_random_number
    array_real.append(get_random_real)

    get_simple_stub = lambda a,b,c,d,e: "SIMPLE_CROSSOVER"
    array_stubs.append(get_simple_stub)
    get_simple_real = Individual.simple_crossover
    array_real.append(get_simple_real)

    get_mutation_stub = lambda a,b,c,d,e: "MUTATION_CROSSOVER"
    array_stubs.append(get_mutation_stub)
    get_mutation_real = Individual.mutation_crossover
    array_real.append(get_mutation_real)
    return array_stubs,array_real

def recovery_crossover_methods(array_real):
    Individual.mutation_crossover = array_real.pop()
    Individual.simple_crossover = array_real.pop()
    Individual.get_random_number = array_real.pop()
    Individual.get_loser_agent = array_real.pop()
    Individual.get_winner_agent = array_real.pop()
    return Individual

def change_crossover_methods(stubs):
    Individual.mutation_crossover = stubs.pop()
    Individual.simple_crossover = stubs.pop()
    Individual.get_random_number = stubs.pop()
    Individual.get_loser_agent = stubs.pop()
    Individual.get_winner_agent = stubs.pop()
    return Individual

def test_simple_crossover_selection():
    agent_winner = ["agent1",2,0]
    agent_loser  = ["agent2",1,0]
    stubs,real = create_crossover_stubs(agent_winner,agent_loser,0.70)
    #Change real methods
    Individual = change_crossover_methods(stubs)
    #Test of the function 
    result1= test_individual.crossover(test_individual_1)
    #recovery methods
    Individual = recovery_crossover_methods(real)
    assert(result1 == "SIMPLE_CROSSOVER" )

def test_mutation_crossover_selection():
    agent_winner = ["agent1",2,0]
    agent_loser  = ["agent2",1,0]
    stubs,real = create_crossover_stubs(agent_winner,agent_loser,0.05)
    #Change real methods
    Individual = change_crossover_methods(stubs)
    #Test of the function 
    result1= test_individual.crossover(test_individual_1)
    #recovery methods
    Individual = recovery_crossover_methods(real)
    assert(result1 == "MUTATION_CROSSOVER" )









