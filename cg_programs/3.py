import tkinter as tk 
import math 
 
def draw_ellipse_points(canvas, xc, yc, x, y, color): 
    points = [(x, y), (-x, y), (x, -y), (-x, -y)] 
    for dx, dy in points: 
        canvas.create_oval(xc + dx, yc + dy, xc + dx + 1, yc + dy + 1, fill=color, outline=color) 
 
def bresenham_ellipse(canvas, xc, yc, rx, ry, color): 
    x = 0 
    y = ry 
 
    rx2 = rx * rx 
    ry2 = ry * ry 
    two_rx2 = 2 * rx2 
    two_ry2 = 2 * ry2 
 
    px = 0 
    py = two_rx2 * y 
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2) 
 
    while px < py: 
        draw_ellipse_points(canvas, xc, yc, x, y, color) 
        x += 1 
        px += two_ry2 
        if p1 < 0: 
            p1 += ry2 + px 
        else: 
            y -= 1 
            py -= two_rx2 
            p1 += ry2 + px - py 
 
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2 
 
    while y >= 0: 
        draw_ellipse_points(canvas, xc, yc, x, y, color) 
        y -= 1 
        py -= two_rx2 
        if p2 > 0: 
            p2 += rx2 - py 
        else: 
            x += 1 
            px += two_ry2 
            p2 += rx2 - py + px 
 
def draw_internal_pattern(canvas, xc, yc, rx, ry, pattern, color): 
    if pattern == 'radial': 
        for angle in range(0, 360, 15): 
            rad = math.radians(angle) 
            x = xc + int(rx * math.cos(rad)) 
            y = yc + int(ry * math.sin(rad)) 
            canvas.create_line(xc, yc, x, y, fill=color) 
    elif pattern == 'horizontal': 
        for dy in range(-ry, ry + 1, 10): 
            y = yc + dy 
            span = int(rx * ((1 - (dy / ry) ** 2) ** 0.5)) 
            canvas.create_line(xc - span, y, xc + span, y, fill=color) 
    elif pattern == 'vertical': 
        for dx in range(-rx, rx + 1, 10): 
            x = xc + dx 
            span = int(ry * ((1 - (dx / rx) ** 2) ** 0.5)) 
            canvas.create_line(x, yc - span, x, yc + span, fill=color) 
    elif pattern == 'cross': 
        draw_internal_pattern(canvas, xc, yc, rx, ry, 'horizontal', color) 
        draw_internal_pattern(canvas, xc, yc, rx, ry, 'vertical', color) 
 
 
def get_user_input(): 
    xc = int(input("Enter center X: ")) 
    yc = int(input("Enter center Y: ")) 
    rx = int(input("Enter X radius (horizontal): ")) 
    ry = int(input("Enter Y radius (vertical): ")) 
 
    print("Color Options: 1. Red  2. Green  3. Blue  4. Black  5. Magenta") 
    color_choice = input("Choose color (1-5): ") 
    color_map = {'1': 'red', '2': 'green', '3': 'blue', '4': 'black', '5': 'magenta'} 
    color = color_map.get(color_choice, 'black') 
 
    print("Pattern Inside Ellipse: 1. None  2. Radial  3. Horizontal  4. Vertical  5. Cross") 
    pattern_choice = input("Choose internal pattern (1-5): ") 
    pattern_map = {'1': 'none', '2': 'radial', '3': 'horizontal', '4': 'vertical', '5': 'cross'} 
    pattern = pattern_map.get(pattern_choice, 'none') 
 
    return xc, yc, rx, ry, color, pattern 
 
def draw_bresenham_ellipse_with_pattern(xc, yc, rx, ry, color, pattern): 
    root = tk.Tk() 
    root.title("Bresenham Ellipse with Patterns") 
    canvas = tk.Canvas(root, width=700, height=700, bg="white") 
    canvas.pack() 
 
    bresenham_ellipse(canvas, xc, yc, rx, ry, color) 
 
    if pattern != 'none': 
        draw_internal_pattern(canvas, xc, yc, rx, ry, pattern, color) 
 
    canvas.create_oval(xc - 3, yc - 3, xc + 3, yc + 3, fill=color) 
    canvas.create_text(xc + 25, yc, text=f"({xc},{yc})", font=("Arial", 10), fill=color) 
 
    root.mainloop() 
 
while True: 
    details = get_user_input() 
    draw_bresenham_ellipse_with_pattern(*details) 
    again = input("Draw another ellipse? (y/n): ") 
    if again.lower() != 'y': 
        break 