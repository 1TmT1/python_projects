def main():
    counter = 0
    s2 = str(input('Enter string: '))
    s1 = str(input('Enter string: '))
    for x in s1:
        if x in s2:
            counter += 1
    if counter == len(s1):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
