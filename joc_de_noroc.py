import random

cash = []

def add_cash():
    try:
        add_money = int(input("Insert Amount Of Money: "))
        cash.append(add_money)
    except ValueError:
        print("Please insert only numeric values")
    else:
        add_more = input("Would you like to add more? (Y/N): ").lower()
        if add_more == "y":
            try:
                extra_money = int(input("Add Amount: "))
                cash.append(extra_money)
            except ValueError:
                print("Please insert only numeric values")
        else:
            return

def play_game():
    objects = ['Hearts', 'Spades', 'Kings', 'Hearts', 'Spades', 'Kings', 'Hearts', 'Spades', 'Kings']
    num_spins = 3
    stake = int(input("Enter Stake: "))
    reward = stake * 2

    while True:
        for _ in range(num_spins):
            random.shuffle(objects)
            selected_items = random.sample(objects, 3)
            print(selected_items)

        if selected_items[0] == selected_items[1] == selected_items[2]:
            print("You Won " + str(reward))
            cash.append(reward)
            break
        else:
            print("Sorry, You Lost")

def show_balance():
    print("Current balance: $", sum(cash))

def main():
    while True:
        print("1. Add Money")
        print("2. Show Balance")
        print("3. Spin the Wheel")
        print("4. Exit Game")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_cash()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            play_game()
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

main()

