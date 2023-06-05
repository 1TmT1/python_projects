def main():
    a = 0
    b = 1
    while True:
        print(a)
        c = a + b
        a = b
        b = c
        if a >= 10000:
            break


if __name__ == "__main__":
    main()
