# Binary to Decimal Conversion Prompt the user for a binary string and convert it to decimal.

def bin_to_dec(binary_str):
    return int(binary_str, 2)

# Example usage:
binary_string = input("Enter a binary string: ")
decimal_value = bin_to_dec(binary_string)
print(f"The decimal value of ",binary_string,"is",decimal_value)
