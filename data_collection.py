import os
import pprint
import requests
from bs4 import BeautifulSoup
from music_objects import Chord, ChordShape, Scale
from urllib.parse import urljoin

'''
Archive of funcitons I made to collect and/or format data from different sources. The 
formatted data is now in the music_data.py file or text files. 
'''

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

@staticmethod
def scrape_chord_shapes(url):
    print("scraping url...\t", url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with open('chord_shapes.txt', 'w') as file:
        # Find all links to text files
        count = 0
        for link in soup.find_all('a'):
                
                    href = link.get('href')
                    if href and href.endswith('.txt'):
                        txt_url = urljoin(url, href)  # Construct the full URL
                        filename = os.path.basename(txt_url)  # Get the filename
                        filename_without_ext = os.path.splitext(filename)[0]  # Remove the .txt extension
                        print(filename_without_ext + ":\n")

                        txt_response = requests.get(txt_url)
                        # if txt_response.status_code != 200:
                        #     print(f"Failed to get {txt_url}")
                        #     continue

                        # Process the text file content into ChordShape objects
                        file.write(filename_without_ext + ":\n")
                        process_chord_shapes(txt_response.text, file)
                        
                        count += 1

def process_chord_shapes(txt_content, file):
    lines = txt_content.split('\n')

    for line in lines:
        if line and all(s.isdigit() or s == 'x' for s in line.split()):
            coords = [0 if s == 'x' else int(s) + 1 for s in line.split()]
            curr = ChordShape(coords, 0)
            coords = [curr.root] + coords
            file.write(str(coords) + "\n")             
    
url = 'https://www.hakwright.co.uk/guitarchords/A_chords.html'

file = 'C:\\Users\\socce\\Desktop\\Guitar Project (Python)\\old_chord_assignments.txt'
with open(file, 'r') as file:
    lines = file.readlines()
    chords = []
    for line in lines:
        if '[' in line:
            parts = line.split('[')
            parts = parts[1].split(']')
            parts = parts[0].split(',')
            parts = [int(part.strip()) for part in parts]

            print("ChordShape(", parts, "),\n")

