"""Desafio 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame
from time import sleep

musicas=["./Media/Almanaque.MP3","./Media/Tropea.MP3","./Media/Marakesh!.MP3"]

while True:
    c=int(input("Escolha uma musica:\n1)Almanaque\n2)Tropea\n3)Marakesh!\n"))

    if c==1:
        c=musicas[0]
    elif c==2:
        c=musicas[1]
    elif c==3:
        c=musicas[2]    
    
    pygame.mixer.init()

    pygame.mixer.music.load(c)

    pygame.mixer.music.play()

    print(f"Musica escolhida: {c}")
    print("Tocando a musica...")
    while pygame.mixer.music.get_busy():
        pass
    print("A musica acabou")
    sleep(3)