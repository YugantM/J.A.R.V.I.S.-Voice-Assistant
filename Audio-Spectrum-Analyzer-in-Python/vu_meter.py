#!/usr/bin/python3
import pyaudio
from amplitude import Amplitude
from vu_constants import RATE, INPUT_FRAMES_PER_BLOCK




def audio_int():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                                channels=2,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=INPUT_FRAMES_PER_BLOCK
                                )
    maximal = Amplitude()
    data = stream.read(INPUT_FRAMES_PER_BLOCK)
    amp = Amplitude.from_data(data)
    if amp > maximal:
                maximal = amp
    # amp.display(scale=100, mark=maximal)
    return amp.display(scale=100, mark=maximal)

# print(type(audio_int()))
# while True:
#     audio_int()
            # data = stream.read(INPUT_FRAMES_PER_BLOCK)
            # amp = Amplitude.from_data(data)
            # if amp > maximal:
            #     maximal = amp
            # amp.display(scale=100, mark=maximal)

# if __name__ == "__main__":
#     main()
