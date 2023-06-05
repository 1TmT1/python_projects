import random


def pick_random_number():
    random_num = random.randint(0, 3)
    return random_num


def get_user_choice():
    choice = input("Enter rock, paper or scissors: ")
    return choice


def get_computer_choice():
    choice = pick_random_number()
    if choice == 0:
        choice = "rock"
    elif choice == 1:
        choice = "paper"
    else:
        choice = "scissors"
    return choice


def main():
    counter_computer = 0
    counter_user = 0
    while counter_user < 3 and counter_computer < 3:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(computer_choice)
        try:
            if user_choice == computer_choice:
                print("Draw!")
                print("user: " + str(counter_user) + " ; " + "bot: " + str(counter_computer))
            else:
                if (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock"):
                    print("User won!")
                    counter_user += 1
                    print("user: " + str(counter_user) + " ; " + "bot: " + str(counter_computer))
                elif (user_choice == "scissors" and computer_choice == "rock") or (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors"):
                    print("Computer won!")
                    counter_computer += 1
                    print("user: " + str(counter_user) + " ; " + "bot: " + str(counter_computer))
                else:
                    print("You didn't type available choice!")
        except:
            print("Error...")


if __name__ == "__main__":
    main()
