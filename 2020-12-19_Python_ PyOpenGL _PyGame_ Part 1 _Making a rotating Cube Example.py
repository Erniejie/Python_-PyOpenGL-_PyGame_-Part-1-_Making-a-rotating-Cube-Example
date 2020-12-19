#SENTDEX-OpenGL with PyOpenGL tutorial Python and PyGame p.1
#--- Making a rotating Cube Example-Nov 3rd 2014
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
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


def main():
    pygame.init()
    display =(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

    gluPerspective(45,(display[0]/display[1]) ,0.1, 50)

    glTranslate(0,0,-5)

    """ EXPLANATION:glRotate(degree,move in x,?,?)"""
    glRotate(0,0,0,0)   #  this "rotation function" makes the ANIMATION IN 3D

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        #glRotate(1,3,2,1)
        #glRotate(1,1,-1,1)
        glRotate(1,1,1,1)
                

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
        





                



        


    

    
