from SilentAuctionArt import logo
print(logo)
bidders = {}
restart = True
while restart:
    name = input("What is your name?: ")
    bid = int(input("What is your bid: $"))
    bidders.update({name: bid})
    play_again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if play_again == "yes":
        print(logo)
        print(logo)
        print(logo)
    else:
        max_bet = 0
        for name, bet in bidders.items():
            if bet > max_bet:
                max_bet = bet
        print(f"The winner is someone with a bid of ${max_bet}")
        restart = False
