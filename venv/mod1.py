import numpy as np
import cv2
import pygame
import os, sys, time

R = True
L = False
U = False
D = False

snake = [[4,4], [4,3], [4,2]]
head = snake[0]
tail = snake[-1]

def move_right():
    global R, L, U, D,board, head, tail, snake
    if head[0] < 8:
        tail = snake[-1]
        board[head[1]][head[0]+1] = "b"
        board[tail[1]][tail[0]] = " "
        head[0] += 1
        tail = snake[-1]
        snake.insert(0,head)
        snake = snake [:-1]

        R = True
        L = False
        U = False
        D = False
    print (tail)

def move_left(board, headX, headY):
    if headX >1:
        board[headY][headX] = " "
        board[headY][headX-1] = "h"
        headX -= 1
        global R, L, U, D
        R = False
        L = True
        U = False
        D = False
    return board, headX, headY

def move_up(board, headX, headY):
    if headY >1:
        board[headY][headX] = " "
        board[headY-1][headX] = "h"
        headY -= 1
        global R, L, U, D
        R = False
        L = False
        U = True
        D = False
    return board, headX, headY

def move_down(board, headX, headY):
    if headY < 8:
        board[headY][headX] = " "
        board[headY+1][headX] = "h"
        headY += 1
        global R, L, U, D
        R = False
        L = False
        U = False
        D = True
    return board, headX, headY


board = [[ " " ] * 10, [ " " ] * 10, [ " " ] * 10,[ " " ] * 10,[ " " ] * 10,
         [ " " ] * 10, [ " " ] * 10,[ " " ] * 10,[ " " ] * 10,[ " " ] * 10 ]



for i in range (0,10):
    for j in range(0, 10):
        if (i == 0 or i == 9):
            board[i][j] = "x"
        if (j == 0 or j == 9):
            board[i][j] = "x"

for i in snake:
    board[i[0]][i[1]] = "b"

print ("\n" * 100)
for i in range (0,10):
    print(board[i], end="\n")

# janela
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    key_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # move right
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and head[0]<8:
            key_pressed = True
            move_right()
            print ("\n" * 100)
            print(head)
            for i in range(0, 10):
                print(board[i], end="\n")

        # move left
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and headX>1:
            key_pressed = True
            board, headX, headY = move_left(board, headX, headY)
            print ("\n" * 100)
            print(headX, headY)
            for i in range(0, 10):
                print(board[i], end="\n")

        # move up
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and headY>1:
            key_pressed = True
            board, headX, headY = move_up(board, headX, headY)
            print ("\n" * 100)
            print(headX, headY)
            for i in range(0, 10):
                print(board[i], end="\n")

        # move down
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and headY<8:
            key_pressed = True
            board, headX, headY = move_down(board, headX, headY)
            print ("\n" * 100)
            print(headX, headY)
            for i in range(0, 10):
                print(board[i], end="\n")

    if R and not key_pressed:
        move_right()
    # elif L and not key_pressed:
    #     board, headX, headY = move_left(board, headX, headY)
    # elif U and not key_pressed:
    #     board, headX, headY = move_up(board, headX, headY)
    # elif D and not key_pressed:
    #     board, headX, headY = move_down(board, headX, headY)

    # desenhando tabuleiro
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == "x":
                pygame.draw.rect(screen, (92, 64, 51), pygame.Rect(i * 20, j * 20, 20, 20))
            else:
                pygame.draw.rect(screen, (153, 204, 50), pygame.Rect(i * 20, j * 20, 20, 20))

    # desenhando snake
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == "b":
                pygame.draw.rect(screen, (0, 127, 255), pygame.Rect(j * 20, i * 20, 20, 20))



    time.sleep(0.3)

    pygame.display.flip()