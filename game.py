from deck import Deck, Card
import sys
from deck_to_list import deck_to_list

def one_round(deck_hand, deck_table):
    while deck_hand.top != None:
        deck_hand.top_to(deck_table)
        deck_hand.top_to_bottom()

def check_original(deck, card_count):
    original = [ card_count - 1 - i for i in range(0, card_count)]
    return deck_to_list(deck) == original

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("To play this game, run it from command line with the size of the deck as an argument")
        quit()
    
    card_count = int(sys.argv[1])
    round_count = 0
    if card_count:
        deck_hand = Deck(card_count)
        deck_table = Deck(0)

        one_round(deck_hand, deck_table)
        swapper = deck_hand
        deck_hand = deck_table
        deck_table = swapper
        round_count += 1
        while(not check_original(deck_hand, card_count)):
            one_round(deck_hand, deck_table)
            swapper = deck_hand
            deck_hand = deck_table
            deck_table = swapper
            round_count += 1
    print("To get your original deck back took", round_count, "rounds")
