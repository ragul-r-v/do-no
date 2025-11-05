import tkinter as tk 
 
def liang_barsky(x1, y1, x2, y2, x_min, y_min, x_max, y_max): 
    dx = x2 - x1 
    dy = y2 - y1 
    p = [-dx, dx, -dy, dy] 
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1] 
 
    u1 = 0.0 
    u2 = 1.0 
 
    for i in range(4): 
        if p[i] == 0: 
            if q[i] < 0: 
                return False, x1, y1, x2, y2 
        else: 
            u = q[i] / p[i] 
            if p[i] < 0: 
                if u > u1: 
                    u1 = u 
            else: 
                if u < u2: 
                    u2 = u 
 
    if u1 > u2: 
        return False, x1, y1, x2, y2 
 
    x1_clip = x1 + u1 * dx 
    y1_clip = y1 + u1 * dy 
    x2_clip = x1 + u2 * dx 
    y2_clip = y1 + u2 * dy 
 
    return True, x1_clip, y1_clip, x2_clip, y2_clip 
 
def draw_result(x1, y1, x2, y2, clipped, x_min, y_min, x_max, y_max): 
    root = tk.Tk() 
    root.title("Liang–Barsky Line Clipping Algorithm") 
    canvas = tk.Canvas(root, width=600, height=600, bg="white") 
    canvas.pack() 
 
    canvas.create_rectangle(x_min, y_min, x_max, y_max, outline="blue", dash=(5, 5), width=2) 
    canvas.create_text(300, 20, text="Liang–Barsky Line Clipping", fill="black", font=("Arial", 14, "bold")) 
 
    canvas.create_line(orig_x1, orig_y1, orig_x2, orig_y2, fill="red", width=2) 
    canvas.create_text(orig_x1, orig_y1 - 10, text="Original", fill="red", font=("Arial", 9)) 
 
    if clipped: 
         
        canvas.create_line(x1, y1, x2, y2, fill="green", width=2) 
        canvas.create_text(x1, y1 - 10, text="Clipped", fill="green", font=("Arial", 9)) 
    else: 
        canvas.create_text(300, 560, text="Line Rejected (Outside)", fill="red", font=("Arial", 12, "bold")) 
 
    root.mainloop() 
 
print("Enter Line Coordinates:") 
orig_x1 = int(input("x1: ")) 
orig_y1 = int(input("y1: ")) 
orig_x2 = int(input("x2: ")) 
orig_y2 = int(input("y2: ")) 
 
print("\nEnter Clipping Window:") 
x_min = int(input("x_min: ")) 
y_min = int(input("y_min: ")) 
x_max = int(input("x_max: ")) 
y_max = int(input("y_max: ")) 
 
accept, cx1, cy1, cx2, cy2 = liang_barsky(orig_x1, orig_y1, orig_x2, orig_y2, x_min, y_min, x_max, 
y_max) 
 
draw_result(cx1, cy1, cx2, cy2, accept, x_min, y_min, x_max, y_max)
