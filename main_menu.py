import pygame
import os
import game_utils

# Initialize Pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
# Screen dimensions
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width - 10, screen_height - 50), pygame.RESIZABLE)
pygame.display.set_caption("Дефектолог")
game_icon = pygame.image.load('assets/images/game_icon.png')
pygame.display.set_icon(game_icon)
background = pygame.image.load('assets/images/background.jpg')

# Colors
buttons_color = (255, 251, 213)
black = (0, 0, 0)

# Font for text
font = pygame.font.Font(None, 36)

# Define buttons globally
card_game_button = None
will_eat_button = None
other_game_button_2 = None


# Function to display the main menu
def display_main_menu():
    global card_game_button, will_eat_button, other_game_button_2  # Declare variables as global
    # Draw the background
    screen.blit(background, (0, 0))

    # Text for the menu
    menu_text = font.render("Выберите игру:", True, black)
    screen.blit(menu_text, (screen.get_width() // 2 - menu_text.get_width() // 2, 100))

    # "Card Game" button
    card_game_button = pygame.Rect(screen.get_width() // 2 - 150, 200, 300, 50)
    pygame.draw.rect(screen, buttons_color, card_game_button)  # Draw the white rectangle for the button
    card_game_text = font.render("Карточная игра", True, black)
    text_rect = card_game_text.get_rect(center=card_game_button.center)  # Get the center of the button
    screen.blit(card_game_text, text_rect)  # Blit the text at the center of the button

    # "Other Game 1" button
    will_eat_button = pygame.Rect(screen.get_width() // 2 - 150, 300, 300, 50)  # will_eat_button
    pygame.draw.rect(screen, buttons_color, will_eat_button)
    will_eat_text = font.render("Я буду", True, black)
    text_rect = will_eat_text.get_rect(center=will_eat_button.center)  # Get the center of the button
    screen.blit(will_eat_text, text_rect)  # Blit the text at the center of the button

    # "Other Game 2" button
    other_game_button_2 = pygame.Rect(screen.get_width() // 2 - 150, 400, 300, 50)
    pygame.draw.rect(screen, buttons_color, other_game_button_2)
    other_game_text_2 = font.render("Другая игра 2", True, black)
    text_rect = other_game_text_2.get_rect(center=other_game_button_2.center)  # Get the center of the button
    screen.blit(other_game_text_2, text_rect)  # Blit the text at the center of the button


# Main game function
def main():
    global card_game_button, will_eat_button, other_game_button_2
    running = True
    game_utils.play_background_music()
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if "Card Game" button is clicked
                    if card_game_button.collidepoint(mouse_pos):
                        # Start the card game from a separate file
                        import i_do  # Import the card_game.py file
                        i_do.run(running, game_utils.pause_background_music,
                                 game_utils.unpause_background_music)  # Call the run() function from card_game.py
                    # Check if "Other Game 1" button is clicked
                    elif will_eat_button.collidepoint(mouse_pos):
                        # Start "Other Game 1" from a separate file
                        import will_eat  # Import the other_game_1.py file
                        will_eat.run(running, game_utils.pause_background_music,
                                     game_utils.unpause_background_music)  # Call the run() function from other_game_1.py
                    # Check if "Other Game 2" button is clicked
                    elif other_game_button_2.collidepoint(mouse_pos):
                        # Start "Other Game 2" from a separate file
                        import other_game_2  # Import the other_game_2.py file
                        other_game_2.run(running, game_utils.pause_background_music,
                                         game_utils.unpause_background_music)
            elif event.type == pygame.ACTIVEEVENT:
                if event.state == 2:  # Minimized
                    game_utils.pause_background_music()
                elif event.state == 1:  # Restored
                    game_utils.unpause_background_music()
        # Draw the main menu
        display_main_menu()
        pygame.display.flip()  # Call flip outside of display_main_menu()


# Start the game
if __name__ == "__main__":
    main()
