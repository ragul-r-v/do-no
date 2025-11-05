import tkinter as tk 
width = 400 
height = 200 
ball_radius = 50 
x = 50 
y = 50 
dx = 3 
dy = 7
root = tk.Tk() 
root.title("Bouncing Ball") 
 
canvas = tk.Canvas(root, width=width, height=height, bg="black") 
canvas.pack() 
 
ball = canvas.create_oval(x - ball_radius, y - ball_radius,  
                          x + ball_radius, y + ball_radius,
                             fill="red") 
 
def move_ball(): 
    global x, y, dx, dy 
    x += dx 
    y += dy 
    if x - ball_radius <= 0 or x + ball_radius >= width: 
        dx = -dx 
    if y - ball_radius <= 0 or y + ball_radius >= height: 
        dy = -dy 
    canvas.coords(ball, x - ball_radius, y - ball_radius, x + ball_radius, y + ball_radius) 
    root.after(20, move_ball) 
 
move_ball() 
root.mainloop()