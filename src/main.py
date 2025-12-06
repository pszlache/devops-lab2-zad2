print("Type same word for repeat: ")

while True:
    text = input("You: ")
    if text.lower() == "end":
        print("Program finish.")
        break
    print("Program:", text)
