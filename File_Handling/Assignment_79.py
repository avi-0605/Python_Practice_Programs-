#Remove Blank Lines Read a text file and write its content to a new file, omitting any blank lines.
try:
    with open("input.txt", "r") as source_file:
        lines = source_file.readlines()

    # Open the output file for writing
    with open("output.txt", "w") as destination_file:
        for line in lines:
            if line.strip():  # Check if the line is not blank
                destination_file.write(line)

    print("Blank lines removed and content written to output.txt.")
except FileNotFoundError:
    print("Source file not found.")
