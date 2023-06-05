import random


def main():
    num_to_guess = random.randint(0, 21)
    while True:
        num = input("Try to guess a number between 0 to 20: ")
        if num == "break":
            break
        elif int(num) < num_to_guess:
            print("Too low!")
        elif int(num) > num_to_guess:
            print("Too high!")
        else:
            print("You got it!")
            break


if __name__ == "__main__":
    main()
