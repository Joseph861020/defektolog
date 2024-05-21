import pygame

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Игра для изучения русского языка")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Define the buttons globally
card_game_button = None
other_game_button_1 = None
other_game_button_2 = None

# Функция для отображения главного меню
def display_main_menu():
    global card_game_button, other_game_button_1, other_game_button_2 # Declare variables as global
    # Отрисовка фона
    screen.fill(green)

    # Текст для меню
    menu_text = font.render("Выберите игру:", True, white)
    screen.blit(menu_text, (screen.get_width() // 2 - menu_text.get_width() // 2, 100))

    # Кнопка "Карточная игра"
    card_game_button = pygame.Rect(screen.get_width() // 2 - 150, 200, 300, 50)
    pygame.draw.rect(screen, white, card_game_button)
    card_game_text = font.render("Карточная игра", True, black)
    screen.blit(card_game_text, card_game_button.center)

    # Кнопка "Другая игра 1"
    other_game_button_1 = pygame.Rect(screen.get_width() // 2 - 150, 300, 300, 50)
    pygame.draw.rect(screen, white, other_game_button_1)
    other_game_text_1 = font.render("Другая игра 1", True, black)
    screen.blit(other_game_text_1, other_game_button_1.center)

    # Кнопка "Другая игра 2"
    other_game_button_2 = pygame.Rect(screen.get_width() // 2 - 150, 400, 300, 50)
    pygame.draw.rect(screen, white, other_game_button_2)
    other_game_text_2 = font.render("Другая игра 2", True, black)
    screen.blit(other_game_text_2, other_game_button_2.center)

    # Обновление экрана
    pygame.display.flip()

# Главная функция игры
def main():
    running = True
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
                    i_do.run(running) # Запустите функцию run() из card_game.py
                # Проверка, была ли нажата кнопка "Другая игра 1"
                elif other_game_button_1.collidepoint(mouse_pos):
                    # Запуск другой игры 1 из отдельного файла
                    import other_game_1  # Импортируйте файл other_game_1.py
                    other_game_1.run(running) # Запустите функцию run() из other_game_1.py
                # Проверка, была ли нажата кнопка "Другая игра 2"
                elif other_game_button_2.collidepoint(mouse_pos):
                    # Запуск другой игры 2 из отдельного файла
                    import other_game_2  # Импортируйте файл other_game_2.py
                    other_game_2.run(running) # Запустите функцию run() из other_game_2.py
        # Отрисовка главного меню
        display_main_menu()

# Запуск игры
if __name__ == "__main__":
    main()