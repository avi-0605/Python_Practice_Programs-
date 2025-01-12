# Longest Word in a Sentence Prompt the user for a sentence, split it into words, and find the longest word.
def longest_word(sentence):
    words = sentence.split()
    
    longest = max(words, key=len)
    return longest
sentence = input("Enter a sentence: ")

print("The longest word is:", longest_word(sentence))
