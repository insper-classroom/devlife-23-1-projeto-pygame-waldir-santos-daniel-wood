import pygame


def inicializa():
        
    pygame.init()

    window_width = 1200
    window_height = 680
    # window_height = int(window_width*0.6)

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('BODY CLEANER')
    
    background_jogo = pygame.image.load('img/blood_stream.jpg')
    background_jogo_espelhada = pygame.transform.flip(background_jogo, True, False )
    background_jogo_espelhada  = pygame.transform.scale(background_jogo, [1200, 680])

    return window, background_jogo_espelhada


def eventos():
    
    rodar_jogo = True
    while rodar_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
           
        return True
         
    pygame.quit()
                


def desenho(window, background_jogo_espelhada):
    
    window.blit(background_jogo_espelhada, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    


def loop_jogo(window, background_jogo_espelhada):
    while eventos():
        desenho(window, background_jogo_espelhada)

    
if __name__ == '__main__':
    init = inicializa()
    loop_jogo(init[0], init[1])