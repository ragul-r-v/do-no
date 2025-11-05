import tkinter as tk 
INSIDE,LEFT,RIGHT,BOTTOM,TOP=0,1,2,3,4

def compute_code(x,y,x_min,y_min,x_max,y_max):
    code = INSIDE

    if x < x_min:code|= LEFT
    elif x > x_max: code|= RIGHT
    if y<y_min:code|= BOTTOM
    elif y>y_max:code|=TOP
    return code

def cohen_sutherland_clip (x1,y1,x2,y2,x_min,y_min,x_max,y_max):

    code1= compute_code (x1,y1,x_min,y_min,x_max,y_max)
    code2= compute_code (x2,y2,x_min,y_min,x_max,y_max)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif (code1&code2)!=0:
            break

        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min -y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:
                y = y1 + (y2 - y1 ) * (x_max-x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min-x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1,y1 = x,y
                code1 = compute_code ( x1,y1,x_min,y_min,x_max,y_max)

            else:
                x2,y2 = x,y
                code2 = compute_code (x2,y2,x_min,y_min,x_max,y_max)

    return accept,x1,y1,x2,y2

def draw_result ( x1,y1,x2,y2, clipped, x_min, y_min, x_max , y_max ):
    root = tk.Tk()
    root.title ( "Cohen - Sutherland Line Clipping ")
    canvas = tk.Canvas ( root,width = 600 , height = 600, bg= "white")

    canvas.pack()

    canvas.create_rectangle(x_min , y_min, x_max, y_max, outline = "blue" ,dash = (5,5),width = 2)
    canvas.create_text ( 300,20,text = "Cohen - Sutherland Line Clipping ", fill = "black" , font = ("Arial", 14, "bold"))

    canvas.create_line (orig_x1, orig_y1, orig_x2, orig_y2, fill = "red", width = 2 )
    canvas.create_text (orig_x1, orig_y1- 10, text = "Original Line " , fill = "red", font = ("Arial", 9))

    if clipped:

        canvas.create_line (x1, y1, x2, y2, fill = "green", width = 2)
        canvas.create_text (x1,y1 -10, text = "Clipped Line ", fill = "green", font = ("Arial", 9))

    else:
        canvas.create_text ( 300, 560, text = "Line Rejected (Outside Window )", fill = "red"  , font = ("Arial", 12, "bold"))

    root.mainloop()

print ( " Enter Line Coordinates : ")

orig_x1 = int (input ( "x1 : "))
orig_y1 = int (input ( "y1 : "))
orig_x2 = int (input ( "x2 : "))
orig_y2 = int (input ( "y2 : "))

print ("\n Enter Clipping Window :")

x_min = int (input ("x_min :"))
y_min = int (input ("y_min :"))
x_max = int (input ("x_max :"))
y_max = int (input ("y_max :"))

accept,cx1,cy1,cx2,cy2 =cohen_sutherland_clip(orig_x1,orig_y1, orig_x2,orig_y2 , x_min,y_min , x_max, y_max)

draw_result(cx1,cy1,cx2,cy2,accept,x_min,y_min, x_max, y_max)






