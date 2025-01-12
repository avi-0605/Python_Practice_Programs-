#Character Frequency in String Build a dictionary that tracks how many times each character appears in a string.
def character_frequency(input_str):
    freq_dict = {}
    for char in input_str:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1
    return freq_dict
input_string = input("Enter a string: ")
frequency = character_frequency(input_string)
print("Character frequency:", frequency)
