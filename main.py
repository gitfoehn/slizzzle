import pygame

def create_pygame_window():
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Slizzle")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")

        screen.fill((250, 250, 153))

        button_rect = pygame.Rect(250, 200, 200, 50)
        button_color = (0, 200, 0)
        button_text = "Quit"
        button_font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, button_color, button_rect)
        button_label = button_font.render(button_text, True, (255, 255, 255))
        screen.blit(button_label, (button_rect.x + button_rect.width // 2 - button_label.get_rect().width // 2, button_rect.y + button_rect.height // 2 - button_label.get_rect().height // 2))
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    create_pygame_window()