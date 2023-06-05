import random
import time


def main():
    start_num = 0
    end_num = 200
    random_number = random.randint(start_num, end_num)
    max_count = 3
    count = 0
    health = 100
    guess_counter = []
    counter = 0
    guesses = []
    print("You have " + str(health) + " health -------- right guesses: " + str(count))
    while health > 0 and count != max_count:
        try:
            cont = False
            guess = int(input("Enter your guess (Number 1 - 200): "))
            if start_num <= guess <= end_num:
                for number in guesses:
                    if guess == number:
                        print("You already tried this one...")
                        time.sleep(1)
                        print("Oh, by the way the number is ", end="")
                        if guess > random_number:
                            print("too high\n")
                        elif guess < random_number:
                            print("too low\n")
                        cont = True
                        break
                if cont:
                    cont = False
                    print("You have " + str(health) + " health -------- right guesses: " + str(count))
                    continue
                else:
                    guesses.append(guess)
                counter += 1
                if guess > random_number:
                    print("\nToo High\n")
                    health -= 10
                elif guess < random_number:
                    print("\nToo Low\n")
                    health -= 10
                else:
                    print("You picked the right number!!!\n")
                    random_number = random.randint(start_num, end_num)
                    health = 100
                    count += 1
                    guess_counter = []
                    counter = 0
                print("You have " + str(health) + " health -------- right guesses: " + str(count))
            else:
                print("You didn't enter number between the specified numbers({}, {})\n".format(start_num, end_num))
        except:
            print("You need to write a number!-)\n")
    if health == 0:
        print("The number was " + str(random_number))
        print("You lost:-(")
        print("You can always try again;-)")
    else:
        sum = 0
        for guesses in guess_counter:
            sum += guesses
        print("You won!!!")
        print("Average gc: " + str(sum / max_count))


if __name__ == "__main__":
    main()
