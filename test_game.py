from deck import Deck, Card
from game import one_round, check_original
from deck_to_list import deck_to_list




def test_one_round():
    deck_hand = Deck(5)
    deck_table = Deck(0)
    one_round(deck_hand, deck_table)

    assert(deck_to_list(deck_hand) == [])
    assert(deck_to_list(deck_table) == [3,1,0,2,4])

def test_check_original():
    deck_hand = Deck(4)
    deck_table = Deck(0)
    assert(check_original(deck_hand, 4))
    
    one_round(deck_hand, deck_table)
    assert(not check_original(deck_table, 4))

    one_round(deck_table, deck_hand)
    assert(check_original(deck_hand, 4))
