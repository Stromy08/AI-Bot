# code/main.py
from pathlib import Path
from openai import OpenAI
from ignore.config import OPENAI_API_KEY  # Adjust the import path

client = OpenAI(api_key=OPENAI_API_KEY)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="It was never meant to be..."
)

response.stream_to_file(speech_file_path)
