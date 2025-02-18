import simpleaudio
import keyboard
import time
import sys

def play_while_pressed():
    
    # Get the wav file path from command line arguments
    wav_file = "/Users/ryem/Desktop/Cornell_Tech/EchoRide_explore/sound_effect/Beep_Sound_Effect.wav"
    
    try:
        # Load the wav file
        wave_obj = simpleaudio.WaveObject.from_wave_file(wav_file)
        print(f"Loaded: {wav_file}")
        print("Press and hold shift to play. Press Ctrl+C to exit.")

        play_obj = None
        was_playing = False
        play_obj = wave_obj.play()
        print("mark2")
        time.sleep(1000)
        print("mark3")

        # while True:
        #     if keyboard.is_pressed('shift'):
        #         # Start playing if not already playing
        #         if not was_playing:
        #             if play_obj is not None:
        #                 play_obj.stop()
        #             play_obj = wave_obj.play()
        #             was_playing = True
        #     else:
        #         # Stop playing if it was playing
        #         if was_playing:
        #             if play_obj is not None:
        #                 play_obj.stop()
        #             was_playing = False

        #     time.sleep(0.1)  # Small delay to prevent high CPU usage

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        if play_obj is not None:
            play_obj.stop()
        print("\nExiting...")
        sys.exit(0)

    except FileNotFoundError:
        print(f"Error: File '{wav_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        play_while_pressed()
        print("mark1")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)
