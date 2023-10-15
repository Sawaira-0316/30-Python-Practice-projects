import pygame
import tkinter as tk
from tkinter import filedialog


# Initialize pygame
pygame.init()

# Create the player window
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# Load the image
image = pygame.image.load(file="C:\Users\Rehan\Pictures.jpg")





# Load the music
music_file = filedialog.askopenfilename()
pygame.mixer.music.load(music_file)

# Initialize variables
is_playing = False
volume = 0.5

# Function to play the music
def play_music():
    pygame.mixer.music.play()
    global is_playing
    is_playing = True

# Function to pause or resume the music
def pause_resume_music():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
    else:
        pygame.mixer.music.unpause()
        is_playing = True

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    global is_playing
    is_playing = False

# Function to increase the volume
def increase_volume():
    global volume
    if volume < 1.0:
        volume += 0.1
    pygame.mixer.music.set_volume(volume)

# Function to decrease the volume
def decrease_volume():
    global volume
    if volume > 0.0:
        volume -= 0.1
    pygame.mixer.music.set_volume(volume)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((255, 255, 255))

    # Display the image
    window.blit(image, (50, 50))

    # Draw the buttons
    play_button = pygame.draw.rect(window, (0, 255, 0), (100, 200, 50, 30))
    stop_button = pygame.draw.rect(window, (255, 0, 0), (175, 200, 50, 30))
    forward_button = pygame.draw.rect(window, (0, 0, 255), (250, 200, 50, 30))
    backward_button = pygame.draw.rect(window, (255, 255, 0), (325, 200, 50, 30))
    volume_up_button = pygame.draw.rect(window, (0, 255, 255), (100, 250, 50, 30))
    volume_down_button = pygame.draw.rect(window, (255, 0, 255), (175, 250, 50, 30))

    # Check for button clicks
    mouse_pos = pygame.mouse.get_pos()
    if play_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            play_music()
    elif stop_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            stop_music()
    elif forward_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
    elif backward_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)
    elif volume_up_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            increase_volume()
    elif volume_down_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            decrease_volume()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
