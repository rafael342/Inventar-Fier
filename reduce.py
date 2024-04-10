from functools import reduce


def adauga_numarul():
    x = []
    numere = int(input("Cate Numere Vrei Sa Adaugi ? : "))
    for i in range(numere):
        numar = int(input(f"Aduaga Numarul Aici {i + 1}: "))
        x.append(numar)
    print(f"Ai Adaugat {len(x)} numere ")

    intrebare = int(input("Ce vrei sa faci cu numerele adaugate ? (1.Adunare, 2.Scadere, 3.Inmultire, 4.Impartire): "))

    if intrebare == 1:
        rezultat = sum(x)
        print("Rezultatul adunarii este:", rezultat)
    elif intrebare == 2:
        rezultat = reduce(lambda a, b: a - b, x)
        print("Rezultatul scaderii este:", rezultat)
    elif intrebare == 3:
        rezultat = reduce(lambda a, b: a * b, x)
        print("Rezultatul inmultirii este:", rezultat)
    elif intrebare == 4:
        rezultat = reduce(lambda a, b: a / b, x)
        print("Rezultatul impartirii este:", rezultat)
    else:
        print("Opțiune invalidă!")


adauga_numarul()



#spin the will
cash = []


def play_game():
    objects = ['Hearts', 'Spades', 'Kings', 'Hearts', 'Spades', 'Kings', 'Hearts', 'Spades', 'Kings']
    num_spins = 3
    stake = int(input("Enter Stake: "))  # Convert input to integer
    reward = stake * 2

    while True:
        for _ in range(num_spins):
            random.shuffle(objects)
            selected_items = random.sample(objects, 3)
            print(selected_items)

        if selected_items[0] == selected_items[1] == selected_items[2]:
            print("You Won " + str(reward))
            cash.append(reward)
            break  # Exit the loop if the winning condition is met
        else:
            print("Sorry, You Lost")


# Call the function to play the game



def show_balance():

        print(cash)

# main program
def main():
    print("1.Add Money")
    print("2.Show Balance")
    print("3.Spin Wall")
    print("4.Exit Game")


















































