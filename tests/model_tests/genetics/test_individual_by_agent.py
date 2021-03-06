# Package: tests.model_tests.strategies
# Description: Individual by agent tests 

# Artificial Intelligence, II Semester 2018
# Project: Connect 4
# Author : Katerine Molina Sanchez 
# E-mail: kanatalia95@gmail.com
# Version: 0.0.0 

#IMPORT SECTION 

from model.genetics.individual_by_agent import IndividualByAgent
from config.config import Config as cf
from model.genetics.game_genetics import GameGenetics 
from model.game.agent import Agent
import random 
import itertools
# Fake agents

agent =  Agent(1,2,True)

test_individual = IndividualByAgent(agent)
test_individual_1 = IndividualByAgent(agent)

array_stubs = []
array_real = []

def test_initialize_individual():
    individual = IndividualByAgent(agent)
    assert(individual.agent==agent)

# MUTATE AGENT TESTS---------------------------------------------

def test_mutate_agent_success():
    array_real.append(random.randint)
    array_real.append(cf.MUTATION_AMOUNT)
    random.randint = lambda x,y: 1
    cf.MUTATION_AMOUNT = 0.5
    strategies  =  [0,0,0,0]
    test_individual.agent.set_strategies(strategies)
    test_individual.mutate_agent()
    assert(test_individual.agent.strategies == [0,0.5,0,0])
    cf.MUTATION_AMOUNT = array_real.pop()
    random.randint = array_real.pop()

# GET WON GAMES AGENT TEST --------------------------------------


def test_get_won_games_agent_winner_1():
    array_real.append(GameGenetics.__init__)
    array_real.append(GameGenetics.play_game)
    GameGenetics.__init__ = lambda x,y,z: None
    GameGenetics.play_game = lambda _: cf.WINNER_1
    result1,result2 = test_individual.get_won_games_agent(agent,agent,1)
    assert(result1 == 1)
    assert(result2 == 0)

def test_get_won_games_agent_winner_2():
    array_real.append(GameGenetics.__init__)
    array_real.append(GameGenetics.play_game)
    GameGenetics.__init__ = lambda x,y,z: None
    GameGenetics.play_game = lambda _: cf.WINNER_2
    result1,result2 = test_individual.get_won_games_agent(agent,agent,1)
    assert(result1 == 0)
    assert(result2 == 0)

def test_get_won_games_agent_winner_ties():
    array_real.append(GameGenetics.__init__)
    array_real.append(GameGenetics.play_game)
    GameGenetics.__init__ = lambda x,y,z: None
    GameGenetics.play_game = lambda _: cf.TIE
    result1,result2 = test_individual.get_won_games_agent(agent,agent,1)
    assert(result1 == 0)
    assert(result2 == 1)
    GameGenetics.play_game = array_real.pop()
    GameGenetics.__init__ = array_real.pop()

def test_get_won_games_agent_winner_multiples_games():
    array_real.append(GameGenetics.__init__)
    array_real.append(GameGenetics.play_game)
    GameGenetics.__init__ = lambda x,y,z: None
    GameGenetics.play_game = lambda _: cf.WINNER_1
    result1,result2 = test_individual.get_won_games_agent(agent,agent,3)
    assert(result1 == 3)
    assert(result2 == 0)
    GameGenetics.play_game = array_real.pop()
    GameGenetics.__init__ = array_real.pop()

# GET_FIRST_BEST_AGENT----------------------------------------------------

def test_get_first_best_agent_success():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y: (2,2)
    strategies = ['G','S','H','E']
    result = test_individual.get_first_best_agent([strategies],test_individual,1)
    assert(result.agent.strategies == strategies)
    assert(result.agent.symb == 1)
    assert(result.agent.symb_opp == 2)
    assert(result.won_games == 0)
    IndividualByAgent.get_won_games_agent = array_real.pop()

def test_get_first_best_agent_no_found_child():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y: (2,2)
    strategies = ['G','S','H','E']
    test_individual_1.won_games  = 2
    test_individual.won_games    = 3
    result = test_individual.get_first_best_agent([strategies],test_individual_1,3)
    assert(result.agent== agent)
    assert(result.won_games == 0)
    IndividualByAgent.get_won_games_agent = array_real.pop()

def test_get_first_best_agent_no_found_child_second_parent():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y: (2,2)
    strategies = ['G','S','H','E']
    test_individual_1.won_games  = 4
    test_individual.won_games    = 2
    result = test_individual.get_first_best_agent([strategies],test_individual_1,3)
    assert(result.agent== agent)
    assert(result.won_games == 0)
    IndividualByAgent.get_won_games_agent = array_real.pop()


# SIMPLE CROSSOVER TESTS-----------------------------------------------------------
def test_simple_crossover_success():
    array_real.append(IndividualByAgent.get_first_best_agent)
    array_real.append(itertools.product)
    array_real.append(random.shuffle)
    
    probabilities = [1,2,3,4,5]
    IndividualByAgent.get_first_best_agent = lambda x,y,z: "Good Answer"
    itertools.product = lambda w,x,y,z: probabilities
    random.shuffle = lambda _:probabilities

    result = test_individual.simple_crossover(test_individual_1,3) 
    assert(result=="Good Answer")

    random.shuffle = array_real.pop()
    itertools.product = array_real.pop()
    IndividualByAgent.get_first_best_agent = array_real.pop()


# CROSSOVER AGENTS TESTS------------------------------------------------------------

def test_crossover_agents_success():
    array_real.append(IndividualByAgent.crossover)
    IndividualByAgent.crossover = lambda x,y,z: "Individual"

    result = test_individual.crossover_agents(["Agent1","Agent2"])
    assert(len(result)== 2)
    assert(result[0]=="Individual")
    
    IndividualByAgent.crossover = array_real.pop()

# CROSSOVER TESTS-------------------------------------------------------------------

def test_crossover_return_self():
    result = test_individual.crossover(None)
    assert(result == test_individual)
    
def test_crossover_return_mutate_individual():
    array_real.append(IndividualByAgent.simple_crossover)
    array_real.append(IndividualByAgent.get_random_number)
    array_real.append(IndividualByAgent.mutate_agent)
    IndividualByAgent.simple_crossover = lambda x,y,z: test_individual_1
    IndividualByAgent.get_random_number = lambda _: 0.05
    IndividualByAgent.mutate_agent = lambda _: None
    
    test_individual_1.won_games = 100
    result = test_individual.crossover(test_individual_1,0.10)
    assert(result==test_individual_1)
    assert(result.won_games == 100)

    IndividualByAgent.mutate_agent = array_real.pop()
    IndividualByAgent.get_random_number = array_real.pop()
    IndividualByAgent.simple_crossover = array_real.pop()

def test_crossover_return_simple_individual():
    array_real.append(IndividualByAgent.simple_crossover)
    array_real.append(IndividualByAgent.get_random_number)
    IndividualByAgent.simple_crossover = lambda x,y,z: test_individual_1
    IndividualByAgent.get_random_number = lambda _: 0.15
    
    test_individual_1.won_games = 100
    result = test_individual.crossover(test_individual_1,0.10)
    assert(result==test_individual_1)
    assert(result.won_games == 100)

    IndividualByAgent.get_random_number = array_real.pop()
    IndividualByAgent.simple_crossover = array_real.pop()

# FIT_AGENT TEST-------------------------------------------------------

def test_fit_agent_winner_self():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y,z: (1,0)

    test_individual.won_games=0 
    test_individual_1.won_games = 0
    test_individual.total_games=0 
    test_individual_1.total_games= 0

    result = test_individual.fit_agent([test_individual_1])

    assert(len(result)==1)
    assert(result[0]== test_individual_1)
    assert(result[0].won_games == 0)
    assert(test_individual.won_games == 1)
    assert(result[0].total_games == 1)
    assert(test_individual.total_games == 1)
    IndividualByAgent.get_won_games_agent = array_real.pop()

def test_fit_agent_winner_opponent():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y,z: (0,0)

    test_individual.won_games=0 
    test_individual_1.won_games = 0
    test_individual.total_games=0 
    test_individual_1.total_games= 0


    result = test_individual.fit_agent([test_individual_1])
    assert(len(result)==1)
    assert(result[0]== test_individual_1)
    assert(result[0].won_games == 1)
    assert(test_individual.won_games == 0)
    assert(result[0].total_games == 1)
    assert(test_individual.total_games == 1)

    IndividualByAgent.get_won_games_agent = array_real.pop()


def test_fit_agent_winner_both():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y,z: (0,1)

    test_individual.won_games=0 
    test_individual_1.won_games = 0
    test_individual.total_games=0 
    test_individual_1.total_games= 0

    result = test_individual.fit_agent([test_individual_1])
    assert(len(result)==1)
    assert(result[0]== test_individual_1)
    assert(result[0].won_games == 0)
    assert(test_individual.won_games == 0)
    assert(result[0].total_games == 1)
    assert(test_individual.total_games == 1)

def test_fit_agent_winner_self_multiples_games():
    array_real.append(IndividualByAgent.get_won_games_agent)
    IndividualByAgent.get_won_games_agent = lambda w,x,y,z: (0,1)

    test_individual.won_games=0 
    test_individual_1.won_games = 0
    test_individual.total_games=0 
    test_individual_1.total_games= 0

    test_individual_2 = IndividualByAgent("Agent")
    result = test_individual.fit_agent([test_individual_1,test_individual_2])
    assert(len(result)==2)
    assert(result[0].total_games == 1)
    assert(result[1].total_games == 1)
    assert(test_individual.total_games == 2)
    
    IndividualByAgent.get_won_games_agent = array_real.pop()

# GET_FITNESS_ TEST---------------------------------------------------------

def test_get_fitness_success():
    test_individual.total_games = 10 
    test_individual.won_games = 5

    result = test_individual.get_fitness_value()
    assert(result == 0.5)









"""     
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
     """









