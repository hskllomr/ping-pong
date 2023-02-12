import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Game")
wn.setup(width=800,height=600)
wn.tracer(0)

score=0
score2=0

kale=turtle.Turtle()
kale.speed(0)
kale.shape("square")
kale.color("white")
kale.shapesize(stretch_wid=5,stretch_len=1)
kale.penup()
kale.goto(350,0)

karsikale=turtle.Turtle()
karsikale.speed(0)
karsikale.shape("square")
karsikale.color("white")
karsikale.shapesize(stretch_wid=5,stretch_len=1)
karsikale.penup()
karsikale.goto(-350,0)

top=turtle.Turtle()
top.speed(0)
top.shape("square")
top.color("white")
top.penup()
top.goto(0,0)
top.dx=2
top.dy=-2

skor=turtle.Turtle()
skor.speed(0)
skor.color("white")
skor.penup()
skor.hideturtle()
skor.goto(0,260)
skor.write("Player A: 0 Player: 0",align="center",font=("Courier",24,"normal"))


def up():
    y=kale.ycor()
    y+=20
    kale.sety(y)

def down():
    y=kale.ycor()
    y-=20
    kale.sety(y)

def up2():
    y=karsikale.ycor()
    y+=20
    karsikale.sety(y)

def down2():
    y=karsikale.ycor()
    y-=20
    karsikale.sety(y)


wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(up2,"Up")
wn.onkeypress(down2,"Down")

while True:
    wn.update()

    #topun koordinatını güncelle
    top.setx(top.xcor()+top.dx)
    top.sety(top.ycor()+top.dy)

    # topun sektiği ya da karşıya geçtiği durum(Her bir uç için)
    if top.ycor()>290:
        top.sety(290)
        top.dy*=-1

    if top.ycor()<-290:
        top.sety(-290)
        top.dy*=-1

    if top.xcor()>390:
        top.goto(0,0)
        top.dx*=-1
        score=score+1
        skor.clear()
        skor.write("Player A:{} Player: B {}".format(score,score2),align="center",font=("Courier",24,"normal"))


    if top.xcor()<-390:
        top.goto(0,0)
        top.dx*=-1
        score2=score2+1
        skor.clear()
        skor.write("Player A:{} Player: B {}".format(score,score2),align="center",font=("Courier",24,"normal"))

    # top ile engelin çarpışması(engelin uzunluğu dikkate alınıyor)
    if (top.xcor()>340 and top.xcor()<350) and (top.ycor()<kale.ycor()+40 and top.ycor()>kale.ycor()-50):
        top.setx(340)
        top.dx*=-1

    if (top.xcor()<-340 and top.xcor()>-350) and (top.ycor()<karsikale.ycor()+40 and top.ycor()>karsikale.ycor()-50):
        top.setx(-340)
        top.dx*=-1


















