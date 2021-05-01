import math
import pygame
import numpy as np
import random


class Die:
    faces_num=[]
    
    def __init__(self, num_sides, faces_num, x, y, color, num_faces):
        self.num_sides=num_sides
        self.num_faces=num_faces
        self.radius = 45
        self.faces_num=[faces_num[i] for i in range(num_faces+1)]
        self.polygon=[]
        self.central_angle = (2*np.pi)/num_sides
        self.total_angle = np.pi*(num_sides-2)
        self.center = (x,y) 
        self.color=color
        self.cordenates()
        self.face=0

    def cordenates(self):
        self.polygon=[]
        for i in range(self.num_sides):
            self.polygon.append((self.center[0]+(self.radius*math.cos(self.central_angle*(i+1))),self.center[1]+(self.radius*math.sin(self.central_angle*(i+1)))))

    def update(self, screen, font):  
        pygame.draw.polygon(screen,self.color,self.polygon) 
        draw_number_text = font.render(str(self.faces_num[self.face]), 1,(0,0,0))
        if int(self.face)<10:
            screen.blit(draw_number_text, (self.center[0]-self.radius+35,self.center[1]-self.radius+25))
        else:
            screen.blit(draw_number_text, (self.center[0]-self.radius+22,self.center[1]-self.radius+25))    


    def roll(self):
        n = random.sample(range(1, self.num_faces+1), 1)[0]
        self.face=int(self.faces_num[n])
    
        return n