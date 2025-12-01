import os
from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv


def load_api_key():
    load_dotenv()
    api_key = os.getenv("PPLX_API_KEY")
    if api_key is None:
        raise ValueError("PPLX_API_KEY not found in environment variables.")
    return api_key


def set_api_key():
    api_key = load_api_key()
    try:
        os.environ["PPLX_API_KEY"] = api_key
    except ValueError as e:
        print(e)


def talk_to_perplexity():
    while True:
        user_input = input("Enter your message (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Exiting the chat.")
            break
        try:
            print("Processing response...")
            chat = ChatPerplexity(timeout=60,streaming=True)
            response = chat.invoke(user_input)
            print(response.content)
        except Exception as e:
            print("An error occurred:", e)