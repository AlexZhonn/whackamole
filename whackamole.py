import pygame
from constants import * 
import random

def draw_grid(screen):
    for i in range(0 , boardcol):
        pygame.draw.line(screen, "black", (i*area,0), (i*area,width),2)
    for i in range(0, boardrow):
        pygame.draw.line(screen, "black", (0,i*area), (length,i*area),2)



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        
        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))
        
        clock = pygame.time.Clock()
        
        running = True
        screen.fill("light green")
        draw_grid(screen)
        screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        while running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a , b = event.pos
                    if a // 32 == 0 and b // 32 == 0:
                        screen.fill("light green")
                        draw_grid(screen)
                        x = random.randrange(1 , 20)
                        y = random.randrange(1 , 16)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x * area ,y * area)))
                        
                    if a // 32 == x and b // 32 == y:
                        screen.fill("light green")
                        draw_grid(screen)
                        x = random.randrange(1 , 20)
                        y = random.randrange(1 , 16)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x * area ,y * area)))
            
            
            pygame.display.flip()
            clock.tick(60)
    
    
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

