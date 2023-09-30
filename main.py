from consts import *
from screens.start_screen.StartScreen import start_screen
from screens.story_screen.StoryScreen import story_screen

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Data Quest")

current_screen = "start_screen"

while True:
    if current_screen == "start_screen":
        current_screen = start_screen(screen)
    elif current_screen == "story_screen":
        current_screen = story_screen(screen)
