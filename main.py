import pygame
import time

import sorting_algorithms as sa
import values as v

pygame.init()
screen = pygame.display.set_mode((v.width, v.height))
pygame.display.set_caption("Sorting visualiser by ludius0")

def check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
def update_screen(algorithm, a, b):
    global SORTING, screen
    SORTING = True
    pygame.display.set_caption(f"Sorting visualiser by ludius0     Algorithm: {algorithm.name}     Time: {time.time() - algorithm.start_time} seconds")
    screen.fill(v.WHITE)
    color = v.BLACK
    j = int(v.width/len(algorithm.array))
    for i in range(len(algorithm.array)):
        if a == algorithm.array[i]: color = v.GREEN
        elif b == algorithm.array[i]: color = v.RED
        else: color = v.BLACK
        pygame.draw.rect(screen, color, (i*j, v.height-j, j, algorithm.array[i]*-1))
    check()             # Without it; program could crash
    pygame.display.update()

def main():
    global SORTING
    screen.fill(v.BLACK)
    bubble_sort = pygame.draw.rect(screen, v.WHITE, (int(v.width/2-150),90,300,70))
    quick_sort = pygame.draw.rect(screen, v.WHITE, (int(v.width/2-150),190,300,70))
    insertion_sort = pygame.draw.rect(screen, v.WHITE, (int(v.width/2-150),290,300,70))
    bogo_sort = pygame.draw.rect(screen, v.WHITE, (int(v.width/2-150),390,300,70))

    alg = {"BubbleSort": sa.BubbleSort(),
           "QuickSort": sa.QuickSort(),
           "InsertionSort": sa.InsertionSort(),
           "BogoSort": sa.BogoSort()}

    SORTING = False
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and SORTING == False:
                # Positions of (x, y) of algorithm Rect
                if pygame.mouse.get_pos()[0] >= int(v.width/2-150) and pygame.mouse.get_pos()[0] <= int(v.width/2+150): 
                    if pygame.mouse.get_pos()[1] >= 90 and pygame.mouse.get_pos()[1] <= 90+70:
                        #pygame.draw.rect(screen, v.RED, (int(v.width/2-151),91,301,71))
                        alg["BubbleSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= int(v.width/2-150) and pygame.mouse.get_pos()[0] <= int(v.width/2+150): 
                    if pygame.mouse.get_pos()[1] >= 190 and pygame.mouse.get_pos()[1] <= 190+70:
                        alg["QuickSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= int(v.width/2-150) and pygame.mouse.get_pos()[0] <= int(v.width/2+150): 
                    if pygame.mouse.get_pos()[1] >= 290 and pygame.mouse.get_pos()[1] <= 290+70:
                        alg["InsertionSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= int(v.width/2-150) and pygame.mouse.get_pos()[0] <= int(v.width/2+150): 
                    if pygame.mouse.get_pos()[1] >= 390 and pygame.mouse.get_pos()[1] <= 390+70:
                        alg["BogoSort"].play()
                        flag = False

        pygame.display.update()

if __name__ == "__main__":
    main()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_r]:
                    main()
                    break
