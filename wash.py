import time
import pygame

from cards import Card
from main_menu import screen, background

buttons_color = (255, 251, 213)
black = (0, 0, 0)

# Image loading
baby_image = pygame.image.load("assets/images/people/baby.png").convert_alpha()
father_image = pygame.image.load("assets/images/people/father.jpg").convert_alpha()
mother_image = pygame.image.load("assets/images/people/mother.jpg").convert_alpha()
grandfather_image = pygame.image.load("assets/images/people/grandfather.png").convert_alpha()
grandmother_image = pygame.image.load("assets/images/people/grandmother.jpg").convert_alpha()
aunt_image = pygame.image.load("assets/images/people/aunt.png").convert_alpha()
uncle_image = pygame.image.load("assets/images/people/uncle.png").convert_alpha()
masha_image = pygame.image.load("assets/images/people/masha.jpg").convert_alpha()
misha_image = pygame.image.load("assets/images/people/misha.jpg").convert_alpha()

# Resize element images to 200x200
element_image_1 = pygame.transform.scale(pygame.image.load("assets/images/wash/element1.jpg").convert_alpha(), (200, 200))
element_image_2 = pygame.transform.scale(pygame.image.load("assets/images/wash/element2.png").convert_alpha(), (200, 200))
element_image_3 = pygame.transform.scale(pygame.image.load("assets/images/wash/element3.jpg").convert_alpha(), (200, 200))
element_image_4 = pygame.transform.scale(pygame.image.load("assets/images/wash/element4.png").convert_alpha(), (200, 200))
element_image_5 = pygame.transform.scale(pygame.image.load("assets/images/wash/element5.jpg").convert_alpha(), (200, 200))
element_image_6 = pygame.transform.scale(pygame.image.load("assets/images/wash/element6.png").convert_alpha(), (200, 200))
element_image_7 = pygame.transform.scale(pygame.image.load("assets/images/wash/element7.jpg").convert_alpha(), (200, 200))
element_image_8 = pygame.transform.scale(pygame.image.load("assets/images/wash/element8.png").convert_alpha(), (200, 200))
element_image_9 = pygame.transform.scale(pygame.image.load("assets/images/wash/element9.jpg").convert_alpha(), (200, 200))
element_image_10 = pygame.transform.scale(pygame.image.load("assets/images/wash/element10.png").convert_alpha(), (200, 200))
element_image_11 = pygame.transform.scale(pygame.image.load("assets/images/wash/element11.jpg").convert_alpha(), (200, 200))
element_image_12 = pygame.transform.scale(pygame.image.load("assets/images/wash/element12.png").convert_alpha(), (200, 200))
element_image_13 = pygame.transform.scale(pygame.image.load("assets/images/wash/element13.jpg").convert_alpha(), (200, 200))
element_image_14 = pygame.transform.scale(pygame.image.load("assets/images/wash/element14.png").convert_alpha(), (200, 200))
element_image_15 = pygame.transform.scale(pygame.image.load("assets/images/wash/element15.jpg").convert_alpha(), (200, 200))
element_image_16 = pygame.transform.scale(pygame.image.load("assets/images/wash/element16.jpg").convert_alpha(), (200, 200))
element_image_17 = pygame.transform.scale(pygame.image.load("assets/images/wash/element 17.jpg").convert_alpha(), (200, 200))
element_image_18 = pygame.transform.scale(pygame.image.load("assets/images/wash/element18.jpg").convert_alpha(), (200, 200))
element_image_19 = pygame.transform.scale(pygame.image.load("assets/images/wash/element19.jpg").convert_alpha(), (200, 200))
element_image_20 = pygame.transform.scale(pygame.image.load("assets/images/wash/element20.png").convert_alpha(), (200, 200))

action_image = pygame.image.load("assets/images/wash/wash.png").convert_alpha()
action_image = pygame.transform.scale(action_image, (75, 75))  # Scale the action image

back_card_family = pygame.image.load("assets/images/wash/card_back1.png").convert_alpha()
back_card_element = pygame.image.load("assets/images/wash/card_back0.png").convert_alpha()

# Sound loading
element_sound = pygame.mixer.Sound("assets/sounds/food_sound.mp3")
family_sound = pygame.mixer.Sound("assets/sounds/family.mp3")

font = pygame.font.Font(None, 36)

# Card dimensions
card_width = 100
card_height = 150

# Spacing between elements
family_spacing = 50
element_spacing = 100
row_spacing = 50

family_row_y = 100

# Family member cards
family_member_cards = [
    Card(back_card_family, family_sound, None, 180, family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + card_width + family_spacing, family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 2 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 3 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 4 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 5 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 6 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 7 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
    Card(back_card_family, family_sound, None, 180 + 8 * (card_width + family_spacing), family_row_y, card_width, card_height, font, black),
]

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
]
for i, card in enumerate(family_member_cards):
    card.image = family_member_images[i]

elements_cards = []
element_images = [
    element_image_1,
    element_image_2,
    element_image_3,
    element_image_4,
    element_image_5,
    element_image_6,
    element_image_7,
    element_image_8,
    element_image_9,
    element_image_10,
    element_image_11,
    element_image_12,
    element_image_13,
    element_image_14,
    element_image_15,
    element_image_16,
    element_image_17,
    element_image_18,
    element_image_19,
    element_image_20,
]

elements_columns = 10 # Adjusted elements_columns to fit the new card size
elements_cards = []
for i in range(len(element_images)):
    card_x = 100 + (i % elements_columns * (card_width + element_spacing))
    card_y = family_row_y + card_height + family_spacing + row_spacing + 150 + (
            i // elements_columns * (card_height + row_spacing)) # Added 150 pixels down
    elements_cards.append(Card(back_card_element, element_sound, "", card_x, card_y, card_width, card_height, font, black))

# Game loop
clock = pygame.time.Clock()
flip_duration = 1.8


def run(running, pause_music, unpause_music):
    back_button = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    # Check for clicks on element cards
                    for i, card in enumerate(elements_cards):
                        if card.is_clicked(mouse_pos):
                            card.sound.play()
                            card.is_flipped = not card.is_flipped
                            card.flip_time = time.time()

                    # Check for clicks on family cards
                    for i, card in enumerate(family_member_cards):
                        if card.is_clicked(mouse_pos):
                            card.sound.play()
                            card.is_flipped = not card.is_flipped
                            card.flip_time = time.time()

                            # Flip other family cards back if any are flipped
                            for other_card in family_member_cards:
                                if other_card != card and other_card.is_flipped:
                                    other_card.is_flipped = False

                    # Check for clicks on back button
                    if back_button and back_button.collidepoint(mouse_pos):
                        running = False

            elif event.type == pygame.ACTIVEEVENT:
                if event.state == 2:  # Window loses focus
                    pause_music()
                elif event.state == 1:  # Window gains focus
                    unpause_music()

        screen.blit(background, (0, 0))

        # Draw family cards
        for card in family_member_cards:
            if card.is_flipped:
                flip_progress = min((time.time() - card.flip_time) / flip_duration, 1)
                rotation_angle = flip_progress * 360
                rotated_image = pygame.transform.rotate(card.image, rotation_angle)
                card_rect = rotated_image.get_rect(center=card.rect.center)
                screen.blit(rotated_image, card_rect)
            else:
                card.image = back_card_family
                card.draw(screen)

        # Draw action image between family and element cards
        action_rect = action_image.get_rect(center=(screen.get_width() // 2,
                                                    family_member_cards[0].rect.bottom + (row_spacing // 2) + 100))  # Adjusted y coordinate for centering
        screen.blit(action_image, action_rect)

        # Draw element cards
        for card in elements_cards:
            if card.is_flipped:
                flip_progress = min((time.time() - card.flip_time) / flip_duration, 1)
                rotation_angle = flip_progress * 360
                rotated_image = pygame.transform.rotate(card.image, rotation_angle)
                card_rect = rotated_image.get_rect(center=card.rect.center)
                screen.blit(rotated_image, card_rect)
            else:
                card.image = back_card_element
                card.draw(screen)

        # Back button
        back_button = pygame.Rect(10, 10, 150, 50)
        pygame.draw.rect(screen, buttons_color, back_button)
        back_text = font.render("Назад", True, black)
        text_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, text_rect)

        # Update card images after flipping
        for card in family_member_cards:
            if card.is_flipped and (time.time() - card.flip_time) >= flip_duration:
                card.image = family_member_images[family_member_cards.index(card)]

        for card in elements_cards:
            if card.is_flipped and (time.time() - card.flip_time) >= flip_duration:
                card.image = element_images[elements_cards.index(card)]

        pygame.display.flip()
        clock.tick(60)