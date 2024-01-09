import pprint
def create_chord_dictionary_from_file(file_path):
    chord_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ',' in line:  # Processing a line with chord data
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    # Extracting the name and integer spelling
                    name = parts[0]
                    integer_spelling = set(map(int, parts[2].split()))
                    chord_dict[name] = integer_spelling
    return chord_dict

def create_chords_from_file(chord_spellings):
    with open(chord_spellings, 'r') as file:
        chord_data = file.readlines()
    
    chords = []
    for line in chord_data:
        if ',' not in line:  # This ensures we're processing a line with chord data
            chord_type = line.strip()
        else:
            parts = line.strip().split(', ')
            name = parts[0]
            standard_spelling = set(parts[1].split(' '))
            integer_spelling  = set(parts[2].split(' '))
            chord = Chord(chord_type, name, standard_spelling, integer_spelling)
            chords.append(chord)
            
    return chords

def process_scale_lines(lines):
    scale_dict = {}
    
    for line in lines:
        line = line[:23] + ';' + line[23:]  # Insert ';' at the 24th column
        parts = line.split(';')
        if len(parts) == 3:  # Adjust the condition to match the number of columns in your file
            scale_num, binary_notes, scale_name = parts  # Adjust the indices based on your file structure
            integer_spelling = decimal_to_scale_tones(scale_num.strip())
            scale_dict[scale_name.strip()] = integer_spelling
    return scale_dict   

def decimal_to_scale_tones(decimal_number):
    decimal_number = int(decimal_number)
    # Convert the decimal number to binary. The binary representation is right-aligned
    # and padded with zeros to ensure it always has 12 digits.
    binary_representation = format(decimal_number, '012b')

    # Calculate the scale tones. If a bit is '1', the corresponding note (index + 1) is included.
    scale_tones = [i + 1 for i, bit in enumerate(binary_representation) if bit == '1']

    return tuple(scale_tones)

# Use this to read your file
with open('scale_spellings.txt', 'r') as file:
    scale_lines = file.readlines()

scales_dict = process_scale_lines(scale_lines)
pprint.pprint(scales_dict)
