import tkinter as tk 
import math 
 
root = tk.Tk() 
root.title(" ") 
canvas = tk.Canvas(root, width=600, height=600, bg="white") 
canvas.pack() 
 
x_offset = 300 
y_offset = 300 
 
canvas.create_text(300, 10, text="2D TRANSFORMATIONS", fill="black", font=("Arial", 14, "bold")) 
canvas.create_line(0, y_offset, 600, y_offset, fill="gray")  # X-axis 
canvas.create_line(x_offset, 0, x_offset, 600, fill="gray")  # Y-axis 
 
original_points = [[100, 100], [200, 100], [150, 200]] 
 
print("--- 2D Transformation Menu ---") 
print("1. Translation") 
print("2. Rotation") 
print("3. Scaling") 
print("4. Shearing") 
print("5. Reflection") 

 
choice = int(input("Enter your choice (1-5): ")) 
 
if choice == 1: 
    print("--- TRANSLATION ---") 
    tx = int(input("Enter translation in X (tx): ")) 
    ty = int(input("Enter translation in Y (ty): ")) 
elif choice == 2: 
    print("--- ROTATION ---") 
    angle = float(input("Enter angle (in degrees): ")) 
    theta = math.radians(angle) 
elif choice == 3: 
    print("--- SCALING ---") 
    sx = float(input("Enter scaling in X (sx): ")) 
    sy = float(input("Enter scaling in Y (sy): ")) 
elif choice == 4: 
    print("--- SHEARING ---") 
    shx = float(input("Enter shearing in X (shx): ")) 
    shy = float(input("Enter shearing in Y (shy): ")) 
elif choice == 5: 
    print("--- REFLECTION ---") 
    axis = input("Reflect about X or Y axis? (x/y): ").lower() 
 
transformed_points = [] 
for x, y in original_points: 
    if choice == 1:  # Translation 
        xt = x + tx 
        yt = y + ty 
    elif choice == 2:  # Rotation (about origin) 
        xt = round(x * math.cos(theta) - y * math.sin(theta)) 
        yt = round(x * math.sin(theta) + y * math.cos(theta)) 
    elif choice == 3:  # Scaling 
        xt = x * sx 
        yt = y * sy 
    elif choice == 4:  # Shearing 
        xt = x + y * shx 
        yt = y + x * shy 
    elif choice == 5:  # Reflection 
        if axis == 'x': 
            xt = x 
            yt = -y 
        elif axis == 'y': 
            xt = -x 
            yt = y 
        else: 
            xt, yt = x, y  # Invalid axis input fallback 
    transformed_points.append([xt, yt]) 
 
 
def to_canvas_coords(x, y): 
    return x + x_offset, y_offset - y 
 
for i in range(3): 
    x1, y1 = to_canvas_coords(*original_points[i]) 
    x2, y2 = to_canvas_coords(*original_points[(i+1)%3]) 
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2) 
    canvas.create_text(x1, y1 - 10, text=f"O{i+1}({original_points[i][0]},{original_points[i][1]})", fill="blue") 
 
for i in range(3): 
    x1, y1 = to_canvas_coords(*transformed_points[i]) 
    x2, y2 = to_canvas_coords(*transformed_points[(i+1)%3]) 
    canvas.create_line(x1, y1, x2, y2, fill="red", dash=(4, 2), width=2) 
    canvas.create_text(x1, y1 - 10, text=f"T{i+1}({transformed_points[i][0]},{transformed_points[i][1]})", fill="red") 
 
root.mainloop()