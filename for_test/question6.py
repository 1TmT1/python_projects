def main():
    counter = 0
    for x in range(25):
        num = int(input('Enter number: '))
        if abs(num - (x + 1)) <= 2:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
