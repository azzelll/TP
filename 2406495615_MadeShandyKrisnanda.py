import turtle as t
import random as r

t.pensize(10)
t.title("Olympic Logo and Colorful Chessboard")
t.speed(0)
t.colormode(255)

#memasukan warna sesuai dengan kode RGB ke dalam variable dan list
biru = 0,129,200
kuning = 252,177,49
hitam = 0,0,0,
merah = 0,166,81
hijau = 238,51,78
pen_color = [biru, kuning, hitam, merah, hijau]

#membuat fungsi untuk membuat logo olimpiade bergelomvbang serta membuat menjadi interlock
def olympic_wave():
    t.penup()
    t.goto(-100,-50)
    t.pendown()
    for i in range(3):
        t.pencolor(pen_color[i*2])
        t.circle(50)
        t.penup()
        t.forward(125)
        t.pendown()
    for i in range(2):
        t.penup()
        t.goto(-325/2,-90)
        t.forward(125*(i+1))
        t.pencolor(pen_color[i*2+1])
        t.pendown()
        t.circle(50)
        t.penup()
        t.pendown()
    for i in range(3): #membuat lingkaran interlock
        t.penup()
        t.pencolor(pen_color[i*2])
        t.home()
        t.goto(-100, -50)
        t.penup()
        t.forward(125*i)
        t.penup()
        t.circle(50, 45)
        t.pendown()
        t.circle(50, 180)
        t.penup()
        t.circle(50, 90)
        t.pendown()
        t.circle(50, 45)
        
#membuat fungsi untuk membuat garis olimpiade garis lurus
def olympic_line():
    t.speed(0)
    t.penup()
    t.home()
    t.goto(-100,-220)
    t.pendown()
    for i in range(5):
        t.pencolor(pen_color[i])
        t.circle(50)
        t.penup()
        t.forward(125/2)
        t.pendown()
    t.penup()
    t.goto(-100,-220)
    t.speed()
    for i in range(4): #membuat lingkaran interlock
        t.pencolor(pen_color[i])
        t.penup()
        t.home()
        t.goto(-100,-220)
        t.forward(125*(i)/2)
        t.circle(50, 90)
        t.pendown()
        t.circle(50, 90)
        t.penup()
        t.pendown()
def asking_box():
    for i in range(sum_rows):
        t.pensize(1)
        t.penup()
        t.home()
        t.goto(25-(sum_rows*square_size/2),-290)
        t.right(90)
        t.forward(square_size*i)
        t.left(90)
        t.pendown()
        for i in range(sum_rows): #menggambar kotak dan mengisinya dengan warna random
            if i > 0 : 
                t.forward(square_size)
            r_color = r.randint(0, 255)
            g_color = r.randint(0, 255)
            b_color = r.randint(0, 255)
            t.pencolor(r_color, g_color, b_color)
            t.fillcolor(r_color, g_color, b_color)
            t.begin_fill()
            for i in range(4):
                t.forward(square_size)
                t.right(90)
            t.end_fill()
def write_olympic(): #menuliskan kata kata dibawah kotak
    t.penup()
    t.right(90)
    t.forward(square_size)
    t.forward(30)
    t.right(90)
    t.forward(sum_rows*square_size/2-square_size)
    t.pendown()
    t.pencolor("blue")
    t.write(f"Olympic Logo and Colorful Chessboard of {sum_rows**2} squares", move=False, align="center", font=("arial",15,"normal"))

if __name__=="__main__": #progam utama
    t.screensize(2000,2000)
    sum_rows = int(t.numinput("Olympic Logo and Colorful Chessboard", "Enter the number of row:", minval=2, maxval=25,))
    square_size = int(t.numinput("Olympic Logo and Colorful Chessboard","Enter the squaresize(pixels):", minval=5, maxval=50))
    olympic_wave()
    olympic_line()
    asking_box()
    write_olympic()
    t.mainloop()

