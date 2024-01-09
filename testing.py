import re

def decrease_numbers_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line after line 44
    for i in range(44, len(lines)):
        # Find all numbers in the line and decrease each by 1
        lines[i] = re.sub(r'\b\d+\b', lambda x: str(int(x.group()) - 1), lines[i])

    # Write the processed lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Example usage
file_path = 'music_data.py'
decrease_numbers_in_file(file_path)
