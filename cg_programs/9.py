import tkinter as tk 
 
def draw_face(expression): 
    canvas.delete("all") 
 
    canvas.create_oval(100, 50, 300, 250, fill="peachpuff", outline="black") 
 
    canvas.create_oval(150, 100, 170, 120, fill="white") 
    canvas.create_oval(230, 100, 250, 120, fill="white") 
    canvas.create_oval(158, 108, 162, 112, fill="black")  # Pupils 
    canvas.create_oval(238, 108, 242, 112, fill="black") 
 
    if expression == "sad": 
        canvas.create_line(145, 90, 170, 85, width=2) 
        canvas.create_line(230, 85, 255, 90, width=2) 
    elif expression == "surprise": 
        canvas.create_oval(140, 80, 175, 90, outline="black") 
        canvas.create_oval(225, 80, 260, 90, outline="black") 
    else:  
        canvas.create_line(145, 85, 170, 90, width=2) 
        canvas.create_line(230, 90, 255, 85, width=2) 
 
    if expression == "smile": 
        canvas.create_arc(150, 150, 250, 210, start=0, extent=-180, style="arc", width=2) 
    elif expression == "sad": 
        canvas.create_arc(150, 170, 250, 230, start=0, extent=180, style="arc", width=2) 
    elif expression == "surprise": 
        canvas.create_oval(190, 170, 210, 200, outline="black", width=2) 

    canvas.create_text(200, 20, text=f"Expression: {expression.capitalize()}", font=("Arial", 16, "bold")) 
 
root = tk.Tk() 
root.title("3D Animation - Human Facial Expressions") 
canvas = tk.Canvas(root, width=400, height=300, bg="lightblue") 
canvas.pack() 
 
frame = tk.Frame(root) 
frame.pack() 
 
tk.Button(frame, text="Smile", command=lambda: draw_face("smile")).pack(side=tk.LEFT, padx=10) 
tk.Button(frame, text="Sad", command=lambda: draw_face("sad")).pack(side=tk.LEFT, padx=10) 
tk.Button(frame, text="Surprise", command=lambda: draw_face("surprise")).pack(side=tk.LEFT, 
padx=10) 
 
draw_face("smile") 
 
root.mainloop()