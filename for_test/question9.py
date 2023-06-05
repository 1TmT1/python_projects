def get_month(date):
    month = ''
    counter = 0
    for x in date:
        if 2 < counter < 5:
            month += x
        counter += 1
    if month[0] == '0':
        month = month[1]
    return int(month)


def main():
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    date = input('Enter date: ')
    while date != '00\\00\\0000':
        month = get_month(date)
        arr[month - 1] += 1
        date = input('Enter date: ')

    print(arr)


if __name__ == '__main__':
    main()
