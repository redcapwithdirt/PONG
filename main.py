import os
import turtle

win = turtle.Screen()
win.title("@redcapwithdirt")
win.bgcolor("pink")
win.setup(width = 800,height = 600)
win.tracer(0)

#PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
# ball.shapesize(stretch_wid = 5,stretch_len = 1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2


# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("0 : 0", align = "center", font=("Courier", 24, "normal"))

def paddle_a_up():
	y = paddle_a.ycor()
	y = y + 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y = y - 20
	paddle_a.sety(y)


def paddle_b_up():
	y = paddle_b.ycor()
	y = y + 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y = y - 20
	paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")



# SCORE
score_a = 0 
score_b = 0

# MAIN GAME LOOP
while True:
	win.update()


	# MOVE THE BALL
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# BORDER CHECKING
	if(ball.ycor()>280):
		ball.sety(280)
		ball.dy *= -1
		os.system("aplay bounce.wav&")

	if(ball.ycor()<-280):
		ball.sety(-280)
		ball.dy *= -1
		os.system("aplay bounce.wav&")

	if(ball.xcor()>399):
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("{} : {}".format(score_a,score_b), align = "center", font=("Courier", 24, "normal"))


	if(ball.xcor()<-399):
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("{} : {}".format(score_a,score_b), align = "center", font=("Courier", 24, "normal"))


	# PADDLE AND BALL COLLISION
	if(ball.xcor()>330 and ball.xcor()<340) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
		ball.setx(330)
		ball.dx *= -1
		os.system("aplay bounce.wav&")

	if(ball.xcor()<-330 and ball.xcor()>-340) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
		ball.setx(-330)
		ball.dx *= -1
		os.system("aplay bounce.wav&")

