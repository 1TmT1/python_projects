def main():
    print("0")
    for x in range(0, 5):
        for j in range(1, 11):
            if j != 10:
                print(str(x) + "." + str(j))
            else:
                print(str(x + 1))
    print()


if __name__ == "__main__":
    main()
