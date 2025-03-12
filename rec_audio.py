import sounddevice as sd
import numpy as np
import wavio


# Record user audio
def record_audio(filename, duration=5, samplerate=44100):
    print("Recording... Speak now!")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    wavio.write(filename, audio, samplerate, sampwidth=2)
    print("Recording saved!")
    # return audio
