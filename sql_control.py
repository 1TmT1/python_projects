# run it with python 3.6
import sqlite3
import tkinter as tk
from tkinter import ttk
import random


class Users(object):
    def __init__(self, table_name, user_id, username, password, firstname, lastname):
        self.__table_name = table_name
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__firstname = firstname
        self.__lastname = lastname
        connection = sqlite3.connect("database.db")
        print("Opened database successfully!")
        c = connection.cursor()
        string = """CREATE TABLE IF NOT EXISTS {}({} INTEGER PRIMARY KEY AUTOINCREMENT, {} TEXT NOT NULL, {} TEXT NOT NULL, {} TEXT NOT NULL, {} TEXT NOT NULL);""".format(
            self.__table_name, self.__user_id, self.__username, self.__password, self.__firstname, self.__lastname)
        c.execute(string)
        print("Table created successfully!")
        connection.commit()
        connection.close()

    def insert_user(self, username, password, firstname, lastname):
        connection = sqlite3.connect("database.db")
        str_insert = """INSERT INTO {}({}, {}, {}, {}) VALUES ("{}\", "{}\", "{}\", "{}\")""".format(self.__table_name, self.__username, self.__password, self.__firstname, self.__lastname, username, password, firstname, lastname)
        print(str_insert)
        connection.execute(str_insert)
        connection.commit()
        connection.close()
        print("Record completed successfully!")

    def select_by_user_and_password(self):
        connection = sqlite3.connect("database.db")
        str_select = """SELECT {}, {} FROM {}""".format(self.__username, self.__password, self.__table_name)
        print(str_select)
        cursor = connection.cursor()
        cursor.execute(str_select)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        print("Record completed successfully!")
        return data

    def get_all_users(self):
        connection = sqlite3.connect("database.db")
        str_select = """SELECT * FROM {}""".format(self.__table_name)
        print(str_select)
        cursor = connection.cursor()
        cursor.execute(str_select)
        all_users = cursor.fetchall()
        connection.commit()
        connection.close()
        print("Record completed successfully!")
        return all_users

    def delete_by_user_id(self, user_id):
        connection = sqlite3.connect("database.db")
        str_delete = """DELETE FROM {} WHERE {}=?""".format(self.__table_name, self.__user_id)
        cursor = connection.cursor()
        cursor.execute(str_delete, (user_id,))
        connection.commit()
        connection.close()
        print("Record deleted successfully!")

    def get_max_id(self):
        connection = sqlite3.connect("database.db")
        str_select = """SELECT MAX({}) FROM {}""".format(self.__user_id, self.__table_name)
        cursor = connection.cursor()
        cursor.execute(str_select)
        return cursor.fetchone()[0]

    # def delete_by_price(self, price):
    #     connection = sqlite3.connect("database.db")
    #     str_delete = """DELETE FROM {} WHERE {} == \"{}\"""".format(self.__table_name, self.__price, price)
    #     connection.execute(str_delete)
    #     connection.commit()
    #     connection.close()
    #    print("Record completed successfully!")

    # def update_car(self, car_id, color, model, price):
    #     connection = sqlite3.connect("database.db")
    #     str_update = """UPDATE {} set {}="{}", {}="{}", {}={} WHERE {}=={}""".format(self.__table_name, self.__color,
    #                                                                                  color, self.__model, model,
    #                                                                                  self.__price, price, self.__car_id,
    #                                                                                  car_id)
    #     connection.execute(str_update)
    #     connection.commit()
    #     connection.close()
    #     print("Record completed successfully!")


table_users = Users("Users", "user_id", "username", "password", "firstname", "lastname")
top = tk.Tk()
top.withdraw()
cols = ('User_Id', 'Username', 'Password', 'Firstname', 'Lastname')
listBox = ttk.Treeview(top, columns=cols, show='headings')
colors = {"red": "red", "green": "green", "pink": "pink", "teal": "teal", "cyan": "cyan", "tomato2": "tomato2", "snow": "snow", "gold": "gold"}
try:
    user_id = table_users.get_max_id() + 1
except:
    user_id = 1
print(user_id)
login = tk.Tk()
login.withdraw()
wrong_pass = tk.Label(login, text="Wrong username or password :-(")
main_win = tk.Tk()
main_win.withdraw()
register = tk.Tk()
register.withdraw()


def insert(username, password, firstname, lastname):
    global user_id
    user_id += 1
    key = random.choice(list(colors.keys()))
    table_users.insert_user(username.get(), password.get(), firstname.get(), lastname.get())
    listBox.tag_configure(key, background=colors[key])
    listBox.insert(parent="", index="end", values=(user_id, username.get(), password.get(), firstname.get(), lastname.get()), tags=(key,))
    username.delete(0, len(username.get()))
    password.delete(0, len(password.get()))
    firstname.delete(0, len(firstname.get()))
    lastname.delete(0, len(lastname.get()))


def insert_from_table(user_id, username, password, firstname, lastname):
    key = random.choice(list(colors.keys()))
    listBox.tag_configure(key, background=colors[key])
    listBox.insert("", "end", values=(user_id, username, password, firstname, lastname), tags=(key,))


def disable_event():
    pass


def popup():
    temp = tk.Tk()
    temp.resizable(0, 0)
    temp.protocol("WM_DELETE_WINDOW",)
    frame = tk.Frame(temp)
    frame.pack(side="left")
    temp.geometry("250x100")
    label = tk.Label(temp, padx=10, text="Are you sure you want to delete the current selected user?")
    label.pack()
    yes_btn = tk.Button(temp, text="Yes", bg="light blue", fg="red", command=lambda: delete_selected(temp), width=10)
    yes_btn.pack(padx=10, pady=10, side="left")
    no_btn = tk.Button(temp, text="No", bg="light blue", fg="red", command=temp.destroy, width=10)
    no_btn.pack(padx=10, pady=10, side="left")
    temp.protocol("WM_DELETE_WINDOW", disable_event)
    temp.mainloop()


def delete_selected(win):
    selected_items = listBox.selection()
    for selected_item in selected_items:
        current_user_id = listBox.item(selected_item)["values"][0]
        table_users.delete_by_user_id(current_user_id)
        listBox.delete(selected_item)
    win.destroy()


def check_credentials(users_table, username, password):
    username_entered = username.get()
    password_entered = password.get()
    users = users_table.select_by_user_and_password()
    for user in users:
        if user[0] == username_entered and user[1] == password_entered:
            login.withdraw()
            table_win()
    wrong_pass.grid(row=4)


def exit_login():
    login.withdraw()
    wrong_pass.grid_forget()
    main()


def login_win():
    main_win.withdraw()
    login.update()
    login.deiconify()
    login.overrideredirect(1)
    login.geometry("500x200")
    login.title("login")
    login.configure(background=random.choice(list(colors.values())))
    et_username = tk.Entry(login)
    et_username.place(x=200, y=15)
    et_username.insert(0, 'Enter username:')
    et_password = tk.Entry(login)
    et_password.place(x=200, y=40)
    et_password.insert(0, 'Enter password:')
    quit_button = tk.Button(login, text="Exit Window", width=17, background="red", fg="black", command=lambda: exit_login())
    quit_button.place(x=200, y=100)
    check = tk.Button(login, text="Login", width=17, command=lambda: check_credentials(table_users, et_username, et_password))
    check.place(x=200, y=65)
    login.mainloop()


def exit_register():
    register.withdraw()
    main()


def exit_table_win():
    top.withdraw()
    for i in listBox.get_children():
        listBox.delete(i)
    login_win()


def register_win():
    main_win.withdraw()
    register.update()
    register.deiconify()
    register.geometry("500x200")
    register.title("register")
    register.resizable(0, 0)
    register.configure(background=random.choice(list(colors.values())))
    et_username = tk.Entry(register)
    et_username.place(x=200, y=10)
    et_username.insert(0, 'Enter username:')
    et_password = tk.Entry(register)
    et_password.place(x=200, y=35)
    et_password.insert(0, 'Enter password:')
    et_firstname = tk.Entry(register)
    et_firstname.place(x=200, y=60)
    et_firstname.insert(0, 'Enter firstname:')
    et_lastname = tk.Entry(register)
    et_lastname.place(x=200, y=85)
    et_lastname.insert(0, 'Enter lastname:')
    addLine = tk.Button(register, text="Register", width=15, command=lambda: insert(et_username, et_password, et_firstname, et_lastname))
    addLine.place(x=200, y=125)
    quit_button = tk.Button(register, text="Exit window", background="red", width=15, command=exit_register)
    quit_button.place(x=200, y=150)
    register.mainloop()


def table_win():
        top.update()
        top.deiconify()
        top.overrideredirect(1)
        top.geometry("1025x500")
        top.title("users")
        top.configure(background=random.choice(list(colors.values())))
        check_table(table_users)
        et_username = tk.Entry(top)
        et_username.grid(row=2)
        et_username.insert(0, 'Enter username:')
        et_password = tk.Entry(top)
        et_password.grid(row=3)
        et_password.insert(0, 'Enter password:')
        et_firstname = tk.Entry(top)
        et_firstname.grid(row=4)
        et_firstname.insert(0, 'Enter firstname:')
        et_lastname = tk.Entry(top)
        et_lastname.grid(row=5)
        et_lastname.insert(0, 'Enter lastname:')
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0)
        addLine = tk.Button(top, text="Add Person", width=15, command=lambda: insert(et_username, et_password, et_firstname, et_lastname))
        addLine.grid(row=6, column=0)
        delete = tk.Button(top, text="Delete selected user", width=17, background="blue", fg="white", command=popup)
        delete.grid(row=7, column=0)
        quit_button = tk.Button(top, text="Exit Window", width=17, background="red", fg="black", command=exit_table_win)
        quit_button.grid(row=8, column=0)
        top.mainloop()


def check_table(table):
    users = table.get_all_users()
    for user in users:
        uid = user[0]
        username = user[1]
        password = user[2]
        firstname = user[3]
        lastname = user[4]
        insert_from_table(uid, username, password, firstname, lastname)


def main():
    main_win.update()
    main_win.deiconify()
    main_win.geometry("500x200")
    main_win.title("main")
    main_win.resizable(0, 0)
    main_win.configure(background=random.choice(list(colors.values())))
    register_new = tk.Button(main_win, text="Register user", width=15, command=register_win)
    register_new.place(x=200)
    login = tk.Button(main_win, text="Login", width=15, command=login_win)
    login.place(x=200, y=85)
    exit_button = tk.Button(main_win, text="Exit window", width=15, background="tomato2", command=main_win.destroy)
    exit_button.place(x=200, y=175)
    main_win.protocol("WM_DELETE_WINDOW", disable_event)
    main_win.mainloop()


if __name__ == "__main__":
    main()
