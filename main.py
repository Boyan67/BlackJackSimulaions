import csv
import random
import time

from Game import Game
from Player import Player
import numpy as np
import scipy.stats as st
import statistics as stat

random.seed(25)


def output_report(player_stack, final_bet_history, total_bets, total_player_win, total_ties, total_computer_win):
    """
    Calculates and returns information for the simulation results
    :param player_stack: list of the player's bankroll after each round
    :return: A list of information on the results from the simulation
    """
    casino_advantage = round((10000 - np.mean(player_stack)) / np.mean(total_bets) * 100, 2)
    ci_l, ci_h = st.norm.interval(alpha=0.95, loc=np.mean(player_stack),
                                  scale=st.sem(player_stack))
    player_final_stack_test = [1 if i > 10000 else 0 for i in player_stack]
    mean = round(stat.mean(player_stack), 2)
    std_dev = round(stat.stdev(player_stack), 2)
    ci95 = round(ci_l, 2), (round(ci_h, 2))
    profit_realized = round((sum(player_final_stack_test) / len(player_final_stack_test)) * 100, 2)
    median = np.percentile(player_stack, 50)
    q1 = np.percentile(player_stack, 25)
    q3 = np.percentile(player_stack, 75)
    percent95 = np.percentile(player_stack, 95)
    percent5 = np.percentile(player_stack, 5)
    min_bankroll = min(player_stack)
    max_bankroll = max(player_stack)
    bet_mean = round(stat.mean(final_bet_history), 2)
    bet_median = np.percentile(final_bet_history, 50)
    max_bet = max(final_bet_history)
    return [mean, std_dev, ci95, profit_realized, casino_advantage, total_player_win, total_ties, total_computer_win,
            median, q1, q3, min_bankroll, max_bankroll, bet_mean, bet_median, max_bet, percent5, percent95]


# All card counting methods that will be used for the simulations
hi_lo = {
    "name": "Hi-Lo", "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 0, "8": 0, "9": 0, "10": -1,
    "Jack": -1, "Queen": -1, "King": -1, "Ace": -1}
kiss = {
    "name": "KISS3", "2": 0, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 0, "9": 0, "10": -1,
    "Jack": -1, "Queen": -1, "King": -1, "Ace": -1}
zen = {
    "name": "ZEN", "2": 1, "3": 1, "4": 2, "5": 2, "6": 2, "7": 1, "8": 0, "9": 0, "10": -2,
    "Jack": -2, "Queen": -2, "King": -2, "Ace": -1}
hi_opt_2 = {
    "name": "Hi-Opt 2", "2": 1, "3": 1, "4": 2, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0, "10": -2,
    "Jack": -2, "Queen": -2, "King": -2, "Ace": 0}
wong_halves = {
    "name": "Wong Halves", "2": 0.5, "3": 1, "4": 1, "5": 1.5, "6": 1, "7": .5, "8": 0, "9": -0.5, "10": -1,
    "Jack": -1, "Queen": -1, "King": -1, "Ace": -1}
revere_RAPC = {
    "name": "Revere RAPC", "2": 2, "3": 3, "4": 3, "5": 4, "6": 3, "7": 2, "8": 0, "9": -1, "10": -3,
    "Jack": -3, "Queen": -3, "King": -3, "Ace": -4}
no_card_counting = {
    "name": "no_card_counting", "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
    "Jack": 0, "Queen": 0, "King": 0, "Ace": 0}
decimal_counting = {
    "name": "decimal_counting", "2": 3.8, "3": 4.6, "4": 6.1, "5": 8, "6": 4.6, "7": 2.9, "8": -0.1,
    "9": -2, "10": -4.9, "Jack": -4.9, "Queen": -4.9, "King": -4.9, "Ace": -5.8}
practical = {"name": "practical", '2': 1, '3': 1, '4': 2, '5': 2, '6': 1, '7': 1, '8': 0, '9': -1, '10': -1, 'Jack': -1,
             'Queen': -1, 'King': -1, 'Ace': -2}


# Simulation Settings
# strategy = ["basic"]
# num_decks = [1, 2, 6, 8]
# s17_h17 = ["S17"]
# penetration = [.25, .5, .75, 0.90]
# betting_size = ["running", "true", "true*2", "true+2", "true-2"]
# card_counting = [practical]

# Code to simulate under all simulation settings for 10,000 games of 100 hands each.
def multiple_conditions(filename, strategy, num_decks, s17_h17, penetration, betting_size, card_counting):
    """
    Runs 10,000 hands under a number of conditions you specify in arrays and stores many relevant statistics to a csv file.
    :param filename: Name of csv file to save results
    :param strategy: List of strategies from: ['basic', 'mimic_dealer', 'never_bust']
    :param num_decks: List of different numbers (any number) of decks to perform simulations. e.g.([2, 4, 6])
    :param s17_h17: List of either S17, H17 or both. e.g.(['S17', 'H17'])
    :param penetration: List of percentages of the shoe to be played before shuffling. e.g. (0.90)
    :param betting_size: List of betting systems. Available options (["running", "true", "true*2", "true+2", "true-2"])
    :param card_counting: List of card counting methods defined as dictionaries. Pre-defined card counting methods:
    [hi_lo, zen, kiss, hi-opt2, revereRAPC, wongHalves, no_card_counting, decimal_counting, practical_counting]
    """
    final_bet_history = []
    player = Player("Jim")
    f = open(f'bankroll/{filename}.csv', 'w')
    writer = csv.writer(f)
    count = 0
    for a in strategy:
        for b in num_decks:
            for c in s17_h17:
                for d in penetration:
                    for e in betting_size:
                        for f in card_counting:
                            t0 = time.time()
                            count += 1
                            final_player_stack = []
                            total_bets = []
                            total_player_win = 0
                            total_ties = 0
                            total_computer_win = 0
                            k = 1
                            while k < 10000:
                                k += 1
                                game = Game(a, b, c, d, e, f)
                                game_result = game.play_game(player, 100)
                                final_player_stack.append(game_result[0])
                                total_bets.append(game_result[1])
                                total_player_win += game_result[2]
                                total_ties += game_result[3]
                                total_computer_win += game_result[4]
                                final_bet_history += game_result[5]
                            t1 = time.time()
                            print(f"Time: {t1 - t0}")
                            print(count)
                            sim_variables = [a, b, c, d, e, f['name']]
                            analysis = output_report(final_player_stack, final_bet_history, total_bets,
                                                     total_player_win, total_ties, total_computer_win)
                            row = sim_variables + analysis
                            writer.writerow(row)


def single_simulation(filename, strategy, num_decks, s17_h17, penetration, bet_size, counting_method):
    """
    Simulates a single simulation under specified conditions and creates
    a csv file with the player bankroll at each round.
    :param filename: a string with the name of the file for the results to be stored in
    :param strategy: a string with what strategy to use: 'basic', 'mimic_dealer', 'never_bust'
    :param num_decks: number of decks for the game to be played with
    :param s17_h17: either S17 or H17 to be used as the game type
    :param penetration: percentages of the shoe to be played before shuffling. e.g. (0.90)
    :param bet_size: betting system from available options (["running", "true", "true*2", "true+2", "true-2"])
    :param counting_method: a single card counting method defined as a dictionary. Pre-defined card counting methods:
    [hi_lo, zen, kiss, hi-opt2, revereRAPC, wongHalves, no_card_counting, decimal_counting, practical_counting]
    """
    final_player_stack = []
    player = Player("A")
    file = open(f'bankroll/{filename}.csv', 'w')
    stack = []
    w = csv.writer(file)
    i = 0

    while i < 10000:
        i += 1
        # game_set = Game('basic', 6, 'S17', .75, 'true-2', revere_RAPC)
        game_set = Game(strategy, num_decks, s17_h17, penetration, bet_size, counting_method)
        result = game_set.play_game(player, 100)
        stack.append(result[-1])
        w.writerow(result[-1])
        final_player_stack.append(result[0])


# single_simulation('TestFile', 'basic', 6, 'S17', .75, 'true*2', revere_RAPC)

print(multiple_conditions.__doc__)
