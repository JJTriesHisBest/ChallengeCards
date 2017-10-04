from deck import Card, Deck
from deck_to_list import deck_to_list

def test_create_deck():
    empty_deck = Deck(0)
    assert(deck_to_list(empty_deck) == [])

    deck_of_five = Deck(5)
    assert(deck_to_list(deck_of_five) == [4,3,2,1,0])

def test_top_to_bottom():
    deck = Deck(5)
    deck.top_to_bottom()
    assert(deck_to_list(deck) == [3,2,1,0,4])
    deck.top_to_bottom()
    assert(deck_to_list(deck) == [2,1,0,4,3])

def test_top_to_and_to_top():
    decka = Deck(5)
    deckb = Deck(0)

    decka.top_to(deckb)
    assert(deck_to_list(decka) == [3,2,1,0])
    assert(deck_to_list(deckb) == [4])

def test_top_to_from_empty():
    decka = Deck(0)
    deckb = Deck(0)

    decka.top_to(deckb)
    assert(deck_to_list(decka) == [])
    assert(deck_to_list(deckb) == [])