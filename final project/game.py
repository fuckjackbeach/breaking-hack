import pygame
import sys
import time
import os


WIDTH = 632
HEIGHT = 421
BACKGROUND = pygame.image.load("data/images/classroom.png")
loading_screen = pygame.image.load("data/loadingscreen/breakinghack.png")

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

class LoadingScreen:
    def __init__(self, screen, audio_file_path):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.finished_loading = False
        self.audio_file_path = audio_file_path

    def run(self):
        # Play loading screen music
        play_audio(self.audio_file_path)

        while not self.finished_loading:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(loading_screen, (0, 0))
            pygame.display.flip()

            # Simulate loading time (replace with actual loading)
            time.sleep(5)

            self.finished_loading = True

            self.clock.tick(60)

class ScrollingText:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.messages = [
                        "Loudspeaker: Attention staff and students.",
                        "There has been a security breach to the",
                        "YRDSB network and Teachassist servers ", 
                        "And the schools wifi is expected be to out ",
                        "For the next few days.",
                        "Mr.Park: thats strange, who would do that?",
                        "Loudspeaker: It just turns out that",
                        "The stolen data was sold $1.3 Million"
                        "Mr. Park: Hmmm... (next level)",
                        "Mr.Park: Well that's really weird.",
                        "Someone just released the YRDSB source code.",
                        "Let's do some digging, i bet something in theres cool.",
                        "Teachers Income, Student Ratings, Principal Tapes",
                        "Oh, Jack Beach grades, lets see... LOL he failing.",
                        "You know something about these codes seem familiar...",
                        "Wait, does that say W3STi3?",
                        "Thats my old student Marshall's last name...",
                        "Oh my god, he forgot to hide his IP address.SMH.",
                        "It's traced back to 39 Dunning Avenue.",
                        "I'm sure the school still has his records on file.",
                        "Ha-ha, i knew it! What should i do?",
                        "I know what i should do... ",
                        "But i need money to payt off my gambling debts.",
                        "Or they'll kill me...(next level)",
                        "Mr.Park: Marshall, I can't believe it...",
                        "It was you. You hacked the school servers.",
                        "Marshall: How'd you find me?",
                        "Mr.Park: Your infos still in the schools system",
                        "Marshall: Get out of here, OR ELSE!",
                        "Mr.Park: Calm down, nobodys looking for you.",
                        "Marshall: Why are you here?",
                        "Mr.Park: You know, i never expected much of you.",
                        "But, hacking. Wow.",
                        "Theres a lot of money in it, huh?",
                        "Marshall: I dont know what youre talking about.",
                        "Mr.Park: No?",
                        "W3STi3, Thats not you? ",
                        "Dont lie, im certain it's you, I tracked your IP.",
                        "Marshall: Look, Mr. Park...",
                        "Im not sure what it is you think you're doing here.",
                        "But, if youre gonna tell me to turn myself in",
                        "Its not happening, yo.",
                        "Mr.Park: Can i ask you something?",
                        "You lost your partner today, right? J.Wen?",
                        "Well i was thinking...",
                        "You know the business,",
                        "And i know the coding...",
                        "I was thinking maybe you and I could partner up.",
                        "Fin"
                          ]
        self.current_message_index = 0
        self.font = pygame.font.Font(None, 36)
        self.black_box = pygame.Surface((WIDTH, 100))
        self.black_box.fill((0, 0, 0))

    def show_next_message(self):
        self.current_message_index += 1
        if self.current_message_index >= len(self.messages):
            self.current_message_index = 0

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.show_next_message()

        # Draw the black box at the bottom
        self.screen.blit(self.black_box, (0, HEIGHT - 100))

        # Draw the message on the black box
        message_surface = self.font.render(self.messages[self.current_message_index], True, (255, 255, 255))
        self.screen.blit(message_surface, (10, HEIGHT - 80))

    def run(self):
        # Draw loop
        self.screen.blit(BACKGROUND, (0, 0))
        self.draw()
        pygame.display.flip()
        self.clock.tick(60)
class Level:
    def __init__(self, background_image, ground_segments):
         self.background_image = pygame.image.load(background_image)
         self.boxes = pygame.sprite.Group()

        # Create boxes for each ground segment
         for segment in ground_segments:
            self.boxes.add(Box(*segment))


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

class Box(Sprite):
    def __init__(self, startx, starty, width,height):
        super().__init__("data/images/tiles/decor/0.png", startx, starty)

        
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.topleft = (startx, starty)

class Player(Sprite):
   
    def __init__(self, startx, starty):
        super().__init__("data/sprite/mrparkyo.png", startx, starty)
        self.stand_image = self.image
        self.speed = 4
        self.jumpspeed = 20
        self.facing_left = False
        self.speed = 4
        self.Vsp = 0
        self.gravity = 1

    def move(self, x, y):
        self.rect.move_ip([x,y])

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

class NPC(Sprite):
    def __init__(self, image, startx, starty):
        super().__init__(image, startx, starty)
        self.speed = 2  # Adjust the walking speed
        self.hesitate_frames = 60  # Adjust the number of frames for hesitation
        self.current_frame = 0
        self.direction = 1  # 1 represents walking right, -1 represents walking left
        self.Vsp = 0  # Vertical speed
        self.gravity = 1  # Gravity constant
        self.onground = False  # Initialize onground as False

    def apply_gravity(self):
        if self.Vsp < 10: # 9.8 rounded up
            self.Vsp += self.gravity

        if self.Vsp < 10 and not self.onground: # 9.8: rounded up
            self.Vsp += self.gravity

        if self.Vsp > 0 and self.onground:
            self.Vsp = 0
        self.rect.y += self.Vsp

    def move_behaviors(self):
        # NPC walking behavior
        if self.current_frame < self.hesitate_frames:
            # NPC hesitates for a certain number of frames
            self.current_frame += 1
        else:
            # NPC walks in the specified direction
            self.rect.x += self.direction * self.speed

            # Change direction when reaching the screen edges
            if self.rect.right > WIDTH or self.rect.left < 0:
                self.direction *= -1  # Reverse direction

        # Reset frame count for the next loop
        if self.current_frame >= 2 * self.hesitate_frames:
            self.current_frame = 0

    def update(self, boxes):
        self.onground = pygame.sprite.spritecollideany(self, boxes)
        self.apply_gravity()
        self.move_behaviors()

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        level1_ground_segments = [(0, HEIGHT - 120, WIDTH, 20)]
        level2_ground_segments = [(0, HEIGHT - 120, WIDTH, 20)]
        level3_ground_segments = [(0, HEIGHT - 120, WIDTH, 20)]

        self.levels = [
            Level("data/images/classroom.png", level1_ground_segments),
            Level("data/images/house.jpg", level2_ground_segments),
            Level("data/images/background.jpg", level3_ground_segments),
                ]
        self.current_level_index = 0
        self.current_level = self.levels[self.current_level_index]
        self.player = Player(100, 200)
        self.npc = NPC("data/sprite/westiepinkmanyo.png", 400, 200)

    def switch_to_next_level(self):
        self.current_level_index += 1
        if self.current_level_index < len(self.levels):
            self.current_level = self.levels[self.current_level_index]
            self.player.rect.x = 100  # Reset player's x-coordinate
            self.npc.rect.x = 400  # Reset NPC's x-coordinate
            return True
        else:
            return False
    
    def run(self, scrolling_text):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.level = self.current_level
            self.player.update(self.current_level.boxes)  # Pass the boxes to the update method

            # Update NPC if it exists
            if self.npc:
                self.npc.update(self.current_level.boxes)  # Pass the boxes to the update method

            # Draw loop
            self.screen.blit(self.current_level.background_image, (0, 0))
            scrolling_text.draw()
            self.player.draw(self.screen)

            # Draw NPC if it exists
            if self.npc:
                self.npc.draw(self.screen)

            self.current_level.boxes.draw(self.screen)
            pygame.display.flip()

            # Check if the player reached the right side of the screen
            if self.player.rect.x > WIDTH:
                if not self.switch_to_next_level():
                    # No more levels, exit the game
                    pygame.quit()
                    sys.exit()

            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()

    audio_file_path_loading = "data/breakingbadtheme.mp3"
    loading_screen_instance = LoadingScreen(pygame.display.set_mode((WIDTH, HEIGHT)), audio_file_path_loading)
    loading_screen_instance.run()

    scrolling_text_instance = ScrollingText(pygame.display.set_mode((WIDTH, HEIGHT)))
    game = Main()

    game.run(scrolling_text_instance)

    pygame.quit()
    sys.exit()

#ONLY PUT MARSHALL ON LAST LEVEL WTF IS GOING ON