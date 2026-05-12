import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai


sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = client.models.get(model = "gemini-3.1-flash-lite")
chat = client.chats.create(model=model.name)

def get_hint(words):
    prompt = """
    You are an expert assistant specialized in solving the word association game "Linxicon." Your goal is to help the player connect two "Target" words using semantic logic. You will be provided with game data extracted via a custom JavaScript interceptor.

    ### How to Understand the Data Format:
    The JSON data you receive follows this structure:
    1. "target": The two main words to be connected (Word A - Word B).
    2. "words" (Words List): An array of objects where:
    - "word": The word entered in the game.
    - "group": The semantic status based on the game's logic:
        - "Group A": Connected to the left starting word (Blue).
        - "Group B": Connected to the right starting word (Pink).
        - "Solved": A "Bridge" word that successfully links both sides.
        - "Deconected": No valid connection found yet.
    - "hexColor": The raw color value from the game UI.

    ### Your Strategy Task:
    1. Analyze the semantic gap between "Target A" and "Target B".
    2. Review the words currently in "Group A" and "Group B".
    3. Identify the "Meeting Point": Propose a new word that logically sits between the current active words of both groups.
    4. Filter Noise: Ignore words marked as "Deconected".

    ### Instructions for your Response:
    - Provide a single-word suggestion (HINT).
    - Briefly explain the semantic "bridge" (how it connects the left side to the right side).
    - Keep the tone helpful and concise.

    ### Current Game Data:
    """

    full_prompt = prompt + json.dumps(words, indent=4)


    response = chat.send_message(full_prompt)

    print("-" * 30)
    print(response.text)
    print("-" * 30)
