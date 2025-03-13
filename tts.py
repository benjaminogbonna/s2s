import torch
from transformers import
from TTS.api import TTS
from helper_functions import string_gen

def text_to_speech(text, output_path):
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path


file_name = f'{string_gen()}.wav'
text_to_speech("Hello, this is a test!", output_path=file_name)
