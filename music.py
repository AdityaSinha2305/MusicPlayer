import pygame
from tkinter import filedialog
from tkinter import *

# Initialize pygame
pygame.init()

# Create a Tkinter window (it will not be visible)
root = Tk()
root.withdraw()

# Function to open a file dialog and return the selected file path
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    return file_path

# Function to play the selected audio file
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to stop the music playback
def stop_music():
    pygame.mixer.music.stop()

# Function to pause the music playback
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music playback
def resume_music():
    pygame.mixer.music.unpause()

# Function to set the volume
def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Main function
def main():
    print("Select a music file.")
    file_path = choose_file()
    li = file_path.split('/')
    print("List: ",li)

    if not file_path:
        print("No file selected. Exiting.")
        return

    print(f"Playing: {li[-1]}")
    play_music(file_path)

    while True:
        print("\nMusic Player Menu:")
        print("1. Stop")
        print("2. Pause")
        print("3. Resume")
        print("4. Set Volume")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stop_music()
        elif choice == "2":
            pause_music()
        elif choice == "3":
            resume_music()
        elif choice == "4":
            volume = float(input("Enter volume (0.0 to 1.0): "))
            set_volume(volume)
        elif choice == "5":
            stop_music()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
