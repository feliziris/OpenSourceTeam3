import turtle
import time

distant = 95

colors = ['Red', 'Blue', 'Green']


def moveto(x, y, t1):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()


def move_t(x, y, t1):
    t1.pendown()
    t1.goto(x, y)


def original_dot(x, y):
    y = y - 3
    x = x - 1
    y = 0 + y * distant
    x = 0 + x * distant * -1

    return y, x


def draw_rect(t1):
    for i in range(4):
        t1.forward(10)
        t1.left(90)


def show(path_list):
    print("Start navigation")
    win = turtle.Screen()
    t1 = turtle.Turtle()

    win.setup(1000, 700)
    win.bgpic("route.gif")  # background 이미지 삽입
    t1.shape("circle")
    t1.speed(3)

    for idx, location in enumerate(path_list):
        t1.hideturtle()

        a, b = original_dot(location[0][0], location[0][1])
        moveto(a, b, t1)

        t1.showturtle()
        t1.color(colors[idx])

        for i in location:
            a, b = original_dot(i[0], i[1])
            move_t(a, b, t1)
            time.sleep(0.1)

        t1.write("대피로 {}".format(idx))


    t1.hideturtle()

    time.sleep(10)
