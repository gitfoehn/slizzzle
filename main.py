import pygame
from constants import RESOLUTION
from enums import Colors
import sys

from slizzle.slizzle_controller import SlizzleController

game_started = False
menu = True


def create_pygame_window():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
                    running = False

        # Background-Color
        screen.fill(Colors.CAMBRIDGE_BLUE)

        button_rect = pygame.Rect(250, 200, 200, 50)
        button_color = (0, 200, 0)
        button_text = "Quit"
        button_font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, button_color, button_rect)

        button_label = button_font.render(button_text, True, (255, 255, 255))
        screen.blit(button_label, (button_rect.x + button_rect.width // 2 - button_label.get_rect().width // 2,
                                   button_rect.y + button_rect.height // 2 - button_label.get_rect().height // 2))
        pygame.display.flip()
    pygame.quit()


def show_image():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    image = pygame.image.load("assets/bregenzerwald.jpg")
    rect = image.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    sys.exit()

        screen.blit(image, image.get_rect(center=image.get_rect().center))
        pygame.display.flip()


if __name__ == '__main__':
    controller = SlizzleController()
    controller.start_game()
    # show_image()

    # view = View()
    # view.show_game_view()
