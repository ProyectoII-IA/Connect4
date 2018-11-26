# Package: tests.model_tests.startegies
# Description: Individual tests 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina Sanchez 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION 

from model.genetics.individual import Individual
from config.config import Config as cf
from model.genetics.game_genetics import GameGenetics 
# Fake agents

agent_1 = ["agent1",0,1]
agent_2 = ["agent2",0,2]

test_individual = Individual("agent1",0,"agent2",0)
test_individual_1 = Individual("agent1_1",0,"agent2_1",0)

array_stubs = []
array_real = []

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
    stubs,real = create_crossover_stubs(agent_winner,agent_loser,cf.MUTATION_PROBABILITY+10)
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
    stubs,real = create_crossover_stubs(agent_winner,agent_loser,cf.MUTATION_PROBABILITY-0.01)
    #Change real methods
    Individual = change_crossover_methods(stubs)
    #Test of the function 
    result1= test_individual.crossover(test_individual_1)
    #recovery methods
    Individual = recovery_crossover_methods(real)
    assert(result1 == "MUTATION_CROSSOVER" )

# FIT AGENTS TESTS------------------------------------------

def create_fit_agents_stub(winner):

    play_game_stub = lambda _: winner
    array_stubs.append(play_game_stub)
    play_game_real = GameGenetics.play_game
    array_real.append(play_game_real)

    return array_stubs,array_real

def recovery_fit_agents_real(real):
    GameGenetics.play_game = real.pop()
    return GameGenetics

def change_git_agents_stubs(stubs):
    GameGenetics.play_game = stubs.pop()
    return GameGenetics


def test_fit_agents_winner_agent1():
    agent_1 = ["agent1",0,0]
    agent_2  = ["agent2",0,0]
    temp_loop = cf.FIT_LOOP 
    cf.FIT_LOOP = 3
    stubs,real = create_fit_agents_stub(cf.WINNER_1)

    GameGenetics = change_git_agents_stubs(stubs)


    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2

    result = test_individual.fit_agents()
    assert(result==1)
    assert(test_individual.agent_1[1]==3)
    assert(test_individual.agent_2[1]==0)

    # recover variable 
    cf.FIT_LOOP = temp_loop
    GameGenetics = recovery_fit_agents_real(real)

def test_fit_agents_winner_agent2():
    agent_1 = ["agent1",0,0]
    agent_2  = ["agent2",0,0]
    temp_loop = cf.FIT_LOOP 
    cf.FIT_LOOP = 3
    stubs,real = create_fit_agents_stub(cf.WINNER_2)

    GameGenetics = change_git_agents_stubs(stubs)


    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2

    result = test_individual.fit_agents()
    assert(result==1)
    assert(test_individual.agent_2[1]==3)
    assert(test_individual.agent_1[1]==0)

    # recover variable 
    cf.FIT_LOOP = temp_loop
    GameGenetics = recovery_fit_agents_real(real)

def test_fit_agents_winner_both():
    agent_1 = ["agent1",0,0]
    agent_2  = ["agent2",0,0]
    temp_loop = cf.FIT_LOOP 
    cf.FIT_LOOP = 3
    stubs,real = create_fit_agents_stub(cf.TIE)

    GameGenetics = change_git_agents_stubs(stubs)


    test_individual.agent_1 = agent_1
    test_individual.agent_2 = agent_2

    result = test_individual.fit_agents()
    assert(result==1)
    assert(test_individual.agent_2[1]==3)
    assert(test_individual.agent_1[1]==3)

    # recover variable 
    cf.FIT_LOOP = temp_loop
    GameGenetics = recovery_fit_agents_real(real)
    









