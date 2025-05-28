# import required module
from playsound import playsound
import time

# for playing note.wav file
print('playing sound using  playsound')

# Path to the sound file
sound_file = '/Users/ryem/Desktop/Cornell_Tech/EchoRide_explore/sound_effect/Beep_Sound_Effect.wav'

# Number of times to play the sound
num_loops = 10
# i = 0

for _ in range(num_loops):
    playsound(sound_file)
    time.sleep(0.1)  # Pause between plays

while True:
            if keyboard.is_pressed('shift'):
                # Start playing if not already playing
                if not was_playing:
                    if play_obj is not None:
                        play_obj.stop()
                    play_obj = wave_obj.play()
                    was_playing = True
            else:
                # Stop playing if it was playing
                if was_playing:
                    if play_obj is not None:
                        play_obj.stop()
                    was_playing = False
            
            time.sleep(0.1)  # Small delay to prevent high CPU usage
            

