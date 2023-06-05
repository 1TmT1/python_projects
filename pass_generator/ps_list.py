def get_names(num_people):
    names = []
    for x in range(num_people):
        name = input("Enter the name:")
        name = name.lower()
        names.append(name)
    return names


def get_last_name():
    last_name = input("Enter the last name:")
    return last_name


def get_dates(num_people):
    dates = []
    for x in range(num_people):
        if x != num_people:
            date = input("Enter the date(DD/MM/YY):")
            dates.append(date)
    return dates


def get_phone_numbers(num_people):
    phone_numbers = []
    x = 0
    while x < num_people:
        try:
            temp_phone_number = input("Enter a phone number:")
            phone_number = temp_phone_number
            temp_phone_number = str(int(temp_phone_number))
            phone_numbers.append(phone_number)
            x += 1
        except:
            print("Enter valid phone number!")
    return phone_numbers


def detail_dates(dates):
    det_dates = []
    for x in range(len(dates)):
        date = dates[x].split("/")
        if len(date) != 3:
            print("Invalid date entered {}".format('/'.join(date)))
        else:
            det_dates.append(date)
    return det_dates


# [[12,15,1990], [15,15,1550]]
def c_dates(dates):
    c = []
    for x in range(len(dates)):
        for j in range(len(dates[x])):
            if j == 0:
                for z in range(len(dates)):
                    for a in range(len(dates)):
                        year1 = list(dates[a][2])
                        year2 = list(dates[z][2])
                        c.append(dates[x][j] + dates[z][1] + dates[a][2])
                        c.append(dates[x][j] + dates[z][2] + dates[a][1])
                        c.append(dates[x][j] + dates[z][1] + year1[2] + year1[3])
                        c.append(dates[x][j] + year2[2] + year2[3] + dates[a][2])
                        c.append(dates[x][j] + dates[z][1])
            elif j == 1:
                for z in range(len(dates)):
                    for a in range(len(dates)):
                        year1 = list(dates[z][2])
                        year2 = list(dates[a][2])
                        c.append(dates[x][j] + dates[z][2] + dates[a][0])
                        c.append(dates[x][j] + dates[z][0] + dates[a][2])
                        c.append(dates[x][j] + year1[2] + year1[3] + dates[a][0])
                        c.append(dates[x][j] + dates[z][0] + year2[2] + year2[3])
            else:
                for z in range(len(dates)):
                    for a in range(len(dates)):
                        year = list(dates[x][j])
                        c.append(dates[x][j] + dates[z][0] + dates[a][1])
                        c.append(dates[x][j] + dates[z][1] + dates[a][0])
                        c.append(year[2] + year[3] + dates[z][0] + dates[a][1])
                        c.append(year[2] + year[3] + dates[z][1] + dates[a][0])
    return c


def generate_passwords(names, dates, phone_numbers, file):
    file = open(file, 'w')
    comb_dates = c_dates(dates)
    phone_numbers.append('')
    for x in range(len(names)):
        file.write(names[x])
        file.write(phone_numbers[x])
        for j in comb_dates:
            file.write(''.join(j) + "\n")
            file.write(names[x] + ''.join(j) + "\n")
            file.write(names[x] + ''.join(j) + phone_numbers[x] + "\n")
            file.write(names[x] + phone_numbers[x] + ''.join(j) + "\n")
            file.write(phone_numbers[x] + names[x] + ''.join(j) + "\n")
            file.write(''.join(j) + names[x] + "\n")
            if x != (len(names) - 1):
                letters = list(names[x])
                last_letters = list(names[len(names) - 1])
                file.write(letters[0] + last_letters[0] + phone_numbers[x] + "\n")
                file.write(letters[0] + phone_numbers[x] + last_letters[0] + "\n")
                file.write(phone_numbers[x] + letters[0] + last_letters[0] + "\n")
                file.write(letters[0] + last_letters[0] + "\n")
                file.write(last_letters[0] + letters[0] + "\n")
                file.write(last_letters[0] + letters[0] + phone_numbers[x] + "\n")
                file.write(last_letters[0] + phone_numbers[x] + letters[0] + "\n")
                file.write(phone_numbers[x] + last_letters[0] + letters[0] + "\n")
                file.write(last_letters[0] + letters[0] + ''.join(j) + "\n")
                file.write(last_letters[0] + letters[0] + ''.join(j) + phone_numbers[x] + "\n")
                file.write(last_letters[0] + letters[0] + phone_numbers[x] + ''.join(j) + "\n")
                file.write(last_letters[0] + phone_numbers[x] + letters[0] + ''.join(j) + "\n")
                file.write(phone_numbers[x] + last_letters[0] + letters[0] + ''.join(j) + "\n")
                file.write(''.join(j) + last_letters[0] + letters[0] + "\n")
                file.write(''.join(j) + last_letters[0] + letters[0] + phone_numbers[x] + "\n")
                file.write(''.join(j) + last_letters[0] + phone_numbers[x] + letters[0] + "\n")
                file.write(''.join(j) + phone_numbers[x] + last_letters[0] + letters[0] + "\n")
                file.write(phone_numbers[x] + ''.join(j) + last_letters[0] + letters[0] + "\n")
                file.write(''.join(j) + letters[0] + last_letters[0] + "\n")
                file.write(''.join(j) + letters[0] + last_letters[0] + phone_numbers[x] + "\n")
                file.write(''.join(j) + letters[0] + phone_numbers[x] + last_letters[0] + "\n")
                file.write(''.join(j) + phone_numbers[x] + letters[0] + last_letters[0] + "\n")
                file.write(phone_numbers[x] + ''.join(j) + letters[0] + last_letters[0] + "\n")
                file.write(letters[0] + last_letters[0] + ''.join(j) + "\n")
                file.write(letters[0] + last_letters[0] + ''.join(j) + phone_numbers[x] + "\n")
                file.write(letters[0] + last_letters[0] + phone_numbers[x] + ''.join(j) + "\n")
                file.write(letters[0] + phone_numbers[x] + last_letters[0] + ''.join(j) + "\n")
                file.write(phone_numbers[x] + letters[0] + last_letters[0] + ''.join(j) + "\n")
    file.close()


def check_dupes(input_file, output_file):
    lines_seen = set()
    output_file = open(output_file, "w")
    for each_line in open(input_file, "r"):
        if each_line not in lines_seen:
            output_file.write(each_line)
            lines_seen.add(each_line)
    output_file.close()


def main():
    try:
        num_people = int(input("Enter number of people: "))
        names = get_names(num_people)
        names.append(get_last_name())
        dates = get_dates(num_people)
        phone_numbers = get_phone_numbers(num_people)
        dates = detail_dates(dates)
        generate_passwords(names, dates, phone_numbers, "temp_passes.txt")
        check_dupes("temp_passes.txt", "passes.txt")
    except:
        print("Error, probably didn't entered a number...")


if __name__ == "__main__":
    main()
