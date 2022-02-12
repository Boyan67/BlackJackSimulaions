import random
import time
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
    casino_advantage = round((10000 - np.mean(player_stack)) / np.mean(total_bets) * 100, 2)
    ci_l, ci_h = st.norm.interval(alpha=0.95, loc=np.mean(player_stack),
                                  scale=st.sem(player_stack))
    player_final_stack_test = [1 if i > 10000 else 0 for i in player_stack]

    print(f'Mean: {round(np.mean(player_stack), 2)}')
    print(f'Std Dev: {round(np.std(player_stack), 2)}')
    print(f'95% CI: {round(ci_l, 2), (round(ci_h, 2))}')
    print(f'Profit realized in {round((sum(player_final_stack_test) / len(player_final_stack_test)) *100, 2)} % of replications')
    print(f"casino advantage: {casino_advantage}")
    print(f"player hand  wins: {total_player_win}")
    print(f"hand ties: {total_ties}")
    print(f"player hand loses: {total_computer_win}")
    print(f"Median: {np.percentile(player_stack, 50)}")
    print(f"Q1: {np.percentile(player_stack, 25)}")
    print(f"Q3: {np.percentile(player_stack, 75)}")
    print(f"Min Bankroll: {min(player_stack)}")
    print(f"Max Bankroll: {max(player_stack)}")
    print(f"Bet Mean: {round(np.mean(final_bet_history), 2)}")
    print(f"Bet Median: {np.percentile(final_bet_history, 50)}")
    print(f"Bet Max: {max(final_bet_history)}")


t0 = time.time()

player = Player("Jim")
decks = [6]
for i in decks:
    final_player_stack = []
    total_bets = []
    total_player_win = 0
    total_ties = 0
    total_computer_win = 0
    k = 1
    while k < 10000:
        k += 1
        game = Game(i, 1.5, "S17", 2, True, 0.95, "true")
        game_result = game.play_game(player, 100)
        final_player_stack.append(game_result[0])
        total_bets.append(game_result[1])
        total_player_win += game_result[2]
        total_ties += game_result[3]
        total_computer_win += game_result[4]
        final_bet_history += game_result[5]
    output_report(final_player_stack)

t1 = time.time()
print(f"Time: {t1 - t0}")

