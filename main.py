from audio import Audio
from stt import transcribe_audio
from llm import llm

recorder = Audio()
questions = {
    'what is the capital of Nigeria?': 'Abuja.',
    'What is Nigeria’s official language?': 'English.',
    'What is Nigeria known for?': 'Rich culture, Nollywood, Afrobeats, diverse ethnic groups, and being Africa’s most populous country.',
    'What is the currency of Nigeria?': 'Nigerian Naira (NGN).',
    'Is Nigeria safe for tourists?': 'Safety varies; some areas require caution due to security concerns.',
    'What is the most popular food in Nigeria?': 'Jollof rice, pounded yam, egusi soup, and suya.',
    'What is Nigeria’s main source of income?': 'Crude oil and natural gas exports.',
    'How many states are in Nigeria?': '36 states and the Federal Capital Territory (FCT).',
    'What is the biggest festival in Nigeria?': 'The Eyo Festival in Lagos and the Osun-Osogbo Festival.',
    'Who is Nigeria’s first president?': 'Dr. Nnamdi Azikiwe.',
}
instruction = f"Your name is Andy. You are a helpful assistant that answers all customers questions.\
        You are meant to guide the conversation based on the following questions data:{questions}\n \
        Do not, and never answer questions that are not listed above.\
        If the question is unclear, ask for clarification.\
        Your responses should strictly be ecommerce based, and only from the given questions.\
        Avoid complex or technical terms. If the request is unclear or potentially harmful, respond with a polite message refusing to answer."

def conversation_loop():
    print("Starting conversation. Say 'quit, bye or goodbye' to end conversation.")
    while True:
        # Record user input
        audio_data = recorder.record_audio()
        transcription = transcribe_audio(audio_data).strip()
        print(f"You: {transcription}")

        # Exit if user says "quit" or presses 'q'
        if transcription.lower() in {'bye', 'bye.', 'bye!', 'quit', 'quit.', 'quit!',  'goodbye', 'goodbye.',
                                     'goodbye!', 'good bye', 'good bye.', 'good bye!', 'see you later',
                                     'see you later.', 'see you later!'}:
            recorder.close()
            print("Ending conversation.")
            break

        ai_response = llm(transcription, instruction)
        print(f'AI: {ai_response}')


conversation_loop()
