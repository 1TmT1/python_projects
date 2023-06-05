# import all the modules needed in order to run the program
import random
import string


# return a random letter (a, b, c) upper or lower
def get_random_letter():
    random_num = random.randint(0, 1)
    if random_num == 0:
        letter = random.choice(string.ascii_lowercase)
    else:
        letter = random.choice(string.ascii_uppercase)
    return letter


# return a random number (0 => 9)
def get_random_number():
    random_number = random.randint(0, 9)
    return random_number


# return a random sign (example: @)
def get_random_sign():
    return random.choice(string.punctuation)


# check if every letter in the password is upper, then if all the letters are upper it will change the first to a lower case
def every_letter_upper(password, num_letters):
    upper_counter = 0
    for x in password:
        if x.isupper():
            upper_counter += 1
        if upper_counter == num_letters:
            break

    if upper_counter == num_letters:
        for x in range(len(password)):
            if password[x].isupper():
                password = list(password)
                password[x] = password[x].lower()
                password = "".join(password)
                break
    return password


# check if every letter in the password is lower, then if all the letters are lower it will change the first to a upper case
def every_letter_lower(password, num_letters):
    lower_counter = 0
    for x in password:
        if x.islower():
            lower_counter += 1
        if lower_counter == num_letters:
            break

    if lower_counter == num_letters:
        for x in range(len(password)):
            if password[x].islower():
                password = list(password)
                password[x] = password[x].upper()
                password = "".join(password)
                break
    return password


# call for the functions that check the letters and return the new password
def check_password(password, num_letters):
    password = every_letter_upper(password, num_letters)
    password = every_letter_lower(password, num_letters)
    return password


# check if the input of the number of letters and the number of digits is o.k.
def check_num_letters_numbers(password_length):
    is_num_letters = False
    is_num_numbers = False
    num_letters = 0
    while not is_num_letters or not is_num_numbers:
        if not is_num_letters and not is_num_numbers:
            num_letters = int(input("Enter number of letters(less than " + str(password_length) + "): "))
            if num_letters < password_length:
                num_numbers = int(
                    input("Enter number of numbers(less than " + str(password_length - num_letters) + "): "))
                if (password_length - num_letters - num_numbers) > 0:
                    return num_letters, num_numbers
                elif (password_length - num_letters) <= 0:
                    continue
                else:
                    is_num_letters = True
            else:
                print("You entered number of letter that greater by " + str(num_letters - password_length) + " from the password length.")
                continue
        else:
            num_numbers = int(
                input("Enter number of numbers(less than " + str(password_length - num_letters) + "): "))
            if (password_length - num_letters - num_numbers) > 0:
                return num_letters, num_numbers


# main function - calls to the functions in order to create a unique password!
def main():
    try:
        password_length = int(input("How many characters for your password(minimum 6): "))
        if password_length >= 6:
            num_letters, num_numbers = check_num_letters_numbers(password_length)
            temp_num_letters = num_letters
            sum_letters_numbers = temp_num_letters + num_numbers
            password = ""
            if (num_numbers + temp_num_letters) < password_length:
                for x in range(password_length):
                    if temp_num_letters > 0:
                        password += get_random_letter()
                        temp_num_letters -= 1
                    if num_numbers > 0:
                        password += str(get_random_number())
                        num_numbers -= 1
                    if sum_letters_numbers < password_length:
                        password += get_random_sign()
                        sum_letters_numbers += 1
                if password.isupper() and not password.islower():
                    letter = 1
                    for x in password:
                        if letter == 1:
                            if str.isalpha(x):
                                num = random.randint(0, 1)
                                if num == 1:
                                    x.lower()
                                    letter -= 1
                        else:
                            break
                elif not password.isupper() and password.islower():
                    letter = 1
                    for x in password:
                        if letter == 1:
                            if str.isalpha(x):
                                num = random.randint(0, 1)
                                if num == 1:
                                    x.upper()
                                    letter -= 1
                        else:
                            break
                if password_length <= 50:
                    password = check_password(password, num_letters)
                print(password)
            else:
                print("Type normal letter size - (length - 10, number of letters - 4, number of numbers - 2)!")
        else:
            print("You didn't type good length - the minimum password length is 6!")
    except:
        print("Error, please enter a whole valid number...")


# calls the main function
if __name__ == "__main__":
    main()
