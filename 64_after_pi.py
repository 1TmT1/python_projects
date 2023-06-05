import math


def main():
    # gets the 14th digit of pi after the dot

    # index numbers - 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    # actual index number after dot - 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    # actual numbers after dot - 1 4 1 5 9 2 6 5 3 5 8 9 7 9

    pi = str(math.pi).split('.')[1]
    sum = 0
    for x in range(len(pi)):
        if x == 1:
            sum += int(pi[x])
        elif x == 13:
            sum += int(pi[x])
    print(math.pi)
    print(sum)


if __name__ == "__main__":
    main()
