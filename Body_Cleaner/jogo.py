import pygame


def inicializa():
        
    pygame.init()

    window_width = 1200
    window_height = 680
    # window_height = int(window_width*0.6)

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('BODY CLEANER')

    eventos()


def eventos():
    
    rodar_jogo = True
    while rodar_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar_jogo = False
    pygame.quit()
    
inicializa()