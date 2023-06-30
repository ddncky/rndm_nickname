import pygame as p
import Button as b
import GeneratorEngine


WIDTH = 612
HEIGHT = 433


def main():
    p.init()
    start_screen = p.display.set_mode((WIDTH, HEIGHT))
    start_screen.fill(p.Color('pink'))
    p.display.set_caption('bla')
    clock = p.time.Clock()
    running = True

    start_img = p.image.load("pics/startbutton.png")
    fon_img = p.image.load("pics/fon.jpeg")
    start_button = b.Buton(-85, 20, start_img, 1)

    while running:
        start_screen.blit(fon_img, (0, 0))

        if start_button.drawButtons(start_screen):
            running = False

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        p.display.flip()


main()