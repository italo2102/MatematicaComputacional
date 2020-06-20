import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

points = (
	(0,0,0),
	(3,0,0),
	(0,3,0),
	(0,0,3)
)


lines=(
	(0,1),
	(0,2),
	(0,3)
)

verticies = (
	(1,0,0),
	(1,1,0),
	(0,1,0),
	(0,0,0),
	(1,0,1),
	(1,1,1),
	(0,0,1),
	(0,1,1)
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(5,1),
	(5,4),
	(5,7),
	(6,3),
	(6,4),
	(6,7)
)

surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
)

colors = (
	(1,0,0),
	(0,1,0),
	(1,0,0),
	(0,0,0),
	(1,0,0),
	(1,0,0),
	(0,0,1),
	(0,1,1),
	(1,1,1),
	(0,1,0),
	(0,0,1),
	(0,0,0)
)

colors1 = (
	(1,0,1),
	(1,0,0),
	(0,1,0),
	(0,0,0),
	(1,0,0),
	(1,1,1),
	(0,0,1),
	(0,1,1),
	(1,0,0),
	(1,1,0),
	(0,1,0),
	(0,0,0)
)

def Cube():
	glBegin(GL_QUADS)
	
	for surface in surfaces:
		x=0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(verticies[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	for line in lines:
		for point in line:
			glVertex3fv(points[point])
	glEnd()
	
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verticies[vertex])
	glEnd()
	
def Cube2():
	verticies2= np.zeros((8, 3))
	
	P = [[0.91068360, -0.24401693 ,  0.33333333],
    [0.33333333 ,  0.91068360,  -0.24401693],
    [-0.24401693 ,  0.33333333 ,  0.91068360]]
    
	glBegin(GL_QUADS)
	for surface in surfaces:
		x=0
		for vertex in surface:
			x+=1
			glColor3fv(colors1[x])
			glVertex3fv(verticies[vertex])
	glEnd()
	
	glBegin(GL_LINES)
	i=0
	for vertex in verticies:
		nuevo= np.dot(P,vertex)
		verticies2[i] = nuevo
		i = 1 + i
	verticies2 = tuple(verticies2)
        
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verticies2[vertex])
	glEnd()
	
	
def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(60, (display[0]/display[1]),5.5, 2.0)
	glTranslatef(0.0,0.0,-5)
	glRotatef(0,0,0,0)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		#glRotatef(1,3,1,1)
		glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
		Cube()
		Cube2()
		pygame.display.flip()
		pygame.time.wait(10)
		
main()
	
