import pygame
from handle_dice import Dice_handler

pygame.font.init()
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Roll a die")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS=60
NUMBER_FONT = pygame.font.SysFont('lucidasans',35)
TOTAL_FONT = pygame.font.SysFont('malgungothic',38)
BUTTON_FONT = pygame.font.SysFont('lucidasans', 18, bold=True)
TITLE_FONT = pygame.font.SysFont('malgungothic', 30, bold=True)


def draw_screen(dices, buttons, roll_button, total_str):
    SCREEN.fill((255,255,255))
    for row in dices:
        for die in row:
            die.update(SCREEN, NUMBER_FONT)
    pygame.draw.rect(SCREEN, (0,255,0), pygame.Rect(100, 50, 600, 450),  2)   

    for i in range(len(buttons)):
        pygame.draw.rect(SCREEN, (255,255,100), buttons[i])
        if i==5:
            SCREEN.blit(BUTTON_FONT.render(str(20), 1,(0,0,0)),(117 + (60*i), 538))
        else:
            SCREEN.blit(BUTTON_FONT.render(str(2*i+4), 1,(0,0,0)),(117 + (60*i), 538))

    draw_total_text = TOTAL_FONT.render('Total: '+ str(total_str), 1,(0,0,0))
    SCREEN.blit(draw_total_text, ((68*7), 525))
    pygame.draw.rect(SCREEN, (255,255,100), roll_button) 
    SCREEN.blit(BUTTON_FONT.render('Roll', 1,(0,0,0)),(120 + (80*7), 538))
    SCREEN.blit(TITLE_FONT.render('Roll The Dice', 1,(0,0,0)),(300, 10))
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