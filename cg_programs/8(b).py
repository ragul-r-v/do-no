import tkinter as tk 
root = tk.Tk() 
root.title("2D Animation - Car Movement") 
width = 800 
height = 200 
canvas = tk.Canvas(root, width=width, height=height, bg="skyblue") 
canvas.pack() 
canvas.create_rectangle(0, 150, width, height, fill="gray") 
car_body = canvas.create_rectangle(50, 110, 150, 140, fill="red", outline="black") 
car_top = canvas.create_rectangle(70, 90, 130, 110, fill="orange", outline="black") 
wheel1 = canvas.create_oval(60, 135, 80, 155, fill="black") 
wheel2 = canvas.create_oval(120, 135, 140, 155, fill="black") 
car_parts = [car_body, car_top, wheel1, wheel2] 
def move_car(): 
    for part in car_parts: 
        canvas.move(part, 5, 0)  # Move right by 5 pixels
    if canvas.coords(car_body)[2] < width: 
        root.after(20, move_car) 
 
move_car() 
root.mainloop()