import games.cards.card_deck as cd
import functools

def test_length():
    cards = [1,2,3,4,5,6]
    deck = cd.CardDeck(cards)

    assert len(deck) == 6

def test_draw_card():
    cards = [1,2,3,4,5,6]
    deck = cd.CardDeck(cards)
    top_card = deck.draw_card()

    assert top_card == 1
    assert len(deck) == 5

def test_draw_cards():
    cards = [1,2,3,4,5,6]
    deck = cd.CardDeck(cards)
    drawn_cards = deck.draw_cards(2)

    assert len(drawn_cards) == 2
    assert len(deck) == 4
    assert drawn_cards[0] == 1
    assert drawn_cards[1] == 2

def test_shuffle():
    cards = [1,2,3,4,5,6]
    deck = cd.CardDeck(cards)
    deck.shuffle()

    drawn_cards = deck.draw_cards(6)

    assert functools.reduce(
        lambda x, 
        y: x and y, 
        map(
            lambda p, 
            q: p == q, 
            cards, 
            drawn_cards
        ), 
        True) == False