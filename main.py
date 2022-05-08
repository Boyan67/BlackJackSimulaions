import csv
import random
import time

import pandas as pd

from Game import Game
from Player import Player
import numpy as np
import scipy.stats as st

random.seed(25)
final_player_stack = []
final_bet_history = []
total_bets = []
total_player_win = 0
total_ties = 0
total_computer_win = 0


def output_report(player_stack):
    # Average Casino Winnings after 100 hands divided by average bet placed
    casino_advantage = round((10000 - np.mean(player_stack)) / np.mean(total_bets) * 100, 2)
    print(len(total_bets))
    print(total_bets)
    print(len(player_stack))
    print(player_stack)
    print(np.mean(player_stack))
    print(np.mean(total_bets))
    ci_l, ci_h = st.norm.interval(alpha=0.95, loc=np.mean(player_stack),
                                  scale=st.sem(player_stack))
    player_final_stack_test = [1 if i > 10000 else 0 for i in player_stack]
    mean = round(np.mean(player_stack), 2)
    # print(f'Mean: {mean}')
    std_dev = round(np.std(player_stack), 2)
    # print(f'Std Dev: {std_dev}')
    CI95 = round(ci_l, 2), (round(ci_h, 2))
    profit_realized = round((sum(player_final_stack_test) / len(player_final_stack_test)) * 100, 2)
    # print(f'Profit realized in {profit_realized} % of replications')
    # These are already created
    # print(f"casino advantage: {casino_advantage}")
    # print(f"player hand  wins: {total_player_win}")
    # print(f"hand ties: {total_ties}")
    # print(f"player hand loses: {total_computer_win}")
    median = np.percentile(player_stack, 50)
    # print(f"Median: {median}")
    q1 = np.percentile(player_stack, 25)
    # print(f"Q1: {q1}")
    q3 = np.percentile(player_stack, 75)
    percent95 = np.percentile(player_stack, 95)
    percent5 = np.percentile(player_stack, 5)
    # print(f"Q3: {q3}")
    min_bankroll = min(player_stack)
    # print(f"Min Bankroll: {min_bankroll}")
    max_bankroll = max(player_stack)
    # print(f"Max Bankroll: {max_bankroll}")
    bet_mean = round(np.mean(final_bet_history), 2)
    # print(f"Bet Mean: {bet_mean}")
    bet_median = np.percentile(final_bet_history, 50)
    # print(f"Bet Median: {bet_median}")
    max_bet = max(final_bet_history)
    # print(f"Bet Max: {max_bet}")
    return [mean, std_dev, CI95, profit_realized, casino_advantage, total_player_win, total_ties, total_computer_win,
            median, q1, q3, min_bankroll, max_bankroll, bet_mean, bet_median, max_bet, percent5, percent95]


hi_lo = {
    "name": "Hi-Lo", "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 0, "8": 0, "9": 0, "10": -1,
    "Jack": -1, "Queen": -1, "King": -1, "Ace": -1,
}
kiss = {
    "name": "KISS3", "2": 0, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 0, "9": 0, "10": -1,
    "Jack": -1, "Queen": -1, "King": -1, "Ace": -1,
}
zen = {
    "name": "ZEN", "2": 1, "3": 1, "4": 2, "5": 2, "6": 2, "7": 1, "8": 0, "9": 0, "10": -2,
    "Jack": -2, "Queen": -2, "King": -2, "Ace": -1,
}
hi_opt_2 = {
    "name": "Hi-Opt 2", "2": 1, "3": 1, "4": 2, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0, "10": -2,
    "Jack": -2, "Queen": -2, "King": -2, "Ace": 0,
}
wong_halves = {
    "name": "Wong Halves", "2": 0.5, "3": 1, "4": 1, "5": 1.5, "6": 1, "7": .5, "8": 0, "9": -0.5, "10": -1,
    "Jack": -1, "Queen": -1, "King": -1, "Ace": -1,
}
revere_RAPC = {
    "name": "Revere RAPC", "2": 2, "3": 3, "4": 3, "5": 4, "6": 3, "7": 2, "8": 0, "9": -1, "10": -3,
    "Jack": -3, "Queen": -3, "King": -3, "Ace": -4,
}
no_card_counting = {
    "name": "no_card_counting", "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
    "Jack": 0, "Queen": 0, "King": 0, "Ace": 0,
}

player = Player("Jim")

# f = open('1deck_h17.csv', 'w')
# strategy = ["basic"]
# num_decks = [1]
# s17_h17 = ["H17"]
# penetration = [0.25, 0.50, 0.75, 0.90]
# betting_size = ["running", "true", "true*2", "true+2", "true-2"]
# card_counting = [hi_lo, kiss, zen, hi_opt_2, wong_halves, revere_RAPC]

# f = open('2deck_h17.csv', 'w')
# strategy = ["basic"]
# num_decks = [2]
# s17_h17 = ["H17"]
# penetration = [0.25, 0.50, 0.75, 0.90]
# betting_size = ["running", "true", "true*2", "true+2", "true-2"]
# card_counting = [hi_lo, kiss, zen, hi_opt_2, wong_halves, revere_RAPC]

# f = open('6deck_h17.csv', 'w')
# strategy = ["basic"]
# num_decks = [6]
# s17_h17 = ["H17"]
# penetration = [0.25, 0.50, 0.75, 0.90]
# betting_size = ["running", "true", "true*2", "true+2", "true-2"]
# card_counting = [hi_lo, kiss, zen, hi_opt_2, wong_halves, revere_RAPC]

# f = open('test.csv', 'w')
# strategy = ["basic"]
# num_decks = [6]
# s17_h17 = ["S17"]
# penetration = [0.90]
# betting_size = ["true"]
# card_counting = [kiss]
#
#
# writer = csv.writer(f)
# count = 0
# for a in strategy:
#     for b in num_decks:
#         for c in s17_h17:
#             for d in penetration:
#                 for e in betting_size:
#                     for f in card_counting:
#                         t0 = time.time()
#                         count += 1
#                         final_player_stack = []
#                         total_bets = []
#                         total_player_win = 0
#                         total_ties = 0
#                         total_computer_win = 0
#                         k = 1
#                         while k < 10000:
#                             k += 1
#                             game = Game(a, b, c, d, e, f)
#                             game_result = game.play_game(player, 100)
#                             final_player_stack.append(game_result[0])
#                             total_bets.append(game_result[1])
#                             total_player_win += game_result[2]
#                             total_ties += game_result[3]
#                             total_computer_win += game_result[4]
#                             final_bet_history += game_result[5]
#                         t1 = time.time()
#                         print(f"Time: {t1 - t0}")
#                         print(count)
#                         sim_variables = [a, b, c, d, e, f['name']]
#                         analysis = output_report(final_player_stack)
#                         row = sim_variables + analysis
#                         writer.writerow(row)
# f.close()


f = open('bankroll/hi_lo_8deck.csv', 'w')
stack = []
writer = csv.writer(f)
k = 0
t0 = time.time()
# betting_size = ["running", "true", "true*2", "true+2", "true-2"]
while k < 10000:
    k += 1
    game = Game('basic', 8, 'S17', .8, 'true', hi_lo)
    game_result = game.play_game(player, 100)
    stack.append(game_result[-1])
    writer.writerow(game_result[-1])
    final_player_stack.append(game_result[0])


with open("bankroll/hi_lo_8deck.csv", newline='') as in_file:
    with open("bankroll/hi_lo_8deck_out.csv", 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)

print((np.mean(final_player_stack) - 10000)/100)
t1 = time.time()
print(f"Time: {t1 - t0}")
