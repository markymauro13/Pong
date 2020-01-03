import turtle

window = turtle.Screen()
window.title("Pong by Mark Mauro")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# Score
score1 = 0
score2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))


# functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 25
    paddle_1.sety(y)
def paddle_1_down():
    y = paddle_1.ycor()
    y -= 25
    paddle_1.sety(y)
def paddle_2_up():
    y = paddle_2.ycor()
    y += 25
    paddle_2.sety(y)
def paddle_2_down():
    y = paddle_2.ycor()
    y -= 25
    paddle_2.sety(y)

# keyboard binding
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= - 1
        score1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
