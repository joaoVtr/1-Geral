'''# Faça um programa que desenhe a seguinte situação de um jogo da velha na tela:
O| |X
-----
O|X|
-----
O|X|O
O fundo da tela deve ser Branco
Deverá estar escrito centralizado em cima do tabuleiro o título "Jogo da Velha"na cor
Preto.
O tabuleiro, no tamanho e na posição que você preferir, deverá estar na cor Steel Azul
As jogadas "X"deverão ser desenhados como duas linhas cruzadas e estar na cor Verde
Hunter
As jogadas "O"deverão ser desenhadas círculos não preenchidos estar na cor Vermelho
Indiano
Deverá ter um traço em cima do trio vencedor com uma cor aleatória e largura aleatória
entre 1 e 10.'''
import pygame, sys
from pygame.locals import * 

pygame.init()

blue = (0, 50, 255)
white = (255, 255, 255)
black = (0, 0, 0)
vermelho = (255, 0, 0)

width = 500 
height = 400 

tela = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Jogo da Velha")
tela.fill(white)

#Criar Retângulo
def gnrt_rect(x,y,w ,h, esp):
	espe_linha = 4 # Espessura da linha 
	data_list = []
	bk_y = y
	for i in range (3):
		for j in range(3):
			pygame.draw.rect(tela, black, (x, y, w, h), 1)
			data_list.append([(x,y),(x+w, y+h)])
			if i != 2:
				linha_posx = x + w + esp/2
				pygame.draw.line(tela, black, (linha_posx - 1, y), (linha_posx - 1, y + h - 1), espe_linha)
			y += h + esp
		x+= w + esp
		y = bk_y
	return data_list

# Criar local de jogo
def gnrt_board():
	y = 70
	h = 70
	w = 70
	esp = 10 #espaçamento entre os rentangulos
	x = width/2 - (3*w + 2* esp)/2
	data_list = gnrt_rect(x, y, w, h,esp)
	print(data_list)
gnrt_board()

fonte_txt = pygame.font.SysFont(None, 32)
texto = fonte_txt.render("Jogo da Velha", True, black )
texto_rect = texto.get_rect()
texto_rect.centerx = width/2
texto_rect.centery = 15

tela.blit(texto,texto_rect)

pygame.display.update()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		# print(pygame.mouse.get_pos())