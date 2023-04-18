import pygame


def inicializa():
        
    pygame.init()

    window_width = 1200
    window_height = 680

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('BODY CLEANER')
    
    background_jogo = pygame.image.load('img/blood_stream.jpg')
    background_jogo_espelhada = pygame.transform.flip(background_jogo, True, False )
    background_jogo_espelhada  = pygame.transform.scale(background_jogo_espelhada, [1200, 680])


    objetos = {}
    objetos['globulo_branco'] = pygame.image.load('img/globulo_branco.jpg')
    objetos['globulo_branco'] = pygame.transform.scale(objetos['globulo_branco'], [119//3, 115//3])

    return window, background_jogo_espelhada, objetos


def eventos():
    
    rodar_jogo = True
    while rodar_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
           
        return True
         
    pygame.quit()
                

def desenho(window, background_jogo_espelhada, objetos):
    
    window.blit(background_jogo_espelhada, (0, 0))
    # pygame.display.flip()
    
    window.blit(objetos['globulo_branco'], (0, 320))
    pygame.display.update()
    
  
        

def loop_jogo(window, background_jogo_espelhada, objetos):
    while eventos():
        desenho(window, background_jogo_espelhada, objetos)

    
if __name__ == '__main__':
    init = inicializa()
    loop_jogo(init[0], init[1], init[2])