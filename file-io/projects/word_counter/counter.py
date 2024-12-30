with open("file-io/projects/word_counter/example.txt", "r+") as file:
    print("Counting how many words are in the file...")
    content = file.read()
    words = content.split()
    print(f"Content: {content}")
    print(f"Words: {words}")
    print(f"Word count: {len(words)}")
