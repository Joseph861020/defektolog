import time

import pygame

from cards import Card
from main_menu import screen, play_background_music

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
background = (255,251,213)
red = (255, 0, 0)

# Загрузка изображений
image1 = pygame.image.load("assets/images/i_do/picture1.png").convert_alpha()
image2 = pygame.image.load("assets/images/i_do/picture2.png").convert_alpha()
image3 = pygame.image.load("assets/images/i_do/picture3.png").convert_alpha()

# Загрузка звуковых эффектов
sound1 = pygame.mixer.Sound("assets/sounds/sound1.wav")
sound2 = pygame.mixer.Sound("assets/sounds/sound2.wav")
sound3 = pygame.mixer.Sound("assets/sounds/sound3.wav")

# Данные карточек
card_data = [
    {"image": image1, "sound": sound1, "text": ""},
    {"image": image2, "sound": sound2, "text": ""},
    {"image": image3, "sound": sound3, "text": ""}
]

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Создание экземпляров карточек
card_width = 150
card_height = 200
cards = []
for i, data in enumerate(card_data):
    card_x = 100 + (i * (card_width + 100))  # Добавляем 100 пикселей между картами
    card_y = 100
    # Pass font and black to the Card constructor
    cards.append(Card(data["image"], data["sound"], data["text"], card_x, card_y, font, black))

# Игровой цикл
clock = pygame.time.Clock()  # For animation


def run(running, pause_music, unpause_music):  # Accept running as an argument
    back_button = None
    play_background_music()
    while running:  # Use the passed running variable
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the game loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for card in cards:
                    if card.is_clicked(mouse_pos):
                        card.sound.play()
                        card.growing = True  # Start the growing animation
                        card.moving_to_center = True  # Start moving to the center
                        card.z_index = 100  # Move card to the top
                        card.center_time = time.time()  # Record the time when the card reached the center
                if back_button and back_button.collidepoint(mouse_pos):
                    running = False  # Exit the game loop
            # Handle window focus change
            elif event.type == pygame.ACTIVEEVENT:
                if event.state == 2:  # Minimized
                    pause_music()
                elif event.state == 1:  # Restored
                    unpause_music()

        # Отрисовка фона
        screen.fill(background)  # Задаем зеленый фон

        # Sort cards by z_index (ascending order)
        cards.sort(key=lambda card: card.z_index)

        # Отрисовка карточек
        for card in cards:
            # Movement to the center
            if card.moving_to_center:
                screen_center_x = screen.get_width() // 2
                screen_center_y = screen.get_height() // 2
                card.x += (screen_center_x - card.width // 2 - card.x) // 10  # Slower movement
                card.y += (screen_center_y - card.height // 2 - card.y) // 10  # Slower movement
                card.update_rect()  # Update the rectangle
                if abs(card.x - (screen_center_x - card.width // 2)) < 5 and abs(
                        card.y - (screen_center_y - card.height // 2)) < 5:
                    card.moving_to_center = False  # Stop moving
                    card.growing = True  # Start growing

            # Animation for growing
            if card.growing:
                if card.width < card.original_width * 2:  # Limit the max size
                    card.width += 2  # Slower growth
                    card.height += 2  # Slower growth
                    card.update_rect()  # Update the rectangle
                else:
                    card.growing = False  # Stop growing
                    card.center_time = time.time()  # Record the time when the card reached its maximum size

            # Stay in the center for 2 seconds
            if card.center_time and time.time() - card.center_time > 2:
                card.growing = False
                card.shrinking = True  # Start shrinking

            # Animation for shrinking back
            if card.shrinking and card.width > card.original_width:
                card.width -= 2  # Slower shrinking
                card.height -= 2  # Slower shrinking
                card.update_rect()  # Update the rectangle
                if card.width == card.original_width:
                    card.width = card.original_width
                    card.height = card.original_height
                    card.update_rect()  # Update the rectangle
                    card.shrinking = False  # Stop shrinking
                    card.moving_back = True  # Start moving back

            # Move back to original position
            if card.moving_back:
                card.x += (card.original_x - card.x) // 10  # Slower movement
                card.y += (card.original_y - card.y) // 10  # Slower movement
                card.update_rect()
                if abs(card.x - card.original_x) < 5 and abs(card.y - card.original_y) < 5:
                    card.x = card.original_x  # Reset x
                    card.y = card.original_y  # Reset y
                    card.update_rect()
                    card.moving_back = False  # Stop moving back
                    card.z_index = 0  # Reset z_index

            card.draw(screen)

        # Draw the back button
        back_button = pygame.Rect(10, 10, 150, 50)
        pygame.draw.rect(screen, white, back_button)
        back_text = font.render("Назад", True, black)
        text_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, text_rect)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second
