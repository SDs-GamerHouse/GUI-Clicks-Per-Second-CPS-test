# Importing required libaries
import pygame
import time

# Initializing pygame
pygame.init()

# Setting up the window
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CPS Test")

def intro_screen(window):
    running = True
    while running:
        bg = pygame.image.load("Assets/intro screen.png")
        window.blit(bg, (0, 0))

        play_button = pygame.transform.scale(pygame.image.load("Assets/play_button.png"),(400, 90))
        play_button_rect = play_button.get_rect()
        play_button_rect.center = 300, 450
        window.blit(play_button, play_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    menu_screen(window)
                    running = False

        pygame.display.update()

def menu_screen(window):
    running = True
    while running:
        bg = pygame.image.load("Assets/menu screen.png")
        window.blit(bg, (0, 0))

        five_secs_button = pygame.transform.scale(pygame.image.load("Assets/5_secs_button.png"), (500, 136))
        five_secs_button_rect = five_secs_button.get_rect()
        five_secs_button_rect.center = 300, 200
        window.blit(five_secs_button, five_secs_button_rect)

        one_min_button = pygame.transform.scale(pygame.image.load("Assets/1_min_button.png"), (500, 130))
        one_min_button_rect = one_min_button.get_rect()
        one_min_button_rect.center = 300, 400
        window.blit(one_min_button, one_min_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if five_secs_button_rect.collidepoint(event.pos):
                    test(window, 5)
                    running = False
                elif one_min_button_rect.collidepoint(event.pos):
                    test(window, 60)
                    running = False


        pygame.display.update()

def test(window, timer):
    running = True
    count = 0
    start = False
    time_elapsed = timer

    while running and not start:
        bg = pygame.image.load("Assets/click background.png")
        window.blit(bg, (0, 0))

        font = pygame.font.Font(None, 80)
        start_text = font.render("Click To Start!", True, (255, 255, 255), None)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = 300, 300
        window.blit(start_text, start_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start = True
                running = False

        pygame.display.update()

    while start and timer >= 0:
        bg = pygame.image.load("Assets/click background.png")
        window.blit(bg, (0, 0))

        click_box = pygame.transform.scale(pygame.image.load("Assets/click_box.png"), (500, 278))
        click_box_rect = click_box.get_rect()
        click_box_rect.center = 300, 350
        window.blit(click_box, click_box_rect)

        click_text = font.render(f"Clicks: {count}", True, (255, 255, 255), None)
        click_text_rect = click_text.get_rect()
        click_text_rect.center = 300, 125

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click_box_rect.collidepoint(event.pos):
                    count += 1
                    click_text = font.render(f"Clicks: {count}", True, (255, 255, 255), None)

        window.blit(click_text, click_text_rect)
        pygame.display.update()

        time.sleep(1)
        timer -= 1
    
    if time_elapsed == 5:
        end_screen(window, count, time_elapsed)
    elif time_elapsed == 60:
        end_screen(window, count, time_elapsed)

def end_screen(window, clicks, timer):
    font = pygame.font.Font(None, 80)
    text = font.render(f"CPS: {round(clicks/timer, 2)}", True, (255, 255, 255), None)
    text_rect = text.get_rect()
    text_rect.center = 300, 300

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((0, 0, 128))
        window.blit(text, text_rect)
        pygame.display.update()


intro_screen(WINDOW)