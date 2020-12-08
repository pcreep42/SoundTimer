import time

from playsound import playsound


class SoundTimer:
    def __init__(self):
        self.sound_file_path = 'bell.wav'

    def count_n_call(self, time_qty: int):
        for time_count in range(0, time_qty):  # loop which count time_qty seconds
            time.sleep(1)
            print(time_count)
        playsound(self.sound_file_path)  # playing the sound


