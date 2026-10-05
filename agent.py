def agent(command):
    command = command.lower().strip()

    if command in ["hello", "hi", "salam"]:
        return "Hello! Main tumhara AI agent hoon."

    if "youtube" in command:
        return "YouTube task received."

    if "name" in command:
        return "Mera naam My AI Agent hai."

    if command == "help":
        return "Main tumhari commands receive kar sakta hoon."

    return "Command samajh nahi aayi."


if __name__ == "__main__":
    print("My AI Agent is running!")
    
    while True:
        command = input("You: ")

        if command.lower() == "exit":
            print("Agent stopped.")
            break

        answer = agent(command)
        print("Agent:", answer)
