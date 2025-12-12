import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return api_key

def set_api_key():
    api_key = load_api_key()
    try:
        os.environ["OPENAI_API_KEY"] = api_key
    except ValueError as e:
        print(e)

def talk_to_openai(user_input: str):
    try:
        print("Processing response...")
        chat = ChatOpenAI(model="gpt-4o-mini", streaming=True)
        response = chat.invoke(user_input)
        return response.content
    except Exception as e:
        return f"An error occurred: {e}"