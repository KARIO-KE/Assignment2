def get_input():
    while True:
        user_input = input("Enter a word (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            break
        print(user_input)
get_input()