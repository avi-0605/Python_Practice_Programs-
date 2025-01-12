# Number to Words Convert an integer (e.g., 123) to words (e.g., "one two three").

def number_to_words(num):
    num_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return ' '.join(num_words[digit] for digit in str(num))
num = int(input("Enter a number: "))
print(f"The number {num} in words is: {number_to_words(num)}")
