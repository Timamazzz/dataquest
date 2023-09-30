import sys
from consts import *

font = pygame.font.Font(None, 36)


def start_screen(screen):
    running = True

    # Тексты
    title_text = font.render("Data Квест", True, WHITE)
    title_text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4 - 20))

    info_text = font.render("впиши свое имя в историю", True, WHITE)
    info_text_rect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 20))

    input_box_width = WIDTH // 4  # Ширина инпута
    input_box = pygame.Rect((WIDTH - input_box_width) // 2, HEIGHT // 2 - 20, input_box_width, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)

        screen.blit(title_text, title_text_rect)
        screen.blit(info_text, info_text_rect)

        txt_surface = font.render(text, True, color)
        width = max(WIDTH // 4, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        start_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 100, WIDTH // 2, 50)
        pygame.draw.rect(screen, BLACK, start_button)
        start_text = font.render("Старт", True, WHITE)
        start_text_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_text_rect)

        exit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 30, WIDTH // 2, 50)
        pygame.draw.rect(screen, BLACK, exit_button)
        exit_text = font.render("Выйти", True, WHITE)
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()

        mouse_pos = pygame.mouse.get_pos()
        if exit_button.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        if start_button.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return "story_screen"
