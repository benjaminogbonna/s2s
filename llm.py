import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def llm(user_msg, instruction):
    client = genai.Client(api_key=GEMINI_API_KEY)
    chat = client.chats.create(model='gemini-1.5-flash',
                               config=types.GenerateContentConfig(system_instruction=instruction),
                               history=[]
                               )
    response = chat.send_message(user_msg)
    if response and response.text:
        return response.text
    return 'An error occurred, please try again!'
