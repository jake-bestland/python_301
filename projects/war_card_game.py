import random

class Card:
    """Represents a standard playing card.
    Attribues:
        suit: 0-3
        rank: 1-13
    """
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        """checks if self card is less than other card, by rank.
        returns: bool
        """
        t1 = self.rank
        t2 =other.rank
        return t1 < t2
    
    def __eq__(self, other):
        """checks whether self and other have same rank.
        returns: bool
        """
        return self.rank == other.rank
    
class Deck:
    """Represents a deck of 52 standard playing cards."""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(0, 13):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def count_card(self):
        """Counts the amount of cards in a deck"""
        return len(self.cards)
    
    def pop_card(self, i=-1):
        """removes and returns a card from a deck.  
        
        i: index of the card to pop; defaults to the last card in the deck
        """
        return self.cards.pop(i)
    
    def add_card(self, card):
        """adds card to the end of the deck"""
        self.cards.append(card)

    # def add_hand(self, hand):
    #     self.hand = hand
    #     for card in self.hand:
    #         self.cards += card

    def shuffle(self):
        """shuffles the deck of cards."""
        random.shuffle(self.cards)

    def sort(self):
        """sorts cards in ascending order"""
        self.cards.sort()
        
    def move_cards(self, hand, num):
        """moves given number of cards from the deck into the Hand.
        
        hand:destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card[0])
    
class Hand(Deck):
    """Represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    

deck = Deck()
deck.shuffle()

player1 = Hand('Player 1')
player2 = Hand('Player 2')
deck.move_cards(player1, 26)
deck.move_cards(player2, 26)

while True:
    if player1.count_card() == 0:
        print("Player 2 wins the game!")
        break
    if player2.count_card() == 0:
        print("Player 1 wins the game!")
        break
    inp = input("To continue, press enter. Press 'q' to quit, or 'c' to see how many cards each player has.")
    if inp == "q":
        break
    if inp == "c":
        print(f"Player 1: {player1.count_card()} cards.\nPlayer 2: {player2.count_card()} cards.")
        continue
    p1_card = player1.pop_card(0)
    p2_card = player2.pop_card(0)
    print(f"Player 1 draws: {p1_card}")
    print(f"Player 2 draws: {p2_card}")
    if p1_card > p2_card:
        print(f"Player 1 wins the hand and adds {p1_card} and {p2_card} to their hand.")
        player1.add_card(p1_card)
        player1.add_card(p2_card)
        continue
    elif p1_card < p2_card:
        print(f"Player 2 wins the hand and adds {p2_card} and {p1_card} to their hand.")
        player2.add_card(p2_card)
        player2.add_card(p1_card)
        continue
    else:
        print(f"It's a tie! {player1.label} goes to war with {player2.label} to see who wins the hand!")
        num = 3
        p1_w_hand = Hand()
        p2_w_hand = Hand()
        p1_w_hand.add_card(p1_card)
        p2_w_hand.add_card(p2_card)
        if player1.count_card() < 3 and player1.count_card() < player2.count_card():
            num = player1.count_card()
        elif player2.count_card() < 3:
            num = player2.count_card()
        tie = True
        while tie == True:
            player1.move_cards(p1_w_hand, num)
            player2.move_cards(p2_w_hand, num)
            print(f"{player1.label} and {player2.label} each lay 2 cards face down. P1={p1_w_hand}.\n P2={p2_w_hand}")
            p1_w_card = p1_w_hand.pop_card()
            p2_w_card = p2_w_hand.pop_card()
            print(f"Player 1 draws: {p1_w_card}")
            print(f"Player 2 draws: {p2_w_card}")
            if p1_w_card > p2_w_card:
                print(f"{player1.label} wins!")
                player1.add_card(p1_w_card)
                player1.add_card(p2_w_card)
                for card in p1_w_hand.cards:
                    player1.add_card(card)
                for card in p2_w_hand.cards:
                    player1.add_card(card)
                tie = False
            elif p1_w_card < p2_w_card:
                print(f"{player2.label} wins!")
                player2.add_card(p1_w_card)
                player2.add_card(p2_w_card)
                for card in p1_w_hand.cards:
                    player2.add_card(card)
                for card in p2_w_hand.cards:
                    player2.add_card(card)
                tie = False
            else:
                p1_w_hand.add_card(p1_w_card)
                p2_w_hand.add_card(p2_w_card)
                continue
    

