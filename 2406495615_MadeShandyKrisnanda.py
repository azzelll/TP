import turtle as t
import random as r

#Menyiapkan semua pengaturan dasar pada program ini
t.title("Olympic Logo and Colorful Chessboard") 
t.pensize(10)
t.speed(0)
t.screensize(500, 4500)
t.colormode(255)

#Memasukan warna sesuai dengan kode RGB ke dalam variable dan list
blue = 0,129,200
yellow = 252,177,49
black = 0,0,0
red = 0,166,81
green = 238,51,78
pen_color = [blue, yellow, black, red, green]

def make_circle(x, y, radius, degree, color): #Membuat lingkaran
    t.pencolor(color)
    t.penup()
    t.home()
    t.goto(x, y)
    t.pendown()
    t.circle(radius, degree)

def olympic_wave(): #Membuat logo olympic gelombang
    for i in range(5): 
        if i % 2 == 0 :
            make_circle(-130+i*65,120,50,360,pen_color[i])
        elif i % 2 == 1 :
            make_circle(-130+i*65,80,50,360,pen_color[i])
    for i in range(5):
        if i % 2 == 0 :
            make_circle(-130+i*65,120,50,-45,pen_color[i])
            make_circle(-130+i*65,120,50, 70,pen_color[i])
        elif i % 2 == 1 :
            make_circle(-130+i*65,80,50,-135,pen_color[i])
            make_circle(-130+i*65,80,50, 180,pen_color[i])

def olympic_line(): #Membuat logo olympic lurus
    for i in range(5):
        make_circle(-130+i*65,-50,50,360,pen_color[i])
    for i in range(5):
        make_circle(-130+i*65,-50,50,-90,pen_color[i])
        make_circle(-130+i*65,-50,50,180,pen_color[i])
        
def checkboard(): #Membuat papan catur dengan warna random sesuai input
    t.pensize(1)
    for i in range(sum_rows):
        t.penup()
        t.home()
        t.goto(0-(sum_rows*square_size/2),-150-(i*square_size))
        t.pendown()
        for i in range(sum_rows):
            r_color = r.randint(0, 255)
            g_color = r.randint(0, 255)
            b_color = r.randint(0, 255)
            t.pencolor(r_color, g_color, b_color)
            t.fillcolor(r_color, g_color, b_color)
            t.begin_fill()
            for i in range(5):
                t.forward(square_size)
                if i <4 :
                    t.right(90)
            t.end_fill()

def write_sum(): #Menuliskan jumlah kotak pada papan catur
    t.pensize(1)
    t.penup()
    t.home()
    t.goto(0,-180-(sum_rows*square_size))
    t.pendown()
    t.pencolor(blue)
    t.write(f"Olympic Logo and Colorful Chessboard of {sum_rows**2} squares", move=False, align="center", font=("arial",15,"normal"))
            
if __name__ == "__main__": #Program utama
    sum_rows = int(t.numinput("Olympic Logo and Colorful Chessboard", "Enter the number of row:", minval=2, maxval=25,))
    square_size = int(t.numinput("Olympic Logo and Colorful Chessboard","Enter the squaresize(pixels):", minval=5, maxval=50))
    olympic_wave()
    olympic_line()
    checkboard()
    write_sum()
    t.mainloop()