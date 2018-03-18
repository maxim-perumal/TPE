# coding: utf-8

import sys
import random
import math
import os
import pygame
from socket import *
from pygame.locals import *

SCREEN_X = 1600
SCREEN_Y = 900
DIFF_ANGLE = 3.14/4

"""Soit Rect la hitbox, et les sprite les elements de rendus."""

def load_img(name):
    """Charge une image et retourne un objet image compatible Pygame
        il est necessaire de stocker les images dans un dossier data"""
    path = os.path.join('data', name)
    image = pygame.image.load(path)
    if image.get_alpha is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    return image, image.get_rect()

class Obstacle(pygame.sprite.Sprite):
    """Un obstacle de graphisme obstacle.png,
    hérite de la class Sprite de Pygame.
    Return: sprite objet Obstacle (pour rendus)
    Method: update"""
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = (random.randint(0,SCREEN_X), random.randint(0,SCREEN_Y) , width, height)


class Car(pygame.sprite.Sprite):
    """Une voiture de graphisme car.png et de control car_ai,
    hérite de la class Sprite de Pygame.
    Return: sprite objet Car (pour rendus)
    Method: update_car, calc_newpos
    Atributes: area, vector"""

    def __init__(self, vector):
        """ Initialisation du Sprite et de Car"""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_img('car.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update_car(self, newPos):
        """Actualisation de l'objet Car dans la simulation"""
        self.rect = newPos
        print("    X: " + str(self.getX()) + "    Y: " + str(self.getY()) + "    Z: " + str(self.getZ()))

    def calc_newpos(self, rect, vector):
        """Calcul de la position en x,y d'après un vecteur de mouvement"""
        (angle,z) = vector
        (x,y) = (10*z*math.cos(angle),10*z*math.sin(angle))
        return rect.move((round(x),-round(y)))

    def obstacle_detected(self, newPos):
        if self.area.contains(newPos):
            if self.rect.colliderect(Obstacle_list[0].rect):
                return True
            else:
                return False
        else:
            return True

    def calc_vectorNorm(self, vector):
        (angle,z) = vector
        (x,y) = (z*math.cos(angle),z*math.sin(angle))
        norm = math.sqrt((x)**2 + (y)**2)
        return norm

    def getX(self):
        (angle,z) = self.vector

        Yvector = (angle - DIFF_ANGLE,z)
        vectorIsMax = False

        while (vectorIsMax == False):

            if (self.obstacle_detected(self.calc_newpos(self.rect, Yvector))):
                vectorIsMax = True

            (angle,z) = Yvector
            Yvector = (angle,z + 1)

        return self.calc_vectorNorm(Yvector)

    def getY(self):
        (angle,z) = self.vector

        Yvector = (angle,z)
        vectorIsMax = False

        while (vectorIsMax == False):

            if (self.obstacle_detected(self.calc_newpos(self.rect, Yvector))):
                vectorIsMax = True

            (angle,z) = Yvector
            Yvector = (angle,z + 1)

        return self.calc_vectorNorm(Yvector)

    def getZ(self):
        (angle,z) = self.vector

        Yvector = (angle  + DIFF_ANGLE,z)
        vectorIsMax = False

        while (vectorIsMax == False):

            if (self.obstacle_detected(self.calc_newpos(self.rect, Yvector))):
                vectorIsMax = True

            (angle,z) = Yvector
            Yvector = (angle,z + 1)

        return self.calc_vectorNorm(Yvector)

    def turn_180(self):
        (angle,z) = self.vector
        angle = 3.14 + angle
        self.vector = (angle,z)

    def turn_deg(self, Xdeg):
        (angle,z) = self.vector
        Xrad = Xdeg * 3.14/180
        angle = Xrad + angle
        self.vector = (angle,z)

    def change_speed(self, delta):
        (angle,z) = self.vector
        self.vector = (angle,z + delta)

    def set_speed(self, speed):
        (angle,z) = self.vector
        self.vector = (angle,speed)

class Car_ai(Car):
    """Class de controle de la voiture, contient la logique de ces mouvements,
    hérite de la class Car.
    Return: sprite objet Car (pour rendus)
    Method: update
    Atributes: area, vector"""

    def __init__(self):
        """Initialisation de Car et du Sprite"""
        speed = 1
        self.hit = 0
        self.vector = (-1,speed)
        Car.__init__(self, self.vector)

    def update(self):
        """Actualiste la position de la voiture, appelé a chaque Frame"""
        newPos = self.calc_newpos(self.rect,self.vector)
        if (self.getY() < 10):
            self.set_speed(0)
        self.update_car(newPos)

def main():
    """Boucle principal de la simulation"""

    #Initialisation de la fenetre Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Car simulateur')

    # Remplissage de l'arrière-plan
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    #Initialisation de la voiture et de l'IA
    car = Car_ai()
    global Obstacle_list
    Obstacle_list = [Obstacle((0,0,0),20,100)]

    #Initialisation des Sprites
    carsprite = pygame.sprite.RenderPlain(car)
    mursprite = pygame.sprite.RenderPlain(Obstacle_list[0])

    # Blitter pour rendus dans la fenêtre (création des rendus 2D dans fenetre)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialisation de l'horloge pour regulation fps
    clock = pygame.time.Clock()

    #Infinite loop de la simulation
    while 1:

        # Ecoute d'evenements coté user (ex: fermer la fenetre)
        for event in pygame.event.get():
	           if event.type == QUIT:
		                 return

        # Rendus des sprites
        screen.blit(background, car.rect, car.rect)
        carsprite.update()
        screen.blit(background, Obstacle_list[0].rect, Obstacle_list[0].rect)
        carsprite.draw(screen)
        mursprite.draw(screen)
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__': main()
