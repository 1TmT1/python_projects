from itertools import product

# string = str(input("Please enter the possibilities[1,x,2]:"))


def win_draw_lose_game():
    string = ["1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2",
              "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2", "1", "x", "2",
              "1", "x", "2", "1", "x", "2"]

    prod = list(product(string, repeat=3))
    counter = 0
    for ele in prod:
        print("".join(ele), end=' ')
        counter += 1
        if counter % 6 == 0:
            print()
    print()
    print(counter)
    print(int(counter) * 3)


def draw_game():
    string = ""
    for x in range(1, 34):
        if x < 33:
            string += str(x) + ","
        else:
            string += str(x)
    string = string.split(",")
    print(string)
    prod = list(product(string, repeat=7))
    counter = 0
    for ele in prod:
        print("".join(ele), end=' ')
        counter += 1
        if counter % 6 == 0:
            print()
    print()
    print(counter)
    print(int(counter) * 3)


def main():
    draw_game()


if __name__ == "__main__":
    main()
