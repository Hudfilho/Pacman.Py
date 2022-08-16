import pygame

pygame.init()

amarelo = (255,255,0)
preto = (0,0,0)
velocidade = 1

def bola(cor,r):
    tela.fill(preto)
    pygame.draw.circle(tela, cor, (int(x), int(y)), r, )
    pygame.display.update()

tela = pygame.display.set_mode((640,480),0)
x=10
y=240
vel_x=velocidade
vel_y=velocidade

while True:
    #Calcula regras
    x += vel_x
    y += vel_y

    if x>610:
        vel_x= -velocidade
    if x<30:
        vel_x = velocidade
    if y>450:
        vel_y = -velocidade
    if y<30:
        vel_y = velocidade

    #Pinta
    bola((amarelo),30)

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()