import pygame

pygame.mixer.init()

# Load background music
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
