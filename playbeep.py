# play beep while you press shift ley

import keyboard
from pygame import mixer 
import time

def main():
    # Initialize pygame mixer for audio
    mixer.init()
    
    # Load the beep sound
    # try:
    mixer.music.load('/Users/ryem/Desktop/Cornell_Tech/EchoRide_explore/sound_effect/Beep_Sound_Effect.wav')
    # except pygame.error:
    #     print("Error: Could not load 'beep.wav'. Make sure the file exists in the same directory.")
    #     return
    # Setting the volume 
    mixer.music.set_volume(1) 
    
    print("Program started. Press Shift key to play beep sound. Press Esc to exit.")
    mixer.music.play()

    # Flag to track if sound is currently playing
    is_playing = False
    
    try:
        while True:
            # Check if shift is pressed
            print(".")
            if keyboard.is_pressed('shift'):
                if not is_playing:  # Only play if not already playing
                    mixer.music.play()
                    is_playing = True
            else:
                # Stop the sound when shift is released
                mixer.music.pause()
                is_playing = False
                
            # Check for escape key to exit
            if keyboard.is_pressed('esc'):
                print("Exiting program...")
                break
                
            # Small delay to prevent high CPU usage
            print(".")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        # Clean up pygame
        mixer.music.stop()

if __name__ == "__main__":
    main()