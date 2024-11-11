import turtle as t
import random as r

#all settings and numbers used in the program
t.title("Olympic Logo and Colorful Chessboard") 
t.pensize(10)
t.speed(3)
t.screensize(500, 4500)
t.colormode(255)
start_x = -130
move_x = 65
quarter_circle,half_circle, full_circle = 90, 180, 360
onesixth_circle, oneeighth_part = 60, 45
y_top_wave, y_bottom_wave = 120, 80
y_line = -50
range_box_circle = 50

#Inputting colors according to the RGB code into variables and lists
blue = (0,129,200)
yellow = (252,177,49)
black = (0,0,0)
red = (0,166,81)
green = (238,51,78)
pen_color = [blue, yellow, black, red, green]

def make_circle(x, y, degree, color): #Make circles
    t.pencolor(color)
    t.penup()
    t.home()
    t.goto(x, y)
    t.pendown()
    t.circle(50, degree)

def olympic_wave(): #Create an Olympic Wave logo
    for i in range(5): 
        x = start_x+i*move_x
        if i % 2 == 0 :
            make_circle(x,y_top_wave,full_circle,pen_color[i])
        elif i % 2 == 1 :
            make_circle(x,y_bottom_wave,full_circle,pen_color[i])
    for i in range(5):
        x = start_x+i*move_x
        if i % 2 == 0 :
            make_circle(x,y_top_wave, oneeighth_part,pen_color[i])
            #make_circle(x,y_top_wave, -oneeighth_part,pen_color[i])
        elif i % 2 == 1 :
            make_circle(x,y_bottom_wave, quarter_circle,pen_color[i])
            #make_circle(x,y_bottom_wave, ,pen_color[i])

def olympic_line(): #Make a straight Olympic logo
    for i in range(5):
        x = start_x+i*move_x
        make_circle(x,y_line, full_circle,pen_color[i])
    for i in range(5):
        x = start_x+i*move_x
        make_circle(x,y_line,-quarter_circle,pen_color[i])
        make_circle(x,y_line, half_circle,pen_color[i])
        
def checkboard(): #Create chess board with random colors according to input
    t.pensize(1)
    for i in range(sum_rows):
        t.penup()
        t.home()
        t.goto(0-(sum_rows*square_size/2),(y_line-range_box_circle)-(i*square_size))
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

def write_sum(): #Write the number of squares on the chess board
    t.pensize(1)
    t.penup()
    t.home()
    t.goto(0,-180-(sum_rows*square_size))
    t.pendown()
    t.pencolor(blue)
    t.write(f"Olympic Logo and Colorful Chessboard of {sum_rows**2} squares", move=False, align="center", font=("arial",15,"normal"))
            
if __name__ == "__main__": #Main program
    sum_rows = int(t.numinput("Olympic Logo and Colorful Chessboard", "Enter the number of row:", minval=2, maxval=25,))
    square_size = int(t.numinput("Olympic Logo and Colorful Chessboard","Enter the squaresize(pixels):", minval=5, maxval=50))
    while square_size % 2 != 0 :
        square_size = int(t.numinput("Olympic Logo and Colorful Chessboard","Enter the squaresize(pixels):", minval=5, maxval=50))
    olympic_wave()
    olympic_line()
    checkboard()
    write_sum()
    t.mainloop()