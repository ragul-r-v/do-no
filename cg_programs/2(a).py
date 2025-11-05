import tkinter as tk 
import math 
 
def draw_point(canvas, xc, yc, x, y, color): 
    for dx, dy in [(x, y), (-x, y), (x, -y), (-x, -y), 
                   (y, x), (-y, x), (y, -x), (-y, -x)]: 
        canvas.create_oval(xc+dx, yc+dy, xc+dx+1, yc+dy+1, fill=color, outline=color) 
 
def midpoint_circle(canvas, xc, yc, r, color): 
    x = 0 
    y = r 
    p = 1 - r 
    draw_point(canvas, xc, yc, x, y, color) 
 
    while x < y: 
        x += 1 
 
        if p < 0: 
            p += 2 * x + 1 
        else: 
            y -= 1 
            p += 2 * (x - y) + 1 
        draw_point(canvas, xc, yc, x, y, color) 
 
def draw_internal_pattern(canvas, xc, yc, r, pattern, color): 
    if pattern == 'radial': 
        for angle in range(0, 360, 15): 
            rad = math.radians(angle) 
            x = xc + int(r * math.cos(rad)) 
            y = yc + int(r * math.sin(rad)) 
            canvas.create_line(xc, yc, x, y, fill=color) 
 
    elif pattern == 'horizontal': 
        for dy in range(-r, r+1, 10): 
            y = yc + dy 
            span = int((r**2 - dy**2) ** 0.5) 
            canvas.create_line(xc - span, y, xc + span, y, fill=color) 
 
    elif pattern == 'vertical': 
        for dx in range(-r, r+1, 10): 
            x = xc + dx 
            span = int((r**2 - dx**2) ** 0.5) 
            canvas.create_line(x, yc - span, x, yc + span, fill=color) 
 
    elif pattern == 'cross': 
 
        draw_internal_pattern(canvas, xc, yc, r, 'horizontal', color) 
        draw_internal_pattern(canvas, xc, yc, r, 'vertical', color) 
 
def get_user_input(): 
    print("\n--- Midpoint Circle with Internal Patterns ---") 
    xc = int(input("Enter center X: ")) 
    yc = int(input("Enter center Y: ")) 
    r = int(input("Enter radius: ")) 
 
    print("\nColor Options: 1. Red  2. Green  3. Blue  4. Black  5. Magenta") 
    color_choice = input("Choose color (1-5): ") 
    color_map = {'1': 'red', '2': 'green', '3': 'blue', '4': 'black', '5': 'magenta'} 
    color = color_map.get(color_choice, 'black') 
 
    print("\nPattern Inside Circle: 1. None  2. Radial  3. Horizontal  4. Vertical  5. Cross") 
    pattern_choice = input("Choose internal pattern (1-5): ") 
    pattern_map = {'1': 'none', '2': 'radial', '3': 'horizontal', '4': 'vertical', '5': 'cross'} 
    pattern = pattern_map.get(pattern_choice, 'none') 
 
    return xc, yc, r, color, pattern 
 
def draw_circle_with_pattern(xc, yc, r, color, pattern): 
    root = tk.Tk() 
    root.title("Circle with Patterns Inside") 
    canvas = tk.Canvas(root, width=600, height=600, bg="white") 
    canvas.pack() 
 
    canvas.create_text(300, 20, text="Midpoint Circle with Patterns", font=("Helvetica", 16, "bold")) 
 
    canvas.create_text(300, 45, text=f"Center: ({xc},{yc}), Radius: {r}, Pattern: {pattern}", font=("Arial", 12), fill=color) 
 
 
    midpoint_circle(canvas, xc, yc, r, color) 
 
    if pattern != 'none': 
        draw_internal_pattern(canvas, xc, yc, r, pattern, color) 
 
    canvas.create_oval(xc - 3, yc - 3, xc + 3, yc + 3, fill=color) 
    canvas.create_text(xc + 25, yc, text=f"({xc},{yc})", font=("Arial", 10), fill=color) 
 
    root.mainloop() 
 
# Main loop 
while True: 
    user_input = get_user_input() 
    draw_circle_with_pattern(*user_input) 
    again = input("\nDraw another circle? (y/n): ") 
    if again.lower() != 'y': 
        break