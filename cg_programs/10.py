from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
 
angle = 0 
 
def init(): 
    glClearColor(0.5, 0.7, 1.0, 1.0)   
    glEnable(GL_DEPTH_TEST)       
 
def draw_cube_with_outline(): 
     
    glColor3f(1.0, 0.5, 0.0)          
    glutSolidCube(1.0) 
 
    glColor3f(0.0, 0.0, 0.0)        
    glLineWidth(2) 
    glutWireCube(1.01)               
 
def draw_ground(): 
    glColor3f(0.3, 0.9, 0.3)          
    glBegin(GL_QUADS) 
    glVertex3f(-5, -1, -5) 
    glVertex3f(-5, -1, 5)
    glVertex3f(5, -1, 5) 
    glVertex3f(5, -1, -5) 
    glEnd() 
 
def display(): 
    global angle 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
 
    gluLookAt(3, 3, 5, 0, 0, 0, 0, 1, 0)   
 
    draw_ground() 
 
    glPushMatrix() 
    glRotatef(angle, 1, 1, 0) 
    draw_cube_with_outline() 
    glPopMatrix() 
 
    glutSwapBuffers() 
 
def update(value): 
    global angle 
    angle += 1 
    if angle > 360: 
        angle -= 360 
    glutPostRedisplay() 
    glutTimerFunc(16, update, 0) 
 
def reshape(w, h): 
    glViewport(0, 0, w, h) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluPerspective(45, w / h, 1, 50) 
    glMatrixMode(GL_MODELVIEW) 
 
def main(): 
    glutInit() 
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) 
    glutInitWindowSize(600, 600) 
    glutCreateWindow(b"3D Scene - Cube and Ground using OpenGL") 

    init() 
    glutDisplayFunc(display) 
    glutReshapeFunc(reshape) 
    glutTimerFunc(0, update, 0) 
    glutMainLoop()

main()