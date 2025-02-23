import random
from itertools import product, starmap, cycle
from monads import MultiValue
from utils import compose2, update_dict
from card_games import Card, Deck, Hand, draw_to_hand

# See the slides and fill in the code

BUST_LIMIT = 22

def new_deck() -> Deck:
    pass

def shuffle(deck: Deck) -> Deck:
    pass

new_shuffled_deck = compose2(new_deck, shuffle)

def get_points_for_card(card: Card):
    # J, Q, K are worth 10 points
    # A is worth 1 or 11
    # number cards are worth their rank
    pass

def get_points(hand: Hand) -> MultiValue:
    # Score of a hand is the sum of scores of all cards
    pass

def score_hand(hand: Hand):
    # Take all possible scores of a hand and choose best one

#####
# This is the code game loop - the imperitive shell that contains all actions
# In this case any function that uses print or input is an action
#####

def get_player_action(hand):
    while (action := input('(H)it or (S)tay: ').lower()) not in {'h', 's'}:
        print("Only enter H or S")
    return action

def get_dealer_action(hand):
    total_points = score_hand(hand)
    if total_points >= 17:
        return 's'
    return 'h'

def initial_state():
    deck = new_shuffled_deck()
    players = ['Player', 'Dealer']
    hands = {player: [] for player in players}
    actions = {'Player': get_player_action, 'Dealer': get_dealer_action}
    return deck, players, hands, actions

def process_game():
    update_hands = update_dict
    deck, players, hands, actions = initial_state()
    turns = cycle(players)
    while players:
        turn = next(turns)
        hand = hands[turn]
        print(f'\n> {turn} hand is: {" ".join(str(card) for card in hand)}')
        action = actions[turn](hand)
        match action:
            case 'h':
                print(f'Hit')
                hand, deck = draw_to_hand(hand, deck)
                hands = update_hands(hands, turn, hand)
                print(f'Drawn {hand[-1]}')
                try:
                    total = score_hand(hand)
                    print(f'Current score is {total}')
                except ValueError:
                    print(f'BUSTED')
                    return hands
                hands = update_dict(hands, turn, hand)
            case 's':
                print(f'Stay')
                players = [player for player in players if player != turn]
                turns = cycle(players)
    return hands

def get_score(hand):
    try:
        total = score_hand(hand)
        return total
    except ValueError:
        return 'BUSTED'

def end_game(hands):
    print(f'\n*** Game Over ***')
    for player, hand in hands.items():
        print(f'{player}:{get_score(hand)}')

run = compose2(process_game, end_game)
run()
