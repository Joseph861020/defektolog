import pygame

class Card:
    def __init__(self, image, sound, text, x, y, font, color):
        self.image = image
        self.sound = sound
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.color = color

        self.original_width = image.get_width()
        self.original_height = image.get_height()
        self.width = self.original_width
        self.height = self.original_height

        # Store original x and y positions
        self.original_x = x
        self.original_y = y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.growing = False
        self.moving_to_center = False
        self.z_index = 0
        self.center_time = None
        self.shrinking = False
        self.moving_back = False

        # Add the flipping attribute
        self.flipping = False
        self.flip_angle = 0
        self.flip_time = None

        self.target_image = None
        self.is_flipped = False  # Add a flag to check if the card is already flipped

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        # Scale the image based on current width and height
        scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(scaled_image, (self.x, self.y))

        # Draw the text on the card
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update_rect(self):
        # Update the rectangle to match the scaled image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)