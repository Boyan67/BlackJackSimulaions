strategy = ["basic", "never_bust"]
num_decks = [1, 2, 6, 8]
s17_h17 = ["S17", "H17"]
penetration = [0.25, 0.50, 0.75]
betting_size = ["r", "t", "t*2", "t+2", "t-2"]
card_counting = ["Hi-Lo", "Zen", "KISS", "Hi-Opt 2"]

all = []
for a in strategy:
    for b in num_decks:
        for c in s17_h17:
            for d in penetration:
                for e in betting_size:
                    for f in card_counting:
                        all.append(f"{a} - {b} - {c} - {d} - {e} - {f}")

print(len(all))

card_counting_method = {
  "2": 1,
  "3": 1,
  "4": 1,
  "5": 1,
  "6": 1,
  "7": 0,
  "8": 0,
  "9": 0,
  "10": -1,
  "Jack": -1,
  "Queen": -1,
  "King": -1,
  "Ace": -1,
}

print(card_counting_method["2"])
