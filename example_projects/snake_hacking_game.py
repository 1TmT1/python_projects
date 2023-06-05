import turtle
import keyboard
import time
import threading


def main():
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Snake Hacking Tool")
    window.setup(700, 700)

    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.color("blue")
            self.shape("square")
            self.penup()
            self.speed(0)

    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(0)

        def go_down(self):
            self.goto(self.xcor(), self.ycor() - 24)

        def go_right(self):
            self.goto(self.xcor() + 24, self.ycor())

        def go_left(self):
            self.goto(self.xcor() - 24, self.ycor())

    levels = [""]

    level_1 = [
        "xxxxxxxxxpxxxxxxxxxxxxxxx",
        "xxxxx      xxxxxxx   xxxx",
        "xx  x  xx   xxxx      xxx",
        "   xx  xxxx  xxxxxx  xxxx",
        "xxxxxxxxxxxx xxxxxx xxxxx",
        "xxxx xxxx xx    xxxxxxxxx",
        "xxxxxxxx x    x    xxxxxx",
        "xxxxxxxx    x  xxx xxxxxx",
        "xxx x  x x xxxxxxx xxxxxx",
        "xxxxxxxx xxx       xx xxx",
        "xxxxxxxxxx   xxxxxxxx  xx",
        "xxxxxxxxxx       xxxxxxxx",
        "xxxxx           xxxxxxxxx",
        "xxxxxxx    xxxxxxxxx  xxx",
        "xxxxxxxx          xx  xxx",
        "xxxxxxx     xx   xxxxxxxx",
        "xxxxx    xxxxxx  xxxxxxxx",
        "xxxx   xxxxxxxxx xxxxxxxx",
        "xxx        xxxxx  xxxxxxx",
        "xxxxxxx   xxxxxx  xxxxxxx",
        "xxxxxxxx     xxxxx xxxxxx",
        "xxxxxxxxxxx    xxx    xxx",
        "xxxxxxx       xxxxxx  xxx",
        "xxxxxxxxxx   xxxxxxxxxxxx",
        "xxxxxxxxxx xxxxxxxxxxxxxx",
    ]

    levels.append(level_1)

    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "x":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    walls.append((screen_x, screen_y))

                if character == "p":
                    player.goto(screen_x, screen_y)

    def movement():
        if keyboard.is_pressed('LEFT'):
            move_x = player.xcor() - 24
            move_y = player.ycor()
            if (move_x, move_y) not in walls:
                player.go_left()
            else:
                player.color("black")
                time.sleep(1.5)
                player.color("white")
                time.sleep(1)
                player.color("black")
                return True
        elif keyboard.is_pressed("RIGHT"):
            move_x = player.xcor() + 24
            move_y = player.ycor()
            if (move_x, move_y) not in walls:
                player.go_right()
            else:
                player.color("black")
                time.sleep(1.5)
                player.color("white")
                time.sleep(1)
                player.color("black")
                return True

    walls = []
    pen = Pen()
    player = Player()
    setup_maze(levels[1])

    while True:
        try:
            is_hit = movement()
            if is_hit:
                walls = []
                window.clear()
                window.bgcolor("black")
                player = Player()
                setup_maze(levels[1])
        except:
            pass
        window.update()


if __name__ == "__main__":
    main()
