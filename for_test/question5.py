def digits(n):
    new_num = str(n)
    return len(new_num)


def maxi(numbers):
    max = 0
    index = 0
    for x in range(len(numbers)):
        sum = 0
        num = (digits(numbers[x]) ^ 10) / 10
        for y in range(digits(numbers[x])):
            number = numbers[x] % num
            number2 = int(numbers[x] / num)
            sum = number + number2
        if sum > max:
            max = sum
            index = x
    print(numbers[index])


def main():
    maxi([50, 100, 110, 99, 1111999, 12])


if __name__ == "__main__":
    main()
