import abc


class Employee:
    def __init__(self, name, address, salary):
        self.__name = name
        self.__address = address
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_salary(self):
        return self.__salary

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_salary(self, salary):
        self.__salary = salary

    @abc.abstractmethod
    def compute_salary(self):
        pass


class Teacher(Employee):
    def __init__(self, name, address, profession):
        Employee.__init__(self, name, address, 0)
        self.__profession = profession
        print(self.__name)

    def compute_salary(self):
        Employee.set_salary(self, 20000)

    def get_profession(self):
        return self.__profession

    def set_profession(self, profession):
        self.__profession = profession


class Programmer(Employee):
    def __init__(self, name, address, language):
        Employee.__init__(self, name, address, 0)
        self.__language = language

    def compute_salary(self):
        Employee.set_salary(self, 18000)

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language


def main():
    teacher1 = Teacher("helen", "hanegev", "physics")
    teacher2 = Teacher("drake", "popstar", "music")
    programmer1 = Programmer("Tal", "prog", "python")
    employees = [teacher1, teacher2, programmer1]
    total_teacher_salary = 0
    for employee in employees:
        if isinstance(employee, Teacher):
            total_teacher_salary += employee.get_salary()
    print(total_teacher_salary)


if __name__ == "__main__":
    main()
