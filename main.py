from play import *
from user_making_puzzle import *
from about import *


pygame.init()

if __name__ == "__main__" :
    win = pygame.display.set_mode((540, 600))
    win.fill((255, 255, 255))

    pygame.display.set_caption("Sudoku")

    while True: # main game loop
        #drawing the buttons
        term_x = [200, 500]
        term_y = [300, 350, 400, 450]
        for i in range(4) :
            pygame.draw.line(win, (128, 128, 128), (term_x[0], term_y[i]), (term_x[1], term_y[i]))
        for i in range(2) :
            pygame.draw.line(win, (128, 128, 128), (term_x[i], 300), (term_x[i], 450))
                
        fnt = pygame.font.SysFont("comicsans", 40) 
        FNT = pygame.font.SysFont("comicsans", 60)   
        options = ["PLAY", "MAKE & SOLVE", "ABOUT"]
        #render title
        win.blit(FNT.render(("SUDOKU"), 1, (0, 128, 0)), (200, 100))
        text = [fnt.render(options[i], 0, (128, 128, 128)) for i in range(3)]
        for i in range(3):
            win.blit(text[i], (250, term_y[i] + 10))
        for event in pygame.event.get():
            #quit game if user clicks the cross
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #if no quit event is detected
            elif event.type == MOUSEBUTTONDOWN :
                x, y = pygame.mouse.get_pos()
                if x > 200 and x < 400 and y > 300:
                    if y < 350 :
                        PLAY(win)
                        win.fill((255, 255, 255))
                    elif y < 400 :
                        main(win)
                        win.fill((255, 255, 255))
                    elif y < 450 :
                        ABOUT(win)
                        win.fill((255, 255, 255))
                    
        pygame.display.update()
        
