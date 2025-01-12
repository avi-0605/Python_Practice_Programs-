# Decimal to Binary Conversion Prompt the user for a decimal integer and convert it to binary.

def dec_to_bin(decimal_int):
    return bin(decimal_int)[2:] 
decimal_integer = int(input("Enter a decimal integer: "))
binary_value = dec_to_bin(decimal_integer)
print(f"The binary value of {decimal_integer} is {binary_value}.")

