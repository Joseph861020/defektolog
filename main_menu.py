import pygame

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

pygame.display.set_caption("Игра для изучения русского языка")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
background = (255, 251, 213)
red = (255, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Define the buttons globally
card_game_button = None
will_eat_button = None
other_game_button_2 = None

# Load the background music
pygame.mixer.music.load("assets/sounds/background.wav")
pygame.mixer.music.set_volume(0.2)  # Set initial volume to 0.3 (lower)
audio_paused = False  # Flag to track if music is paused


# Function to start background music
def play_background_music():
    pygame.mixer.music.play(-1)  # Play music on a loop (-1)


# Function to pause background music
def pause_background_music():
    pygame.mixer.music.pause()
    audio_paused = True


# Function to unpause background music
def unpause_background_music():
    pygame.mixer.music.unpause()
    audio_paused = False


# Функция для отображения главного меню
def display_main_menu():
    global card_game_button, will_eat_button, other_game_button_2  # Declare variables as global
    # Отрисовка фона
    screen.fill(background)

    # Текст для меню
    menu_text = font.render("Выберите игру:", True, white)
    screen.blit(menu_text, (screen.get_width() // 2 - menu_text.get_width() // 2, 100))

    # Кнопка "Карточная игра"
    card_game_button = pygame.Rect(screen.get_width() // 2 - 150, 200, 300, 50)
    pygame.draw.rect(screen, white, card_game_button)  # Draw the white rectangle for the button
    card_game_text = font.render("Карточная игра", True, black)
    text_rect = card_game_text.get_rect(center=card_game_button.center)  # Get the center of the button
    screen.blit(card_game_text, text_rect)  # Blit the text at the center of the button

    # Кнопка "Другая игра 1"
    will_eat_button = pygame.Rect(screen.get_width() // 2 - 150, 300, 300, 50)  # will_eat_button
    pygame.draw.rect(screen, white, will_eat_button)
    will_eat_text = font.render("Я буду", True, black)
    text_rect = will_eat_text.get_rect(center=will_eat_button.center)  # Get the center of the button
    screen.blit(will_eat_text, text_rect)  # Blit the text at the center of the button

    # Кнопка "Другая игра 2"
    other_game_button_2 = pygame.Rect(screen.get_width() // 2 - 150, 400, 300, 50)
    pygame.draw.rect(screen, white, other_game_button_2)
    other_game_text_2 = font.render("Другая игра 2", True, black)
    text_rect = other_game_text_2.get_rect(center=other_game_button_2.center)  # Get the center of the button
    screen.blit(other_game_text_2, text_rect)  # Blit the text at the center of the button


# Главная функция игры
def main():
    global card_game_button, will_eat_button, other_game_button_2
    running = True
    play_background_music()
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Проверка, была ли нажата кнопка "Карточная игра"
                if card_game_button.collidepoint(mouse_pos):
                    # Запуск карточной игры из отдельного файла
                    import i_do  # Импортируйте файл card_game.py
                    i_do.run(running, pause_background_music,
                             unpause_background_music)  # Запустите функцию run() из card_game.py
                # Проверка, была ли нажата кнопка "Другая игра 1"
                elif will_eat_button.collidepoint(mouse_pos):
                    # Запуск другой игры 1 из отдельного файла
                    import will_eat  # Импортируйте файл other_game_1.py
                    will_eat.run(running, pause_background_music,
                                 unpause_background_music)  # Запустите функцию run() из other_game_1.py
                # Проверка, была ли нажата кнопка "Другая игра 2"
                elif other_game_button_2.collidepoint(mouse_pos):
                    # Запуск другой игры 2 из отдельного файла
                    import other_game_2  # Импортируйте файл other_game_2.py
                    other_game_2.run(running, pause_background_music,
                                     unpause_background_music)  # Запустите функцию run() из other_game_2.py
            elif event.type == pygame.ACTIVEEVENT:
                if event.state == 2:  # Minimized
                    pause_background_music()
                elif event.state == 1:  # Restored
                    unpause_background_music()
        # Отрисовка главного меню
        display_main_menu()
        pygame.display.flip()  # Call flip outside of display_main_menu()


# Запуск игры
if __name__ == "__main__":
    main()
