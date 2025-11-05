import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
 
cube = np.array([ 
    [0, 0, 0], 
    [0, 0, 1], 
    [0, 1, 0], 
    [0, 1, 1], 
    [1, 0, 0], 
    [1, 0, 1], 
    [1, 1, 0], 
    [1, 1, 1] 
]) 
 
edges = [ 
    (0,1), (0,2), (0,4), (1,3), (1,5), 
    (2,3), (2,6), (3,7), (4,5), (4,6), 
    (5,7), (6,7) 
] 
 
def plot_3d(original, transformed, title): 
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d') 
    ax.set_title(title)
    for edge in edges: 
        p1 = original[edge[0]] 
        p2 = original[edge[1]] 
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='blue') 
 
    for edge in edges: 
        p1 = transformed[edge[0]] 
        p2 = transformed[edge[1]] 
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='red') 
 
    plt.show() 
 
def translate(cube, tx, ty, tz): 
    matrix = np.array([ 
        [1, 0, 0, tx], 
        [0, 1, 0, ty], 
        [0, 0, 1, tz], 
        [0, 0, 0, 1] 
    ]) 
    points = np.hstack((cube, np.ones((cube.shape[0], 1)))) 
    return (matrix @ points.T).T[:, :3] 
 
def scale(cube, sx, sy, sz): 
    matrix = np.array([ 
        [sx, 0,  0,  0], 
        [0,  sy, 0,  0], 
        [0,  0,  sz, 0], 
        [0,  0,  0,  1] 
    ]) 
    points = np.hstack((cube, np.ones((cube.shape[0], 1)))) 
    return (matrix @ points.T).T[:, :3] 
 
def rotate_x(cube, angle_deg): 
    angle = np.radians(angle_deg) 
    matrix = np.array([ 
        [1, 0,           0,          0], 
        [0, np.cos(angle), -np.sin(angle), 0], 
        [0, np.sin(angle),  np.cos(angle), 0], 
        [0, 0, 0,  1] 
    ]) 
    points = np.hstack((cube, np.ones((cube.shape[0], 1)))) 
    return (matrix @ points.T).T[:, :3] 
 
def rotate_y(cube, angle_deg): 
    angle = np.radians(angle_deg) 
    matrix = np.array([ 
        [ np.cos(angle), 0, np.sin(angle), 0], 
        [ 0, 1, 0,  0],
         [-np.sin(angle), 0, np.cos(angle), 0], 
        [ 0, 0, 0, 1] 
    ]) 
    points = np.hstack((cube, np.ones((cube.shape[0], 1)))) 
    return (matrix @ points.T).T[:, :3] 
 
def rotate_z(cube, angle_deg): 
    angle = np.radians(angle_deg) 
    matrix = np.array([ 
        [np.cos(angle), -np.sin(angle), 0, 0], 
        [np.sin(angle),  np.cos(angle), 0, 0], 
        [0,  0,  1, 0], 
        [0,  0, 0, 1] 
    ]) 
    points = np.hstack((cube, np.ones((cube.shape[0], 1)))) 
    return (matrix @ points.T).T[:, :3] 
 
while True: 
    print("\n3D Transformation Menu:") 
    print("1. Translation") 
    print("2. Scaling") 
    print("3. Rotation about X-axis") 
    print("4. Rotation about Y-axis") 
    print("5. Rotation about Z-axis") 
    print("6. Exit") 
 
    choice = int(input("Enter your choice: ")) 
    if choice == 1: 
        tx = float(input("Translate X by: ")) 
        ty = float(input("Translate Y by: ")) 
        tz = float(input("Translate Z by: ")) 
        new_cube = translate(cube, tx, ty, tz) 
        plot_3d(cube, new_cube, "3D Translation") 
    elif choice == 2: 
        sx = float(input("Scale X by: ")) 
        sy = float(input("Scale Y by: ")) 
        sz = float(input("Scale Z by: ")) 
        new_cube = scale(cube, sx, sy, sz) 
        plot_3d(cube, new_cube, "3D Scaling") 
    elif choice == 3: 
        angle = float(input("Enter rotation angle (X-axis): ")) 
        new_cube = rotate_x(cube, angle) 
        plot_3d(cube, new_cube, "Rotation about X-axis") 
    elif choice == 4: 
        angle = float(input("Enter rotation angle (Y-axis): ")) 
        new_cube = rotate_y(cube, angle) 
        plot_3d(cube, new_cube, "Rotation about Y-axis") 
    elif choice == 5:
        angle = float(input("Enter rotation angle (Z-axis): ")) 
        new_cube = rotate_z(cube, angle) 
        plot_3d(cube, new_cube, "Rotation about Z-axis") 
    elif choice == 6: 
        break
            
    else: 
            print("Invalid choice. Try again.")