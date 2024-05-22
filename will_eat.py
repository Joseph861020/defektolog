import time
import pygame

from cards import Card
from main_menu import screen, background

# Цвета
buttons_color = (255, 251, 213)
black = (0, 0, 0)

# Загрузка изображений семей
baby_image = pygame.image.load("assets/images/people/baby.jpg").convert_alpha()
father_image = pygame.image.load("assets/images/will_eat/father.png").convert_alpha()
mother_image = pygame.image.load("assets/images/people/mother.png").convert_alpha()
grandfather_image = pygame.image.load("assets/images/people/grandfather.png").convert_alpha()
grandmother_image = pygame.image.load("assets/images/people/grandmother.jpg").convert_alpha()
aunt_image = pygame.image.load("assets/images/people/aunt.png").convert_alpha()
uncle_image = pygame.image.load("assets/images/people/uncle.png").convert_alpha()
masha_image = pygame.image.load("assets/images/people/masha.jpg").convert_alpha()
misha_image = pygame.image.load("assets/images/people/misha.jpg").convert_alpha()
kisa_image = pygame.image.load("assets/images/people/kisa.jpg").convert_alpha()

back_card_family = pygame.image.load("assets/images/people/back_card1.jpg").convert_alpha()

# Загрузка изображений еды
food_image_1 = pygame.image.load("assets/images/will_eat/food1.jpg").convert_alpha()
food_image_2 = pygame.image.load("assets/images/will_eat/food2.jpg").convert_alpha()
food_image_3 = pygame.image.load("assets/images/will_eat/food3.jpg").convert_alpha()
food_image_4 = pygame.image.load("assets/images/will_eat/food4.png").convert_alpha()
food_image_5 = pygame.image.load("assets/images/will_eat/food5.jpg").convert_alpha()
food_image_6 = pygame.image.load("assets/images/will_eat/food6.png").convert_alpha()
food_image_7 = pygame.image.load("assets/images/will_eat/food7.jpg").convert_alpha()
food_image_8 = pygame.image.load("assets/images/will_eat/food8.jpg").convert_alpha()
food_image_9 = pygame.image.load("assets/images/will_eat/food9.jpg").convert_alpha()
food_image_10 = pygame.image.load("assets/images/will_eat/food10.png").convert_alpha()
food_image_11 = pygame.image.load("assets/images/will_eat/food11.jpg").convert_alpha()
food_image_12 = pygame.image.load("assets/images/will_eat/food12.jpg").convert_alpha()
food_image_13 = pygame.image.load("assets/images/will_eat/drink1.jpg").convert_alpha()
food_image_14 = pygame.image.load("assets/images/will_eat/drink2.jpg").convert_alpha()
food_image_15 = pygame.image.load("assets/images/will_eat/drink3.jpg").convert_alpha()
food_image_16 = pygame.image.load("assets/images/will_eat/drink4.jpg").convert_alpha()
back_card_food = pygame.image.load("assets/images/people/back_card0.jpg").convert_alpha()

# Загрузка звуковых эффектов
food_sound = pygame.mixer.Sound("assets/sounds/food_sound.mp3")
family_sound = pygame.mixer.Sound("assets/sounds/family.mp3")

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Создание экземпляров карточек
card_width = 100
card_height = 150
family_spacing = 30
family_row_y = 100
food_spacing = 100  # Reduced spacing for food cards
row_spacing = 50
# Create family member cards
family_member_cards = [
    Card(back_card_family, family_sound, None, 200, family_row_y, font, black),  # Baby card
    Card(back_card_family, family_sound, None, 200 + card_width + family_spacing, family_row_y, font, black),  # Father
    Card(back_card_family, family_sound, None, 200 + 2 * (card_width + family_spacing), family_row_y, font, black),  # Mother
    Card(back_card_family, family_sound, None, 200 + 3 * (card_width + family_spacing), family_row_y, font, black),  # Grandfather
    Card(back_card_family, family_sound, None, 200 + 4 * (card_width + family_spacing), family_row_y, font, black),  # Grandmother
    Card(back_card_family, family_sound, None, 200 + 5 * (card_width + family_spacing), family_row_y, font, black),  # Aunt
    Card(back_card_family, family_sound, None, 200 + 6 * (card_width + family_spacing), family_row_y, font, black),  # Uncle
    Card(back_card_family, family_sound, None, 200 + 7 * (card_width + family_spacing), family_row_y, font, black),  # Masha
    Card(back_card_family, family_sound, None, 200 + 8 * (card_width + family_spacing), family_row_y, font, black),  # Misha
    Card(back_card_family, family_sound, None, 200 + 9 * (card_width + family_spacing), family_row_y, font, black),  # Kisa
]

# Assign the corresponding images to the cards
family_member_images = [
    baby_image,
    father_image,
    mother_image,
    grandfather_image,
    grandmother_image,
    aunt_image,
    uncle_image,
    masha_image,
    misha_image,
    kisa_image
]
for i, card in enumerate(family_member_cards):
    card.image = family_member_images[i]

# Create food cards
food_cards = []
food_images = [
    food_image_1,
    food_image_2,
    food_image_3,
    food_image_4,
    food_image_5,
    food_image_6,
    food_image_7,
    food_image_8,
    food_image_9,
    food_image_10,
    food_image_11,
    food_image_12,
    food_image_13,
    food_image_14,
    food_image_15,
    food_image_16,

]
food_columns = 6  # Number of columns for food cards
for i in range(len(food_images)):
    card_x = 200 + (i % food_columns * (card_width + food_spacing))  # Arrange cards in 4 columns with spacing
    card_y = family_row_y + card_height + family_spacing + (
            i // food_columns * (card_height + row_spacing))  # Arrange cards in 2 rows with spacing
    food_cards.append(Card(back_card_food, food_sound, "", card_x, card_y, font, black))  # Start with the back card

# Игровой цикл
clock = pygame.time.Clock()  # For animation
flip_duration = 1.8  # Duration of the flip animation in seconds


def run(running, pause_music, unpause_music):  # Accept running as an argument
    back_button = None
    # play_background_music() # This is now in game_utils
    while running:  # Use the passed running variable
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the game loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if food cards clicked
                    for i, card in enumerate(food_cards):
                        if card.is_clicked(mouse_pos):
                            card.sound.play()
                            # Start the flip animation
                            card.is_flipped = not card.is_flipped
                            card.flip_time = time.time()

                    # Check if family member cards clicked
                    for i, card in enumerate(family_member_cards):
                        if card.is_clicked(mouse_pos):
                            card.sound.play()
                            # Start the flip animation
                            card.is_flipped = not card.is_flipped
                            card.flip_time = time.time()
                            # Turn back the previous flipped card
                            for other_card in family_member_cards:
                                if other_card != card and other_card.is_flipped:
                                    other_card.is_flipped = False

                    if back_button and back_button.collidepoint(mouse_pos):
                        running = False  # Exit the game loop
            # Handle window focus change
            elif event.type == pygame.ACTIVEEVENT:
                if event.state == 2:  # Minimized
                    pause_music()
                elif event.state == 1:  # Restored
                    unpause_music()

        # Отрисовка фона
        screen.blit(background, (0, 0))

        # Draw the family member cards with flip animation
        for card in family_member_cards:
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
                card.image = back_card_family
                card.draw(screen)

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
                card.image = back_card_food
                card.draw(screen)

        # Draw the back button
        back_button = pygame.Rect(10, 10, 150, 50)
        pygame.draw.rect(screen, buttons_color, back_button)
        back_text = font.render("Назад", True, black)
        text_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, text_rect)

        # Check for flip completion
        for card in family_member_cards:
            if card.is_flipped and (time.time() - card.flip_time) >= flip_duration:
                # Update card.image to the corresponding food image after the animation
                card.image = family_member_images[family_member_cards.index(card)]

        # Check for flip completion for food cards
        for card in food_cards:
            if card.is_flipped and (time.time() - card.flip_time) >= flip_duration:
                # Update card.image to the corresponding food image after the animation
                card.image = food_images[food_cards.index(card)]

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second