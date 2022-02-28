
import pygame
import os
pygame.font.init()


WIDTH, HEIGHT =750, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New try")

#-------- Back ground----------------------
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "backround2.png")),(WIDTH, HEIGHT))
BGS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "backrounss.png")),(WIDTH, HEIGHT))
# 

# --
def main():
    run = True
    FPS = 60
    def redraw_windows():
        WIN.blit(BGS,(0,0))
    while run:
        clock.tick(FPS)
        redraw_window()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        
        

def main_menu():
    title_font = pygame.font.SysFont("comicsans",70)
    run = True
    while run :
        WIN.blit(BG, (0,0))
        title_label = title_font.render("press mouse to begin", 1, (225,225,225))
        WIN.blit(title_label, (int(WIDTH/2) - int(title_label.get_width()/2), 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
   
    
    
main_menu()
