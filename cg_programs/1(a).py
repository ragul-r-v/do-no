import tkinter as tk 
 
print("--- LINE TYPE MENU ---") 
print("1. Horizontal Line") 
print("2. Vertical Line") 
print("3. Forward Slanting (/)") 
print("4. Backward Slanting (\\)") 
choice = input("Enter your line type choice (1-4): ") 
 
print("\nEnter starting point:") 
x1 = int(input("x1: ")) 
y1 = int(input("y1: ")) 
length = int(input("Enter length of line: "))


if choice == '1': 
    x2 = x1 + length 
    y2 = y1 
    label = "Horizontal Line" 
elif choice == '2': 
    x2 = x1 
    y2 = y1 + length 
    label = "Vertical Line" 
elif choice == '3': 
    x2 = x1 + length 
    y2 = y1 - length
    label = "Forward Slanting (/)" 
elif choice == '4': 
    x2 = x1 + length 
    y2 = y1 + length 
    label = "Backward Slanting (\\)" 
else: 
    print("Invalid choice") 
    exit() 
print("\nColor Options: 1. Red  2. Green  3. Blue  4. Black  5. Magenta") 
color_choice = input("Choose color (1-5): ") 
color_map = {'1': 'red', '2': 'green', '3': 'blue', '4': 'black', '5': 'magenta'} 
color = color_map.get(color_choice, 'black')

print("\nPattern Options: 1. Solid  2. Dashed  3. Dotted") 
pattern_choice = input("Choose pattern (1-3): ") 
pattern_map = {'1': 'solid', '2': 'dashed', '3': 'dotted'} 
pattern = pattern_map.get(pattern_choice, 'solid') 

root = tk.Tk() 
root.title("DDA Line Drawing - No Functions") 
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack() 

canvas.create_text(300, 20, text=label, fill=color, font=("Helvetica", 16, "bold")) 

dx = x2 - x1 
dy = y2 - y1 
steps = abs(dx) if abs(dx) > abs(dy) else abs(dy) 
x_inc = dx / steps 
y_inc = dy / steps 
x = x1 
y = y1 
i = 0 
while i <= steps: 
    xi = round(x) 
    yi = round(y)
    if pattern == 'solid': 
        canvas.create_rectangle(xi, yi, xi+1, yi+1, outline=color) 
    elif pattern == 'dashed': 
        if i % 15 < 10: 
            canvas.create_rectangle(xi, yi, xi+1, yi+1, outline=color) 
    elif pattern == 'dotted': 
        if i % 6 == 0: 
            canvas.create_rectangle(xi, yi, xi+1, yi+1, outline=color) 
 
    x += x_inc 
    y += y_inc 
    i += 1 
 
canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill=color) 
canvas.create_oval(x2 - 3, y2 - 3, x2 + 3, y2 + 3, fill=color) 
 
canvas.create_text(x1 - 20, y1 - 10, text=f"({x1},{y1})", fill=color, font=("Arial", 10)) 
canvas.create_text(x2 + 20, y2 + 10, text=f"({x2},{y2})", fill=color, font=("Arial", 10)) 
root.mainloop() 