# import random
#
# # Defining constants for card values and suits
# card_values = {
#     "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
#     "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
# }
# card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#
#
# # Function to create a deck of cards
# def create_deck():
#     return [value + " of " + suit for value in card_values for suit in card_suits]
#
#
# # Function to deal a card from the deck
# def deal_card(deck):
#     return deck.pop(random.randint(0, len(deck) - 1))
#
#
# # Calculate the score for a hand, considering Ace as 1 or 11
# def calculate_score(hand):
#     score = sum(card_values[card.split()[0]] for card in hand)
#     num_aces = sum(1 for card in hand if card.startswith('A'))
#
#     while score > 21 and num_aces:
#         score -= 10
#         num_aces -= 1
#
#     return score
#
#
# # Function for the player's turn
# def player_turn(deck, player_hand):
#     while True:
#         print(f"Your hand: {player_hand}, current score: {calculate_score(player_hand)}")
#         action = input("Type 'hit' to get another card, 'stand' to hold: ").lower()
#
#         if action == 'hit':
#             player_hand.append(deal_card(deck))
#             if calculate_score(player_hand) > 21:
#                 print(f"You went over 21! Your final hand: {player_hand}")
#                 return False
#         elif action == 'stand':
#             return True
#         else:
#             print("Invalid input. Please type 'hit' or 'stand'.")
#
#
# # Function for the dealer's turn
# def dealer_turn(deck, dealer_hand):
#     print(f"Dealer's starting hand: {dealer_hand}")
#     while calculate_score(dealer_hand) < 17:
#         dealer_hand.append(deal_card(deck))
#         print(f"Dealer hits and gets another card: {dealer_hand}")
#     print(f"Dealer stands with hand: {dealer_hand}")
#
#
# # Function to compare scores and determine the winner
# def compare_scores(player_hand, dealer_hand):
#     player_score = calculate_score(player_hand)
#     dealer_score = calculate_score(dealer_hand)
#
#     print(f"Your final hand: {player_hand}, final score: {player_score}")
#     print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
#
#     if player_score > 21:
#         return "You went over. Dealer wins!"
#     elif dealer_score > 21:
#         return "Dealer went over. You win!"
#     elif player_score > dealer_score:
#         return "You win!"
#     elif player_score < dealer_score:
#         return "Dealer wins!"
#     else:
#         return "It's a draw!"
#
#
# # Main function to run the Blackjack game
# def blackjack():
#     deck = create_deck()
#     random.shuffle(deck)
#
#     player_hand = [deal_card(deck), deal_card(deck)]
#     dealer_hand = [deal_card(deck), deal_card(deck)]
#
#     if player_turn(deck, player_hand):
#         dealer_turn(deck, dealer_hand)
#
#     print(compare_scores(player_hand, dealer_hand))
#
#
# # Start the Blackjack game
# if __name__ == "__main__":
#     blackjack()


import random

# Define the deck of cards, with Ace as 11, and face cards as 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to deal a card (randomly selects a card from the deck)
def deal_card():
    return random.choice(cards)


# Calculate the score for a hand, considering Ace as 1 or 11
def calculate_score(hand):
    score = sum(hand)
    num_aces = hand.count(11)

    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1

    return score


# Function for the player's turn
def player_turn(player_hand):
    while True:
        print(f"Your hand: {player_hand}, current score: {calculate_score(player_hand)}")
        action = input("Type 'hit' to get another card, 'stand' to hold: ").lower()

        if action == 'hit':
            player_hand.append(deal_card())
            if calculate_score(player_hand) > 21:
                print(f"You went over 21! Your final hand: {player_hand}")
                return False
        elif action == 'stand':
            return True
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")


# Function for the dealer's turn
def dealer_turn(dealer_hand):
    print(f"Dealer's starting hand: {dealer_hand}")
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print(f"Dealer hits and now has: {dealer_hand}")
    print(f"Dealer stands with hand: {dealer_hand}")


# Function to compare scores and determine the winner
def compare_scores(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

    if player_score > 21:
        return "You went over. Dealer wins!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    elif player_score < dealer_score:
        return "Dealer wins!"
    else:
        return "It's a draw!"


# Main function to run the Blackjack game
def blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    if player_turn(player_hand):
        dealer_turn(dealer_hand)

    print(compare_scores(player_hand, dealer_hand))


# Start the Blackjack game
if __name__ == "__main__":
    blackjack()