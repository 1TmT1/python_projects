class Ganenet(object):
    def __init__(self, name, city, salary):
        self.__name = name
        self.__city = city
        self.__salary = salary

    def add_bonus(self, bonus):
        self.__salary += bonus

    def __str__(self):
        return "ganenet name " + self.__name + " city " + self.__city + " salary " + str(self.__salary)


class KinderGarden(object):
    def __init__(self, name, kids, ganenet):
        self.__name = name
        self.__kids = kids
        self.__ganenet = ganenet

    def get_kids(self):
        return self.__kids

    def shift(self, other, n):
        if self.__kids <= 0:
            print("You can't transfer kids! ")
        else:
            self.__kids -= n
            other.__kids += n

    def get_ganenet(self):
        return self.__ganenet

    def __str__(self):
        return "gan name " + self.__name + " number of kids " + str(self.__kids) + ", ganenet: " + str(self.__ganenet)


def main():
    arr = []
    for x in range(5):
        name = input("enter name")
        city = input("enter city")
        salary = int(input("enter salary"))
        ganenet = Ganenet(name, city, salary)
        gan_name = input("enter gan name")
        kids = int(input("enter number of kids"))
        arr.append(KinderGarden(gan_name, kids, ganenet))

    max = 0
    index = 0
    for x in range(len(arr)):
        if arr[x].get_kids() > max:
            max = arr[x].get_kids()
            index = x
    print(arr[index])
    arr[index].get_ganenet().add_bonus(100)
    min = max
    index_min = 0
    for x in range(len(arr)):
        if min > arr[x].get_kids():
            min = arr[x].get_kids()
            index_min = x
    print(arr[index_min])
    arr[index].shift(arr[index_min], 5)
    print(arr[index_min])
    print(arr[index])


if __name__ == "__main__":
    main()
