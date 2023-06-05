from tkinter import *

points = 0
top = Tk()
img = PhotoImage(file="winner.png")
image_label = Label(top, image=img)
score = Label(top, background="black", fg="SystemButtonFace", text="score: {}".format(points))
score.pack()


def start(label):
    global restart, points
    restart.pack_forget()
    points = 0
    top.configure(background="black")
    label.configure(background="black", fg="SystemButtonFace", text="score: {}".format(points))
    image_label.pack_forget()


restart = Button(top, text="Play Again!", width=25, command=lambda: start(score))


def add_point(label):
    global points, up
    if points < 9:
        points += 1
        label.config(text="score: {}".format(points))
    elif points == 9:
        points += 1
        top.configure(background="SystemButtonFace")
        label.config(background="SystemButtonFace", fg="black", text="score: {}".format(points))
        show_image()
        play_again()


def increment_point(label):
    global points
    if points > 0 and points != 10:
        points -= 1
        label.config(text="score: {}".format(points))
    elif points == 10:
        label.config(text="score: {}".format(points))


def show_image():
    image_label.pack()


def play_again():
    global restart
    restart.pack()


def main():
    global top, image_label
    top.geometry("500x500")
    top.title("Points Counter")
    top.configure(background="black")
    up = Button(top, text="Add One Point!", width=25, command=lambda: add_point(score), activebackground="light green")
    up.pack()
    down = Button(top, text="Increment One Point!", width=25, command=lambda: increment_point(score), activebackground="salmon")
    down.pack()
    top.mainloop()


if __name__ == "__main__":
    main()
