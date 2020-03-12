import pygame
import os
import bird, background
import Pipe
import Base

pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 50)

def draw(win, bird, bg, pipe, base, score):
    bg.draw(win)
    for p in pipe:
        p.draw(win)
    bird.draw(win)
    base.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (500 - 10 - text.get_width(), 10))

    pygame.display.update()
    
def move(win, bird, pipe, base):
    bird.move()
    bird.keyListener()
    for p in pipe:
        p.move()
    base.move()

def main():
    pygame.init()
    width = 500
    height = 800
    WIN = pygame.display.set_mode((width,height))
    pygame.display.set_icon(pygame.image.load(os.path.join("imgs","bird1.png")))
    pygame.display.set_caption("Flappy Bird")

    run = True
    clock = pygame.time.Clock()

    b = bird.Bird()
    bg = background.bg()
    pipe = Pipe.Pipe()
    pipes = [pipe]
    base = Base.Base()

    score = 0

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('ESC')
                run = False
                pygame.quit()
                quit()


        add_pipe = False
        rem = []
        for p in pipes:
            if p.collide(b):
                run = False

            if not p.passed and p.x < b.x:
                p.passed = True
                add_pipe = True

            if p.x + p.pipe_top.get_width() < 0:
                rem.append(p)


        if add_pipe:
            score += 1
            pipes.append(Pipe.Pipe())

        for r in rem:
            pipes.remove(r)

        move(WIN, b, pipes, base)
        draw(WIN, b, bg, pipes, base, score)


main()