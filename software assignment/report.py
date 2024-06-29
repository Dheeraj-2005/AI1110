import pygame
import random
import os
import time

# Initialize pygame.mixer
pygame.mixer.init()

# Function to play audio
def play_audio(audio_file_path):
    pygame.mixer.music.load(audio_file_path)
    print(f"Now playing: {os.path.basename(audio_file_path)}")
    pygame.mixer.music.play()

# Function to pause audio
def pause_audio():
    pygame.mixer.music.pause()
    print("Audio paused.")

# Replace with the directory path containing your audio files
directory_path = "/home/dheeraj/Music"

# Find all audio files in the directory
audio_files = [file for file in os.listdir(directory_path) if file.endswith(".mp3")]

# Shuffle the audio files randomly
random.shuffle(audio_files)

# Flag to track if audio is currently playing
playing = False

# Index to track current audio file in shuffled list
current_index = 0

# Main loop to control playback
while current_index < len(audio_files):
    if not playing:
        # Start playing audio if not already playing
        audio_file_path = os.path.join(directory_path, audio_files[current_index])
        play_audio(audio_file_path)
        playing = True
        #pause=False
    
    # Check for user input
    action = input("Enter action (pause/stop/next): ").strip().lower()
    
    if action == "pause":
        if playing:
            pause_audio()
        else:
            print("No audio playing.")

    elif action == "stop":
        print("Stopping playback.")
        break  # Exit the loop and end playback

    elif action == "next":
        if playing:
            pygame.mixer.music.stop()
            playing = False
        
        current_index = (current_index + 1) % len(audio_files)  # Move to next track
        audio_file_path = os.path.join(directory_path, audio_files[current_index])
        play_audio(audio_file_path)
        playing = True

    else:
        print("Invalid action. Please enter 'pause', 'stop', or 'next'.")

# Quit pygame.mixer
pygame.mixer.quit()

