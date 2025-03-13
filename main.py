from audio import Audio
from stt import transcribe_audio
from llm import llm

recorder = Audio()
audio_data = recorder.record_audio()

instruction = 'You are a helpful assistant.'

if audio_data.dtype == 'float32':
    transcription = transcribe_audio(audio_data)
    response = llm(transcription, instruction)
    print(response)
else:
    print('An error occurred, please try again!')

recorder.close()
