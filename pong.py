import turtle

#parametry okna

okno=turtle.Screen()
okno.title("Paleto piłeczka")
okno.bgcolor("gray")
okno.setup(width=600, height=900)
okno.tracer(0)


#parametry paletki

paleta = turtle.Turtle()
paleta.speed(0)
paleta.shape("square")
paleta.color("black")
paleta.shapesize(stretch_len=5, stretch_wid=0.1)
paleta.penup()
paleta.goto(0, -420)

#piłka

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05  

#punktacja

wynik = 0
ptk = turtle.Turtle()
ptk.speed(0)
ptk.color("black")
ptk.penup()
ptk.hideturtle()
ptk.goto(250, 420)
ptk.write("Punkty: {}".format(wynik), align="right", font=("Courier", 12, "normal"))





#ruch
def paleta_move_right():
    x = paleta.xcor()
    x += 5
    paleta.setx(x)

def paleta_move_left():
    x = paleta.xcor()
    x -= 5
    paleta.setx(x)

# przypisanie do klawiatury
okno.listen()
okno.onkeypress(paleta_move_right, "Right")
okno.onkeypress(paleta_move_left, "Left")





while True:
    okno.update()

    #ruch piłki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # granice boiska
 
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    
    if ball.ycor() > 440:
        ball.sety(440)
        ball.dy *= -1
        
    if ball.ycor() < -440:
        wynik = 0
        ball.goto(0, 0)
        

    #odbijanie od paletki

    if (ball.ycor() < -410 and ball.ycor() > -420) and (ball.xcor() < paleta.xcor() + 40 and ball.xcor() > paleta.xcor() -40 ):
        wynik += 1
        ptk.clear()
        ptk.write("Punkty: {}".format(wynik), align="right", font=("Courier", 12, "normal"))
        ball.sety(-410)
        ball.dy *= -1.02