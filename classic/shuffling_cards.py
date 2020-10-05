import itertools, random

def playing_cards(player):
    deck = list(itertools.product(['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, \
        "Jack", "Queen", "King"], ["Spade", "Heart", "Diamond", "Club"]))
    random.shuffle(deck)

    print("Hey {}! You got: " .format(player))
    for i in range(3):
        print(deck[i][0], "of", deck[i][1])
    print("-" * 25)

n = int(input("Enter number of players: "))

for k in range(n):
    player = input("Enter your name: ")
    playing_cards(player)