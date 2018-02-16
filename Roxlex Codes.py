
"""
Rolex_pt1

Description:
"""
import tsk
import pygame
pygame.init()
import random
window = pygame.display.set_mode([1018,573])
drawing = True
back = tsk.Sprite("Fair.jpg", 0, 0)
dart = tsk.Sprite("Dart.png",500,500)

c = pygame.time.Clock()
dart_flying = False
current_why = 0
why = 0 
strength = 0
dart.scale = 1.0
mouse = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouse:
            dart_flying = True
            mouse = False 
            why = pygame.mouse.get_pos()
            why[1]
            
            current_why = why[1]
    if mouse:
        x, y = pygame.mouse.get_pos()
        dart.center = x, y
        strength = why 
        
    if dart.center_y <= 500 and dart_flying == False:
        dart.center_y = 500
    if dart_flying == True:
        current_why /= 600
        
        dart.scale -= current_why
        dart.center_y -= 20
    c.tick(30)
    back.draw()
    dart.draw()
    pygame.display.flip()
