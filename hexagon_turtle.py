import turtle
window = turtle.Screen()
window.bgcolor('sky blue')
window.title('My classwork')
jaja = turtle.Turtle()
jaja.speed(5)
jaja.color('blue')
jaja.pensize(2)



def maggi(n):
    ang = (n-2)*180/n
    jaja.penup()
    jaja.backward(50)
    jaja.pendown()
    for i in range(n//2):
        jaja.forward(50)
        jaja.left(ang)
        jaja.backward(50)
        jaja.left(ang)
    if n % 2 == 1:
        jaja.forward(50)
        jaja.left(ang)
maggi(9)

window.mainloop()