#File Statistics Display file statistics such as total characters, total lines, total words, etc.
with open('output.txt', 'r') as file:
    text = file.read()
    
print("Characters:", len(text))
print("Lines:", len(text.splitlines()))
print("Words:", len(text.split()))

