import time
import pygame

from cards import Card
from main_menu import screen, black, font


background = pygame.image.load('assets/images/background.jpg')
# Цвета
buttons_color = (255, 251, 213)


# Загрузка изображений семей
baby_image = pygame.image.load("assets/images/people/baby.png").convert_alpha()
father_image = pygame.image.load("assets/images/people/father.jpg").convert_alpha()
mother_image = pygame.image.load("assets/images/people/mother.jpg").convert_alpha()
grandfather_image = pygame.image.load("assets/images/people/grandfather.png").convert_alpha()
grandmother_image = pygame.image.load("assets/images/people/grandmother.jpg").convert_alpha()
aunt_image = pygame.image.load("assets/images/people/aunt.png").convert_alpha()
uncle_image = pygame.image.load("assets/images/people/uncle.png").convert_alpha()
masha_image = pygame.image.load("assets/images/people/masha.jpg").convert_alpha()
misha_image = pygame.image.load("assets/images/people/misha.jpg").convert_alpha()
kisa_image = pygame.image.load("assets/images/people/kisa.jpg").convert_alpha()

back_card_family = pygame.image.load("assets/images/i_do/card_back0.png").convert_alpha()
back_card_action = pygame.image.load("assets/images/i_do/card_back1.png").convert_alpha()  # Back card for actions

# Загрузка изображений действие
image1 = pygame.image.load("assets/images/i_do/cary.png").convert_alpha()
image2 = pygame.image.load("assets/images/i_do/eat.png").convert_alpha()
image3 = pygame.image.load("assets/images/i_do/run.png").convert_alpha()
image4 = pygame.image.load("assets/images/i_do/sing.png").convert_alpha()
image5 = pygame.image.load("assets/images/i_do/sit.png").convert_alpha()
image6 = pygame.image.load("assets/images/i_do/sleep.png").convert_alpha()
image7 = pygame.image.load("assets/images/i_do/stand.png").convert_alpha()
image8 = pygame.image.load("assets/images/i_do/walk.png").convert_alpha()
image9 = pygame.image.load("assets/images/i_do/wash.png").convert_alpha()
image10 = pygame.image.load("assets/images/i_do/drink.png").convert_alpha()

# Загрузка звуковых эффектов
sound1 = pygame.mixer.Sound("assets/sounds/up.mp3")

images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10]


# Создание экземпляров карточек
card_width = 100
card_height = 150
family_spacing = 30
family_row_y = 100
action_row_y = family_row_y + card_height + family_spacing + 50  # Move action cards down by 50 pixels
action_spacing = 50  # Space between action cards
action_columns = 5  # Number of columns for action cards
family_sound = pygame.mixer.Sound("assets/sounds/family.mp3")
# Family member cards
family_member_cards = [
    Card(back_card_family, family_sound, None, 180, family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + card_width + family_spacing, family_row_y, card_width, card_height,
         font, black),
    Card(back_card_family, family_sound, None, 180 + 2 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 3 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 4 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 5 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 6 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 7 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 8 * (card_width + family_spacing), family_row_y, card_width,
         card_height, font, black),
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

# Action cards
action_cards = [
    Card(back_card_action, sound1, "", 100 + (i % action_columns) * (250 + action_spacing),
         action_row_y + (i // action_columns) * (250 + action_spacing), 250, 250, font, black)  # Pass font and color
    for i in range(len(images))
]

# Assign the corresponding images to the cards
for i, card in enumerate(action_cards):
    card.image = images[i]  # Set the front image initially
    card.width = 250  # Set the width of the action cards
    card.height = 250  # Set the height of the action cards
    card.original_width = card.width  # Store original width for scaling
    card.original_height = card.height  # Store original height for scaling
    card.original_x = card.x  # Store original x position for moving
    card.original_y = card.y  # Store original y position for moving

# Игровой цикл
clock = pygame.time.Clock()  # For animation
flip_duration = 1.8  # Duration of the flip animation in seconds
center_duration = 3  # Duration to stay in the center


def run(running, pause_music, unpause_music):  # Accept running as an argument
    back_button = None
    # play_background_music() # This is now in game_utils
    while running:  # Use the passed running variable
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    mouse_pos = pygame.mouse.get_pos()
                    for card in family_member_cards + action_cards:
                        if card.is_clicked(mouse_pos):
                            card.sound.play()
                            card.is_flipped = not card.is_flipped
                            card.flip_time = time.time()

                            # Turn back the previous flipped card in the same category
                            if card in family_member_cards:
                                for other_card in family_member_cards:
                                    if other_card != card and other_card.is_flipped:
                                        other_card.is_flipped = False
                            else:
                                for other_card in action_cards:
                                    if other_card != card and other_card.is_flipped:
                                        other_card.is_flipped = False

                            # Move action card to center and grow
                            if card in action_cards:
                                card.moving_to_center = True
                                card.growing = True
                                card.center_time = time.time()

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

        # Sort cards by z_index (ascending order)
        cards = family_member_cards + action_cards
        cards.sort(key=lambda card: card.z_index)

        # Отрисовка карточек
        for card in cards:
            # Draw the family member cards with flip animation
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
                if card in family_member_cards:
                    card.image = back_card_family
                else:
                    card.image = back_card_action
                card.draw(screen)

            # Handle action card movement and growth
            if card in action_cards:
                if card.moving_to_center:
                    screen_center_x = screen.get_width() // 2
                    screen_center_y = screen.get_height() // 2  # Get the screen center y

                    card.x += (screen_center_x - card.width // 2 - card.x) // 10
                    card.y += (screen_center_y - card.height // 2 - card.y) // 10  # Move card vertically to center
                    card.update_rect()  # Update the rectangle

                    # Check if card is within 5 pixels of the center in both X and Y
                    if abs(card.x - (screen_center_x - card.width // 2)) < 5 and abs(
                            card.y - (screen_center_y - card.height // 2)) < 5:
                        card.moving_to_center = False  # Stop moving
                        card.growing = True  # Start growing
                if card.growing:
                    if card.width < card.original_width * 2:  # Limit the max size
                        card.width += 2  # Slower growth
                        card.height += 2  # Slower growth
                        card.update_rect()  # Update the rectangle
                    else:
                        card.growing = False  # Stop growing
                        card.center_time = time.time()  # Record the time when the card reached its maximum size
                        card.z_index = 100  # Bring to front

                # Stay in the center for 3 seconds
                if card.center_time and time.time() - card.center_time > center_duration:
                    card.shrinking = True  # Start shrinking
                    card.z_index = 0  # Send to back

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
                if card.moving_back:
                    card.x += (card.original_x - card.x) // 10
                    card.y += (card.original_y - card.y) // 10
                    card.update_rect()
                    if abs(card.x - card.original_x) < 5 and abs(card.y - card.original_y) < 5:
                        card.x = card.original_x  # Reset x
                        card.y = card.original_y  # Reset y
                        card.update_rect()
                        card.moving_back = False  # Stop moving back

        # Draw the back button
        back_button = pygame.Rect(10, 10, 150, 50)
        pygame.draw.rect(screen, buttons_color, back_button)
        back_text = font.render("Назад", True, black)
        text_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, text_rect)

        # Check for flip completion
        for card in family_member_cards + action_cards:
            if card.is_flipped and (time.time() - card.flip_time) >= flip_duration:
                # Update card.image to the corresponding food image after the animation
                if card in family_member_cards:
                    card.image = family_member_images[family_member_cards.index(card)]
                else:
                    card.image = images[action_cards.index(card)]

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second