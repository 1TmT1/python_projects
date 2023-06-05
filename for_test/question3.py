def create_dict():
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    email = input("Enter e-mail: ")
    password = input("Enter password: ")
    dictionary = {"fname": name, "lname": last_name, "email": email, "password": password}
    return dictionary


def longest_lname(arr):
    max = 0
    index = 0
    for x in range(len(arr)):
        if len(arr[x]["lname"]) > max:
            max = len(arr[x]["lname"])
            index = x
    return arr[index]


def count_name(arr, name):
    count = 0
    for x in range(len(arr)):
        if name == arr[x]["fname"]:
            count += 1
    return count


def main():
    arr = []
    for x in range(5):
        dict = create_dict()
        arr.append(dict)
    ldict = longest_lname(arr)
    print(ldict)
    number = count_name(arr, 'tal')
    print(number)


if __name__ == "__main__":
    main()
