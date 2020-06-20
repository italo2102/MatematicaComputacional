import pygame
from pygame.locals import *

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Cube2():
    glBegin(GL_LINES)

    n_verticies = np.ones((4,2))

    verticies = (
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 0),
        (0, 0, 0),
        (1, 0, 1),
        (1, 1, 1),
        (0, 0, 1),
        (0, 1, 1)
        )

    verticies = list(verticies)

    P = [[0.91068360, -0.24401693 ,  0.33333333],
    [0.33333333 ,  0.91068360,  -0.24401693],
    [-0.24401693 ,  0.33333333 ,  0.91068360]]

    matriz_v = np.zeros((8, 3))
    i = 0

    for v in verticies:
        nuevo = np.dot(P,v)
        matriz_v[i] = nuevo
        i = 1 + i

    matriz_v = tuple(matriz_v)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(matriz_v[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Sirve para mover el cubo 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-0.5,0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        Cube2()
        pygame.display.flip()
        pygame.time.wait(10)


main()

