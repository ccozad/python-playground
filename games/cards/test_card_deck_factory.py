import games.cards.card_deck_factory as cdf

def test_standard_playing_card_deck():
    deck = cdf.CardDeckFactory.get_deck(cdf.CardDeckType.standard_playing_card)

    assert len(deck) == 52

def test_unknown_type_deck():
    deck = cdf.CardDeckFactory.get_deck('foobar')

    assert len(deck) == 0