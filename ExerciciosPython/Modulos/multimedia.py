import pygame
from os import system
from Modulos.formatar import cor
from time import sleep
import sys

#Função que irá tocar uma musica indicada como parametro da função
def musica(arq):
    """
    Função que irá tocar uma musica indicada como parametro da função
    Como função, indique o caminho e o nome da musica (em formato MP3)
    Exemplo: 'Media/Almanaque.mp3'
    
    """    
    try:
        #Inicializando o mixer
        pygame.mixer.init()
        
        #Carregando o arquivo indicado como parametro
        pygame.mixer.music.load(arq)
        
        #Iniciando a reprodução do arquivo
        pygame.mixer.music.play()
        
        system("cls")
        print(cor(f"A musica '{arq}' foi carregada com sucesso!",34))
        sleep(1)    
        
        #Variavel referente a um contador
        seg=0
        
        while pygame.mixer.music.get_busy():        
            sleep(1)
            
            #Adicionando +1 a cada segundo passado durante a reprodução da musica
            seg+=1
            
            #Exibindo no console a quantidade de segundos passados, e visualmente excluindo o valor numerico referente ao segundo antecessor
            sys.stdout.write("\r")
            sys.stdout.write(cor(f"A musica está tocando... {seg}",35))
            
            #Atualizando o console
            sys.stdout.flush()             
            
            pass
        print(cor("\nA musica acabou!",34))
    except pygame.error:
        system("cls")
        print(cor("Erro! Caminho ou nome invalido!",31))