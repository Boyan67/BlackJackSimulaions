# BlackJackSimulaions
Final Year University Project

This Project is an investigation into the game of blackjack,its rules of play, playing strategies and methods of card counting. The main goal is to discover whether blackjack can be a profitable game, and if so, to determine the best playing strategies and the best card-counting methods. These methods and strategies have been implemented into simulations. An observation of how the casino rules work for or against the players. New card counting methods have been developed in an improvement on existing methods.


## Installation

Only requirments are the numpy and scipy libraries. 

```bash
pip install numpy, scipy
```

## Usage

Within the main file there are two main functions that can be used to reproduce the results.
single_simulation() - Runs 10,000 hands under a set of conditions you specify and records the bankroll of the player in a csv file at after each round.
```python
single_simulation('TestFile', 'basic', 6, 'S17', .75, 'true*2', revere_RAPC)
#For a more detailed description of the function use:
print(single_simulation.__doc__)
```

multiple_conditions() - Runs 10,000 hands under a number of conditions you specify in arrays and stores many relevant statistics to a csv file.
```python
multiple_conditions(filename, strategy, num_decks, s17_h17, penetration, betting_size, card_counting)

#For a more detailed description of the function use:
print(multiple_conditions.__doc__)
```


## Supplementary Material

Under the Supplementary Material folder you can find:
* CSV files with gathered data
* All graphs that were generated from the results files
* Code to generate the graphs
* A progress tracking report for the project and adviser meetings
* Final Report PDF Document

## License
[MIT](https://choosealicense.com/licenses/mit/)
