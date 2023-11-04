from os import system

print("Welcome to the secret auction program.")
condition_1 = True
list_bidders = []
list_bids = []


def add_bidder(a, b):
    list_bidders.append({a: b})


while condition_1:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    list_bids.append(bid)

    add_bidder(name, bid)

    if new_bidder == "yes":
        system("cls")
    elif new_bidder == "no":
        condition_1 = False
        # print("See you")
    else:
        condition_1 = False
        # print("You don't chose , so see you")

high_value = 0
name_winner = ""
for dictionary in list_bidders:
    for key in dictionary:
        valor = dictionary[key]
        if valor > high_value:
            high_value = valor
            name_winner = key
print(f"The winner is {name_winner} with a bid of ${high_value}")
