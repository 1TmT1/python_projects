def get_data():
    name = input("Enter your name:")
    last_name = input("Enter your last name:")
    email = input("Enter your email:")
    password = input("Enter your password:")
    dic = {"name": name, "last name": last_name, "email": email, "password": password}
    return dic


def longest_lastname(data):
    maxi = ""
    index = 0
    for x in range(len(data)):

        if len(maxi) < len(data[x]['last name']):
            maxi = data[x]['last name']
            index = x

    return data[index]


def is_name(data, name):
    counter = 0
    for x in range(len(data)):
        if data[x]['name'] == name:
            counter = counter + 1

    return counter


def main():
    data = []
    for i in range(2):
        data.append(get_data())
    print(longest_lastname(data))
    print(is_name(data, 'tal'))


if __name__ == "__main__":
    main()
