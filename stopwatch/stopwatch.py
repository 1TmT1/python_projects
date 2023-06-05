import tkinter as tk
import threading
import time
import sys
import random
import winsound


top = tk.Tk()
minutes_label = tk.Label(top, text="minutes", background="gold")
minutes_label.place(x=80+70+20, y=75)
minutes = tk.Entry(top, font=('arial', 30), width=5)
minutes.focus()
minutes.place(x=80+35+20, y=100)
seconds_label = tk.Label(top, text="seconds", background="gold")
seconds_label.place(x=80+70+20+120, y=75)
seconds = tk.Entry(top, font=('arial', 30), width=5)
seconds.place(x=80+35+20+120, y=100)
is_running = False
first_run = False
number_minutes = minutes.get()
number_seconds = seconds.get()
quitp=False
colors = ["red", "green", "pink", "teal", "cyan", "tomato2", "snow", "gold"]


def exit_program(popup_win):
    global quitp
    popup_win.destroy()
    quitp = True
    main()


def disable_event():
    pass


def popup():
    temp = tk.Tk()
    temp.resizable(0, 0)
    frame = tk.Frame(temp)
    frame.pack(side="left")
    temp.geometry("250x100")
    label = tk.Label(temp, padx=10, text="Are you sure you want to exit the TIMER?")
    label.pack()
    yes_btn = tk.Button(temp, text="Yes", bg="light blue", fg="red", width=10, command=lambda: exit_program(temp))
    yes_btn.pack(padx=10, pady=10, side="left")
    no_btn = tk.Button(temp, text="No", bg="light blue", fg="red", command=temp.destroy, width=10)
    no_btn.pack(padx=10, pady=10, side="left")
    temp.protocol("WM_DELETE_WINDOW", disable_event)
    temp.mainloop()


def start_timer():
    global minutes, seconds, number_minutes, number_seconds, first_run, first_run, minutes_label, seconds_label
    minutes.configure(state=tk.DISABLED)
    seconds.configure(state=tk.DISABLED)
    if not first_run:
        number_seconds = seconds.get()
        number_minutes = minutes.get()
        first_run = True
    temp_number_minutes = int(minutes.get())
    temp_number_seconds = int(seconds.get())
    total_seconds = temp_number_seconds + temp_number_minutes * 60
    time.sleep(1)
    for x in range(total_seconds):
        if not is_running:
            return None
        elif temp_number_seconds == 0:
            seconds.configure(state=tk.NORMAL)
            seconds.delete(0, "end")
            seconds.insert(0, "59")
            seconds.configure(state=tk.DISABLED)
            minutes.configure(state=tk.NORMAL)
            minutes.delete(0, "end")
            minutes.insert(0, str(temp_number_minutes-1))
            minutes.configure(state=tk.DISABLED)
            minutes_label.configure(background=random.choice(colors))
            seconds_label.configure(background=random.choice(colors))
            temp_number_seconds = 59
        else:
            temp_number_seconds -= 1
            seconds.configure(state=tk.NORMAL)
            seconds.delete(0, "end")
            seconds.insert(0, str(temp_number_seconds))
            seconds.configure(state=tk.DISABLED)
            seconds_label.configure(background=random.choice(colors))
        time.sleep(1)
    frequency = 250
    duration = 500
    winsound.Beep(frequency, duration)
    popup()


t1 = threading.Thread(target=start_timer)


def start_timer_thread():
    global is_running, t1, first_run
    try:
        temp_minutes = int(minutes.get())
        temp_seconds = int(seconds.get())
        if not first_run:
            is_running = True
            t1.start()
        else:
            if t1.is_alive():
                pass
            else:
                t1 = threading.Thread(target=start_timer)
                is_running = True
                t1.start()
    except:
        print("You didn't put whole numbers!")


def stop_timer_thread():
    global is_running
    is_running = False


def reset_timer():
    stop_timer_thread()
    minutes.configure(state=tk.NORMAL)
    minutes.delete(0, "end")
    minutes.insert(0, number_minutes)
    seconds.configure(state=tk.NORMAL)
    seconds.delete(0, "end")
    seconds.insert(0, number_seconds)


def main():
    global quitp
    if quitp:
        top.destroy()
        sys.exit(0)
    top.title("Timer")
    top.geometry("500x400")
    start = tk.Button(top, background="light green", text="start", width=15, command=start_timer_thread)
    start.place(x=80, y=250)
    reset = tk.Button(top, background="blue", fg="white", text="reset", width=15, command=reset_timer)
    reset.place(x=205, y=250)
    stop = tk.Button(top, background="tomato2", text="stop", width=15, command=stop_timer_thread)
    stop.place(x=330, y=250)
    top.mainloop()


if __name__ == "__main__":
    main()
