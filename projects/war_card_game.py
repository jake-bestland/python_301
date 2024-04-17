import random

class Card:
    """Represents a standard playing card.
    Attribues:
        suit: 0-3
        rank: 1-13
    """
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

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
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def count_card(self):
        """Counts the amount of cards in a deck"""
        count = 0
        for card in self.cards:
            count += 1
        return count
    
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
        
    def determine_winner(self, p1_card, p2_card):
        """determines winner based on the rank of the card.
        
        p1_card: the card from player 1
        p2_card: the card from player 2
        """
        self.p1_card = p1_card
        self.p2_card = p2_card
        if p1_card > p2_card:
            return f"win"
        if p1_card < p2_card:
            return f"lose"
        else:
            return f"tie"
    
    def war(self, other, p1_card, p2_card, num=3):
        """A tiebreaker."""
        print(f"{self.label} goes to war with {other.label}")
        p1_w_hand = Hand()
        p2_w_hand = Hand()
        p1_w_hand.add_card(p1_card)
        p2_w_hand.add_card(p2_card)
        if self.count_card() < 3:
            num = self.count_card()
        if other.count_card() < 3:
            num = other.count_card()
        tie = True
        while tie == True:
            self.move_cards(p1_w_hand, num)
            other.move_cards(p2_w_hand, num)
            print(f"{self.label} and {other.label} each lay 2 cards face down. P1={p1_w_hand}.\n P2={p2_w_hand}")
            p1_w_card = p1_w_hand.pop_card()
            p2_w_card = p2_w_hand.pop_card()
            print(f"Player 1 draws: {p1_w_card}")
            print(f"Player 2 draws: {p2_w_card}")
            w_result = p1_w_hand.determine_winner(p1_w_card, p2_w_card)
            if w_result == "win":
                print(f"{self.label} wins!")
                self.add_card(p1_w_card)
                self.add_card(p2_w_card)
                for card in p1_w_hand.cards:
                    self.add_card(card)
                for card in p2_w_hand.cards:
                    self.add_card(card)
                tie = False
            elif w_result == "lose":
                print(f"{other.label} wins!")
                other.add_card(p1_w_card)
                other.add_card(p2_w_card)
                for card in p1_w_hand.cards:
                    other.add_card(card)
                for card in p2_w_hand.cards:
                    other.add_card(card)
                tie = False
            else:
                p1_w_hand.add_card(p1_w_card)
                p2_w_hand.add_card(p2_w_card)
                continue
    

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
    result = player1.determine_winner(p1_card, p2_card)
    if result == "win":
        print(f"Player 1 wins the hand and adds {p1_card} and {p2_card} to their hand.")
        player1.add_card(p1_card)
        player1.add_card(p2_card)
        continue
    elif result == "lose":
        print(f"Player 2 wins the hand and adds {p2_card} and {p1_card} to their hand.")
        player2.add_card(p2_card)
        player2.add_card(p1_card)
        continue
    else:
        print("It's a tie! Both Players must go to war to win the hand!")
        player1.war(player2, p1_card, p2_card)
        # print(f"P1 new hand:{player1}\nP2 new hand:{player2}")
    

