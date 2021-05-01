import pygame
from handle_dice import Dice_handler

pygame.font.init()
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Roll a die")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS=60
NUMBER_FONT = pygame.font.SysFont('lucidasans',35)
TOTAL_FONT = pygame.font.SysFont('malgungothic',38)


def draw_screen(dices, buttons, roll_button, total_str):
    SCREEN.fill((255,255,255))
    for row in dices:
        for die in row:
            die.update(SCREEN, NUMBER_FONT)
    pygame.draw.rect(SCREEN, (0,255,0), pygame.Rect(100, 50, 600, 450),  2)   

    for button in buttons:
        pygame.draw.rect(SCREEN, (255,255,100), button) 

    draw_total_text = TOTAL_FONT.render('Total: '+ str(total_str), 1,(0,0,0))
    SCREEN.blit(draw_total_text, ((68*7), 525))
    pygame.draw.rect(SCREEN, (255,255,100), roll_button) 
    pygame.display.update()

def main():
    pygame.init()

    clock = pygame.time.Clock()
    run=True

    buttons = []
    roll_button = pygame.Rect(100 + (80*7), 525, 75, 50)

    for i in range(6):
        buttons.append(pygame.Rect(100 + (60*i), 525, 50, 50))

    dice_controler = Dice_handler(600,450,(100,50))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(mouse_pos) and i!=5 and len(dice_controler.dice)<=4:
                        dice_controler.create_die(2*i+4)
                        break
                    elif buttons[i].collidepoint(mouse_pos) and i==5 and len(dice_controler.dice)<=4:
                        dice_controler.create_die(20)  
                        break  
                for row in dice_controler.dice:
                    for die in row:
                        if pygame.Rect(die.center[0]-die.radius,die.center[1]-die.radius,2*die.radius,2*die.radius).collidepoint(mouse_pos):
                            dice_controler.delete_die(die)
                            break
                if roll_button.collidepoint(mouse_pos):
                    dice_controler.roll_dice()
        draw_screen(dice_controler.dice,buttons, roll_button, dice_controler.total)        
    main()


if __name__=='__main__':
    main()    