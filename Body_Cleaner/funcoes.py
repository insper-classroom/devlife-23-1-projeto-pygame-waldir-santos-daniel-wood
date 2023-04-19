import pygame


def inicializa():
        
    pygame.init()

    window_width = 1200
    window_height = 680

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('BODY CLEANER')
    
    background_jogo = pygame.image.load('img/blood_stream_02.jpg')
    background_jogo_espelhada = pygame.transform.flip(background_jogo, True, False )
    background_jogo_espelhada  = pygame.transform.scale(background_jogo_espelhada, [1200, 680])


    objetos = {}
    objetos['globulo_branco'] = pygame.image.load('img/globulo_branco.jpg')
    objetos['globulo_branco'] = pygame.transform.scale(objetos['globulo_branco'], [119//3, 115//3])
    
    estados = {'t0' : -1,
                'tempo_atualizado': -1,
                'globulo_branco_pos': [0, 320],
                'globulo_branco_vel': [0, 0]           
    }

    return window, background_jogo_espelhada, objetos, estados


def eventos(objetos, estados):
    
    
    pygame.time.Clock().tick(30)
   
    tempo = pygame.time.get_ticks()
    delta_t = 0
    
    if estados['tempo_atualizado'] >= 0:  # Ignora a primeira vez
        delta_t = tempo - estados['tempo_atualizado']  
    estados['tempo_atualizado'] = tempo
   
    estados['globulo_branco_pos'][0] = estados['globulo_branco_pos'][0] + estados['globulo_branco_vel'][0] * delta_t/1000 #Posição X (deslocamento horizontal)
    estados['globulo_branco_pos'][1] = estados['globulo_branco_pos'][1] + estados['globulo_branco_vel'][1] * delta_t/1000 #Posição Y (deslocamento vertical)
    
    if estados['globulo_branco_pos'][0] < 0:
        estados['globulo_branco_pos'][0] = 0
    if estados['globulo_branco_pos'][0] + 119//3 > 1200:
        estados['globulo_branco_pos'][0] = 1200 - 119//3
       
    if estados['globulo_branco_pos'][1] < 0:
        estados['globulo_branco_pos'][1] = 0
    if estados['globulo_branco_pos'][1] + 115//3 > 680:
        estados['globulo_branco_pos'][1] = 680 - 115//3

    
    
    rodar_jogo = True
    while rodar_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
           
        return True
         
    pygame.quit()
                

def desenho(window, background_jogo_espelhada, objetos, estados):
    
    window.blit(background_jogo_espelhada, (0, 0))
    # pygame.display.flip()
    
    window.blit(objetos['globulo_branco'], estados['globulo_branco_pos'])
    pygame.display.update()
    
  
        

def loop_jogo(window, background_jogo_espelhada, objetos, estados):
    while eventos(objetos, estados):
        desenho(window, background_jogo_espelhada, objetos, estados)

    
if __name__ == '__main__':
    init = inicializa()
    loop_jogo(init[0], init[1], init[2], init[3])