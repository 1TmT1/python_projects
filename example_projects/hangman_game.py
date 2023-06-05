import random


def start():
    is_already_exist = False
    new_word = input("Before we are going to start enter random word: ")
    words = open("words.txt", "r+")
    lines = words.read().splitlines()
    words.close()
    for x in lines:
        if x == new_word:
            is_already_exist = True
            break
    if is_already_exist:
        words = open("words.txt", "r+")
        words.write(new_word + "\n")
        words.close()
    print("Thank you!")


def get_random_word():
    word = open("words.txt", "r+")
    lines = word.read().splitlines()
    random_word = random.choice(lines)
    word.close()
    first_print = ""
    for x in range(len(random_word)):
        first_print += "_"
    print(first_print)
    return random_word


def main():
    limit_guesses = 10
    letters_index = []
    start()
    word = get_random_word()
    word_length = len(word)
    while limit_guesses > 0:
        letter_location = -1
        user_guess = input("Please enter letter:  ")
        for x in range(word_length):
            if word[x] == user_guess:
                letter_location = x
        if letter_location == -1:
            limit_guesses -= 1


if __name__ == "__main__":
    main()
