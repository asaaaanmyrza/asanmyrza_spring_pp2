import pygame
pygame.init()
size = [1050, 800]
center = [525, 400]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

mickey1 = pygame.image.load("mainclock.png").convert_alpha()
mickey = pygame.transform.scale(mickey1, (1050, 800))

hour_arm1 = pygame.image.load("rightarm.png").convert_alpha()
hour_arm = pygame.transform.rotate((pygame.transform.scale(hour_arm1, (1050, 800))), -45)
hour_rect = hour_arm.get_rect(center = center)

def rotate_arm(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=center)
    screen.blit(rotated_image, rotated_rect)
anglehour=0
angleminute=0

minute_arm1 = pygame.image.load("leftarm.png").convert_alpha()
minute_arm = pygame.transform.scale(minute_arm1, (63, 800))
minute_rect = minute_arm.get_rect(center = center)

running = True
while running:
    anglehour+=0.05
    if(anglehour >= 360):
        anglehour=0
    
    angleminute+=0.5
    if(angleminute >= 360):
        angleminute=0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(mickey, (0, 0)) 
    rotate_arm(minute_arm, angleminute, center)
    rotate_arm(hour_arm, anglehour, center)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()