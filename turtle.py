# An example of the use of turtle module :)
import turtle


window = turtle.Screen()
window.bgcolor("black")
    
brad = turtle.Turtle()
brad.color("black")


def draw_square(brad,colour,value,col):
    brad.shape("turtle")
    brad.color(colour)
    brad.speed(0.3)
    brad.forward(200)
    
    for i in range(72):
        for j in range(4):
            brad.forward(value)
            brad.right(90)

        brad.right(5)
    brad.color(a[col])
    brad.backward(200)




a = ["violet","indigo","blue","green","yellow","orange","red"]
angle = (360/7)
for m in range(7):
    draw_square(brad,a[m],70,m)
    brad.right(angle)


for n in range(7):
    draw_square(brad,"white",50,n)
    brad.right(angle)

brad.shape("circle")


