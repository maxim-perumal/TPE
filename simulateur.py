import random

# modulaire nÃ©cessaire pour crÃ©er une simulation
import pygame

# Initialise le module py game
pygame.init()

# crÃ©e une fenÃªtre aux dimensions indiquÃ©es
screen = pygame.display.set_mode((1280, 720))

# cette classe permet de gÃ©rer le nombre d'image par seconde (classe = nouveau type)
clock = pygame.time.Clock()


class simulation():
    scale_x = 0
    scale_y = 0

    car_x = 0
    car_y = 0
    car_r = 0

    co1 = 0
    co2 = 0
    co3 = 0

    fonctionne = True

    def __init__(self):
        print("Simulaton defined")
        self.co1 = random.randint(0,255)
        self.co2 = random.randint(0,255)
        self.co3 = random.randint(0,255)

    def refresh(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fonctionne = False
                #
        pygame.display.flip()

        # bloque l'execution jusqu'Ã  ce que 1/60 seconde se soit Ã©coulÃ©
        clock.tick(60)

    def set_car_pos(self, x , y , r):
        self.car_x = x
        self.car_y = y
        self.car_r = r

    def draw_car(self):
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (self.co1, self.co2, self.co3), pygame.Rect(self.car_x, self.car_y, self.scale_x, self.scale_y))


    def create_car(self, x , y ,r):

        self.car_x = x
        self.car_y = y
        self.car_r = r

        self.scale_x = 50
        self.scale_y = 50
        self.draw_car()
        self.set_car_pos(self.car_x , self.car_y , self.car_r)

simulation = simulation()

x = 500
y = 210
r = 0

simulation.create_car(x, y, r)

while 1:
    x -= 1
    y = x
    simulation.set_car_pos(x,y,0)
    simulation.draw_car()
    simulation.refresh()


"""simulation.create_wall()

simulation.start()"""
