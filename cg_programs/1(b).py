import tkinter as tk 
 
print("--- LINE TYPE MENU ---") 
print("1. Horizontal Line") 
print("2. Vertical Line") 
print("3. Forward Slanting (/)") 
print("4. Backward Slanting (\\)") 
choice = input("Enter your line type choice (1-4): ") 
 
print("\nEnter Starting Point:") 
x0 = int(input("x0: ")) 
y0 = int(input("y0: ")) 
length = int(input("Enter length of line: ")) 
 
print("\nColor Options: 1. Red  2. Green  3. Blue  4. Black  5. Magenta") 
color_choice = input("Choose color (1-5): ") 
color_map = {'1': 'red', '2': 'green', '3': 'blue', '4': 'black', '5': 'magenta'} 
color = color_map.get(color_choice, 'black')

print("\nPattern Options: 1. Solid  2. Dashed  3. Dotted") 
pattern_choice = input("Choose pattern (1-3): ") 
pattern_map = {'1': 'solid', '2': 'dashed', '3': 'dotted'} 
pattern = pattern_map.get(pattern_choice, 'solid') 
 
if choice == '1': 
    x1 = x0 + length 
    y1 = y0 
    label = "Horizontal Line" 
elif choice == '2': 
    x1 = x0 
    y1 = y0 + length 
    label = "Vertical Line" 
elif choice == '3': 
    x1 = x0 + length 
    y1 = y0 - length 
    label = "Forward Slanting (/)" 
elif choice == '4': 
    x1 = x0 + length 
    y1 = y0 + length 
    label = "Backward Slanting (\\)" 
else: 
    print("Invalid line type choice!") 
    exit()
 
root = tk.Tk() 
root.title("Bresenham Line Drawing - With Color & Pattern") 
canvas = tk.Canvas(root, width=800, height=800, bg="white") 
canvas.pack() 
 
canvas.create_text(400, 20, text=label, fill=color, font=("Helvetica", 16, "bold"))

dx = abs(x1 - x0) 
dy = abs(y1 - y0) 
sx = 1 if x0 < x1 else -1 
sy = 1 if y0 < y1 else -1 
err = dx - dy 
 
x = x0 
y = y0 
step_count = 0 
 
while True: 
    # Apply pattern 
    if pattern == 'solid': 
        canvas.create_rectangle(x, y, x + 1, y + 1, outline=color) 
    elif pattern == 'dashed': 
        if step_count % 15 < 10: 
            canvas.create_rectangle(x, y, x + 1, y + 1, outline=color) 
    elif pattern == 'dotted': 
        if step_count % 6 == 0: 
            canvas.create_rectangle(x, y, x + 1, y + 1, outline=color) 
 
    if x == x1 and y == y1: 
        break 
 
    e2 = 2 * err 
    if e2 > -dy: 
        err -= dy 
        x += sx 
    if e2 < dx: 
        err += dx 
        y += sy


        step_count += 1 
 
canvas.create_oval(x0 - 3, y0 - 3, x0 + 3, y0 + 3, fill=color) 
canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill=color) 
 
canvas.create_text(x0 - 20, y0 - 10, text=f"({x0},{y0})", fill=color, font=("Arial", 10)) 
canvas.create_text(x1 + 30, y1 + 10, text=f"({x1},{y1})", fill=color, font=("Arial", 10)) 
root.mainloop() 


