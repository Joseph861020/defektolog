import pygame

class Card:
    def __init__(self, back_image, sound, text, x, y, width, height, font, color):
        self.back_image = back_image
        self.sound = sound
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font  # Store the font
        self.color = color  # Store the color
        # Initialize the rect using pygame.Rect
        self.rect = pygame.Rect(x, y, width, height)  # Correct initialization
        self.is_flipped = False
        self.flip_time = None
        self.image = self.back_image  # Start with the back image
        self.z_index = 0  # Initial z-index
        self.moving_to_center = False  # Flag for moving to center
        self.growing = False  # Flag for growing
        self.shrinking = False  # Flag for shrinking
        self.moving_back = False  # Flag for moving back
        self.center_time = None  # Time when card reached maximum size
        self.original_width = width
        self.original_height = height
        self.original_x = x
        self.original_y = y

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)