def main():
    num = input("Enter number: ")
    sum = 0
    counter = 0
    while num is not 'q':
        sum += int(num)
        counter += 1
        num = input("Enter number: ")
    sum = sum / counter
    print(sum)


if __name__ == "__main__":
    main()
