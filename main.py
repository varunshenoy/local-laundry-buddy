from llama_cpp import Llama
import json
from colorama import init, Fore

init(autoreset=True)


class LaundryBuddy:
    # Drop in your favorite .gguf models to see how they perform!
    def __init__(self, model_path="./rocket-3b.Q4_K_S.gguf"):
        self.llm = Llama(model_path=model_path, chat_format="chatml", verbose=False)
        self.messages = [
            {
                "role": "system",
                "content": "You are a chatbot named Laundry Buddy that helps people answer questions about laundry. Give short, succinct responses.",
            }
        ]

    def respond(self, user_message_content):
        print(Fore.GREEN + "Laundry Buddy: ", end="")
        self.messages.append({"role": "user", "content": user_message_content})
        stream = self.llm.create_chat_completion(
            messages=self.messages,
            stream=True,
            max_tokens=250,
        )
        content = ""
        for output in stream:
            chunk = output["choices"][0]["delta"]
            if "content" in chunk:
                content += chunk["content"]
                print(chunk["content"], end="")
        print("")
        self.messages.append({"role": "assistant", "content": content})


if __name__ == "__main__":
    import os

    os.system("cls" if os.name == "nt" else "clear")
    print(
        "Welcome to Laundry Buddy! Ask me questions about laundry. Type 'quit' to exit.\n"
    )
    buddy = LaundryBuddy()
    while True:
        user_input = input(Fore.BLUE + "You: ")
        if user_input.lower() == "quit":
            break
        buddy.respond(user_input)
