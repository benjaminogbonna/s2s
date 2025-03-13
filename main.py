from audio import Audio
from stt import transcribe_audio
from llm import llm


instruction = 'You are a helpful assistant.'

def conversation_loop():
    print("Starting conversation. Press 'q', quit, bye or good bye to quit.")
    while True:
        # Record user input
        recorder = Audio()
        audio_data = recorder.record_audio()
        if audio_data.dtype == 'float32':
            transcription = transcribe_audio(audio_data)
            print(f"You: {transcription}")

            # Exit if user says "quit" or presses 'q'
            if transcription.lower() in ["quit", "q", 'bye', 'good bye']:
                print("Ending conversation.")
                recorder.close()
                break
            ai_response = llm(transcription, instruction)
            print(f'AI: {ai_response}')
        else:
            print('An error occurred, please try again!')


conversation_loop()
