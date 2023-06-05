def main():
    try:
        write = input("What to write: ")
        amount = int(input("How many lines: "))

        file = open("text.txt", "w")
        for x in range(amount):
            file.write(str(x) + ". " + write + "\n")
        file.close()
    except:
        print("Error!-(")


if __name__ == "__main__":
    main()
