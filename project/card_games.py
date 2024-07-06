from dataclasses import dataclass
from typing import Literal, TypeAlias, Optional

@dataclass(frozen=True)
class Card:
    rank: int
    suit: Literal['S','H','D','C']

    def __str__(self):
        match self.rank:
            case 1:
                rank_display = 'A'
            case 10 | 11 | 12 | 13 as rank:
                rank_display = "TJQK"[rank-10]
            case _ as rank:
                rank_display = str(rank)
        return f'{rank_display}{self.suit}'


Deck: TypeAlias = list[Card]
Hand: TypeAlias = list[Card]


def draw_card(deck) -> Optional[tuple[Card, Deck]]:
    match deck:
        case []:
            return None
        case [first, *rest]:
            return first, rest

def add_card_to_hand(hand: Hand, card: Card) -> Hand:
    return [*hand, card]

def draw_to_hand(hand: Hand, deck: Deck) -> tuple[Hand, Deck]:
    match draw_card(deck):
        case None:
            return draw_to_hand(hand, new_shuffled_deck())
        case (card, deck):
            new_hand = add_card_to_hand(hand, card)
            return new_hand, deck

