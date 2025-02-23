from dataclasses import dataclass
from typing import Literal, TypeAlias, Optional

# See the slides and fill in the code

@dataclass(frozen=True)
class Card:
    # Create a Card dataclass. It should have a rank and suit
    pass

Deck: TypeAlias = list[Card]
Hand: TypeAlias = list[Card]


def draw_card(deck) -> Optional[tuple[Card, Deck]]:
    # if the deck is empty, return None
    # Else take the first card out and return the card and the new deck
    pass

def add_card_to_hand(hand: Hand, card: Card) -> Hand:
    # Add the card to the end of the hand and return the new hand
    pass

def draw_to_hand(hand: Hand, deck: Deck) -> tuple[Hand, Deck]:
    # Draw a card. If not possible, shuffle a new deck and draw
    # Return the hand and the current state of the deck
    pass

