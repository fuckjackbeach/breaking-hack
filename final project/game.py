import pygame
import sys

WIDTH = 400
HEIGHT = 300
BACKGROUND = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player(Sprite):
   
    def __init__(self, startx, starty):
        super().__init__("data/sprite/mrparkyo.png", startx, starty)
        self.stand_image = self.image
        self.speed = 4
        self.jumpspeed = 20
        self.animation_index = 0
        self.facing_left = False
        self.speed = 4
        self.Vsp = 0
        self.gravity = 1


    def move(self, x, y):
        self.rect.move_ip([x,y])
        
    def update(self,boxes):
        # check keys
        Hsp = 0
        onground = pygame.sprite.spritecollideany(self, boxes)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.facing_left = True
            
            self.move(-self.speed,0)
        elif key[pygame.K_RIGHT]:
            self.facing_left = False
            
            self.move(self.speed,0)
        else:
            self.image = self.stand_image
        if key[pygame.K_LEFT]:
            self.facing_left = True
            
            self.move(-self.speed,0)
        elif key[pygame.K_RIGHT]:
            self.facing_left = False
            
            self.move(self.speed,0)
        else:
            self.image = self.stand_image

        if key[pygame.K_UP]:
            self.Vsp = -self.jumpspeed
        
        if self.Vsp < 10: # 9.8 rounded up
            self.Vsp += self.gravity

        if key[pygame.K_UP] and onground:
            self.Vsp = -self.jumpspeed

        if self.Vsp < 10 and not onground: # 9.8: rounded up
            self.Vsp += self.gravity

        # stop falling when the ground is reached
        if self.Vsp > 0 and onground:
            self.Vsp = 0

        self.move(Hsp,self.Vsp)
    
class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("data/images/tiles/decor/0.png", startx, starty)




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player(100, 200)
    boxes = pygame.sprite.Group()
    for bx in range(0,400,70):
        boxes.add(Box(bx,300))
   
   
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.event.pump()
        player.update(boxes)

        # Draw loop
        screen.fill(BACKGROUND)
        player.draw(screen)
        boxes.draw(screen)
        pygame.display.flip()

        clock.tick(60)
if __name__ == "__main__":
    main()
