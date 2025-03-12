import torch
import whisper
from rec_audio import record_audio
import secrets
import string

# Generate random strings
def string_gen(x=15):
    key = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for i in range(x))
    return key


# Load Whisper model
model = whisper.load_model("medium")  # Options: tiny, base, small, medium, large

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]


file_name = f'{string_gen()}.wav'
record_audio(filename=file_name)


text = transcribe_audio(file_name)
print("Transcribed Text:", text)
