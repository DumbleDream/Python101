import turtle
turtle.getscreen().bgcolor('black')
turtle.shape('turtle')
tao = turtle.Pen()
tao.speed(0)
for i in range(60) :
    tao.color('white'); tao.circle(10)
    tao.color('green'); tao.circle(30)
    tao.color('pink'); tao.circle(50)
    tao.color('yellow'); tao.circle(70)
    tao.color('blue'); tao.circle(90)
    tao.lt(10)

    
