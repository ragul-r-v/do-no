import tkinter as tk 
  
clip_window = {'xmin': 150, 'ymin': 150, 'xmax': 400, 'ymax': 400} 
 
def inside(p, edge): 
    x, y = p 
    if edge == 'LEFT': 
        return x >= clip_window['xmin'] 
    elif edge == 'RIGHT': 
        return x <= clip_window['xmax'] 
    elif edge == 'BOTTOM': 
        return y >= clip_window['ymin'] 
    elif edge == 'TOP': 
        return y <= clip_window['ymax'] 
 
def intersect(p1, p2, edge): 
    x1, y1 = p1 
    x2, y2 = p2 
 
    if edge == 'LEFT': 
        x = clip_window['xmin'] 
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1) 
    elif edge == 'RIGHT': 
        x = clip_window['xmax'] 
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1) 
    elif edge == 'BOTTOM': 
        y = clip_window['ymin'] 
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1) 
    elif edge == 'TOP': 
        y = clip_window['ymax'] 
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1) 
    return (x, y) 
 
def suth_hodg_clip(polygon, edges=['LEFT', 'RIGHT', 'BOTTOM', 'TOP']): 
    output_list = polygon 
    for edge in edges: 
        input_list = output_list 
        output_list = [] 
        if not input_list: 
            break 
        s = input_list[-1] 
 
        for e in input_list: 
            if inside(e, edge): 
                if inside(s, edge): 
                    output_list.append(e) 
                else: 
                    output_list.append(intersect(s, e, edge)) 
                    output_list.append(e) 
            elif inside(s, edge): 
                output_list.append(intersect(s, e, edge)) 
            s = e 
    return output_list 
 
def draw_polygon(canvas, points, outline_color, fill_color="", width=2): 
    if len(points) >= 2: 
        canvas.create_polygon(points, outline=outline_color, fill=fill_color, width=width) 
 
def draw_clipping_window(canvas): 
    canvas.create_rectangle( 
        clip_window['xmin'], clip_window['ymin'], 
        clip_window['xmax'], clip_window['ymax'], 
        outline='black', dash=(4, 2) 
    ) 
    canvas.create_text(275, 140, text="Clipping Window", fill="black", font=('Arial', 10)) 
    
def main(): 
     
    polygon_points = [(100, 100), (450, 100), (450, 450), (100, 450)] 
 
    root = tk.Tk() 
    root.title("Sutherland-Hodgman Polygon Clipping") 
 
    canvas = tk.Canvas(root, width=600, height=600, bg='white') 
    canvas.pack() 
    draw_clipping_window(canvas) 
    draw_polygon(canvas, polygon_points, outline_color="blue", fill_color="", width=2) 
    canvas.create_text(300, 20, text="Original Polygon (Blue)", fill="blue", font=('Arial', 12)) 
 
    clipped_polygon = suth_hodg_clip(polygon_points) 
 
    if clipped_polygon: 
        draw_polygon(canvas, clipped_polygon, outline_color="green", fill_color="", width=2) 
        canvas.create_text(300, 40, text="Clipped Polygon (Green)", fill="green", font=('Arial', 12)) 
 
    root.mainloop() 
 
main()
