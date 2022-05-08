import os
import glob
import pandas as pd

# a = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'basic']
# count = 1
# for i in a:
#     count += 1
#     df = pd.read_csv(f"{i}.csv")
#     df.to_csv(f'new_data_analysis/{count}.csv', index=False)
#


head = "strategy,num_decks,s17_h17,penetration,bet_size,card_counting,mean_bankroll,std_dev,CI95,profit_realized,casino_advantage,total_player_win,total_ties,total_computer_win,median,q1,q3,min_bankroll,max_bankroll,bet_mean,bet_median,max_bet,percent5,percent95"
head_list = head.split(",")
df = pd.read_csv("all.csv")

df = df.drop(df.columns[0], axis=1)
df.to_csv('all.csv', index=False)

#no_stack.to_csv('new_data_analysis/combined_no_stack.csv', index=False)
#print(df.to_csv('combined.csv'))

# df = pd.read_csv("new_data_analysis/combined.csv")
# print(df)
# df.drop(df[df['strategy'] == "never_bust"].index, inplace=True)
# df.to_csv('new_data_analysis/combined_no_stack.csv', index=False)
# print(df)

#
# strategy = ["basic", 'never_bust']
# num_decks = [1, 2, 6, 8]
# s17_h17 = ["S17", 'H17']
# penetration = [0.25, 0.50, 0.90]
# betting_size = ["running", "true", "true*2", "true+1", "true-1"]
# card_counting = ['hi_lo', 'kiss', 'zen', 'hi_opt_2']
#
# totals = []
# for a in strategy:
#     for b in num_decks:
#         for c in s17_h17:
#             for d in penetration:
#                 for e in betting_size:
#                     for f in card_counting:
#                         sim_variables = [a, b, c, d, e, f]
#                         totals.append(sim_variables)
#
# print(len(totals))
#
