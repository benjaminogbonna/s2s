from transformers import pipeline, WhisperProcessor, WhisperForConditionalGeneration

def transcribe_audio(audio_data):
    asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")
    transcription = asr_pipeline(audio_data)
    return transcription['text']
