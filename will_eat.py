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
baby_image = pygame.image.load("assets/images/will_eat/baby.jpg").convert_alpha()
food_image_1 = pygame.image.load("assets/images/will_eat/food1.jpg").convert_alpha()
food_image_2 = pygame.image.load("assets/images/will_eat/food2.png").convert_alpha()
food_image_3 = pygame.image.load("assets/images/will_eat/food3.jpg").convert_alpha()
food_image_4 = pygame.image.load("assets/images/will_eat/food4.png").convert_alpha()
food_image_5 = pygame.image.load("assets/images/will_eat/food5.jpg").convert_alpha()
food_image_6 = pygame.image.load("assets/images/will_eat/food6.png").convert_alpha()
food_image_7 = pygame.image.load("assets/images/will_eat/food7.jpg").convert_alpha()
food_image_8 = pygame.image.load("assets/images/will_eat/food8.jpg").convert_alpha()
back_card_image = pygame.image.load("assets/images/will_eat/back_card.jpg").convert_alpha()  # Load the back card image

# Загрузка звуковых эффектов
food_sound = pygame.mixer.Sound("assets/sounds/food_sound.mp3")  # One sound for all foods

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Создание экземпляров карточек
card_width = 150
card_height = 200

# Position the baby card in the center
baby_card_x = screen.get_width() // 2 - card_width // 2
baby_card_y = screen.get_height() // 2 - card_height // 2 - 250  # Move baby card up by 20 pixels
baby_card = Card(baby_image, None, "", baby_card_x, baby_card_y, font, black)  # No sound for baby card
# Create food cards
food_cards = []
food_images = [food_image_1, food_image_2, food_image_3, food_image_4, food_image_5, food_image_6, food_image_7,
               food_image_8]

for i in range(len(food_images)):
    card_x = 100 + (i % 4 * (card_width + 100))  # Arrange cards in 4 columns
    card_y = 250 + (i // 4 * (card_height + 50))  # Arrange cards in rows
    food_cards.append(Card(back_card_image, food_sound, "", card_x, card_y, font, black))  # Start with the back card

# Игровой цикл
clock = pygame.time.Clock()  # For animation
flip_duration = 1.8  # Duration of the flip animation in seconds


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
                # Check if food cards clicked
                for i, card in enumerate(food_cards):
                    if card.is_clicked(mouse_pos):
                        card.sound.play()
                        # Start the flip animation
                        card.is_flipped = not card.is_flipped
                        card.flip_time = time.time()

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

        # Draw the baby card
        baby_card.draw(screen)

        # Draw the food cards with flip animation
        for card in food_cards:
            if card.is_flipped:
                # Calculate the current flip progress (0-1)
                flip_progress = min((time.time() - card.flip_time) / flip_duration, 1)

                # Determine the rotation angle based on progress
                rotation_angle = flip_progress * 360  # 360 degrees for a full flip

                # Rotate the card image
                rotated_image = pygame.transform.rotate(card.image, rotation_angle)

                # Calculate the new position to keep the card centered
                card_rect = rotated_image.get_rect(center=card.rect.center)

                # Draw the rotated image at the adjusted position
                screen.blit(rotated_image, card_rect)

            else:
                # If not flipped, use the back card image
                card.image = back_card_image
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

        # Check for flip completion
        for card in food_cards:
            if card.is_flipped and (time.time() - card.flip_time) >= flip_duration:
                # Update card.image to the corresponding food image after the animation
                card.image = food_images[food_cards.index(card)]
