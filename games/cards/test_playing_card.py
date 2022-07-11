import games.cards.playing_card as pc

def test_constructor():
    card = pc.PlayingCard(pc.PlayingCardSuit.spades, pc.PlayingCardValue.ace)

    assert card._suit.name == 'spades'
    assert card._value.name == 'ace'

def test_suit():
    card = pc.PlayingCard(pc.PlayingCardSuit.spades, pc.PlayingCardValue.ace)

    assert card.suit == 'spades'

def test_value():
    card = pc.PlayingCard(pc.PlayingCardSuit.spades, pc.PlayingCardValue.ace)

    assert card.value == 'ace'

def test_str():
    card = pc.PlayingCard(pc.PlayingCardSuit.spades, pc.PlayingCardValue.ace)

    assert str(card) == 'ace of spades'

def test_repr():
    card = pc.PlayingCard(pc.PlayingCardSuit.spades, pc.PlayingCardValue.ace)

    assert repr(card) == 'PlayingCard(PlayingCardSuit.spades, PlayingCardValue.ace)'