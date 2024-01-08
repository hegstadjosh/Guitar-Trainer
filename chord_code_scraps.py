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
