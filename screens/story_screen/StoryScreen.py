import sys
from consts import *

font = pygame.font.Font(None, 36)


def story_screen(screen):
    running = True
    background = pygame.image.load(background_story)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    story_text = font.render("Здесь ваша история...", True, BLACK)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        screen.blit(story_text, (50, 500))

        next_button = pygame.Rect(WIDTH - 100, HEIGHT - 50, 80, 40)
        pygame.draw.rect(screen, BLACK, next_button)
        next_text = font.render("Далее", True, WHITE)
        screen.blit(next_text, (705, 560))

        pygame.display.flip()

        mouse_pos = pygame.mouse.get_pos()
        if next_button.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
