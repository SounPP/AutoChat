import time
import subprocess

def send_message(message):
    subprocess.run(["xdotool", "type", message])
    subprocess.run(["xdotool", "key", "Return"])

def main():
    time.sleep(10)  # Adjust the delay based on the responsiveness of your CLI
    messages = [
        "Hello, how are you?",
        "What's going on?",
        "I'm a simple auto chatbot.",
        "Exit"
    ]

    for message in messages:
        send_message(message)
        time.sleep(2)

if __name__ == "__main__":
    main()

