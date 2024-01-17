import pprint
import random
import music_objects as mo
'''
File that demonstrates the functionality of the music_objects.py file in conjunction 
with the data in music_data.py.
'''

def main():
    random_scale = list(mo.music_data.scale_map)[random.randint(0, len(mo.music_data.scale_map) - 1)]
    random_scale = mo.Scale(random_scale, mo.music_data.scale_map[random_scale])

    print(str(random_scale) + ": ")

    # print("Diagram 1: " )
    # random_scale.print_diagram(0), print()
    print("Diagram: " )
    random_scale.print_diagram(1), print()
    # print("Diagram 3: " )
    # random_scale.print_diagram(2), print()
    # print("Diagram: " )
    # random_scale.print_diagram('A'), print()

    print("-------------------------------------------------------------")
    chord1 = mo.ChordShape([1, 1, 3, 3, 2, 1])
    chord1.print_diagram()
    print(chord1.chord), print()

'''
Displays a menu of options for the user to choose from.
'''
def menu(): 
    while True:
        print("1. Chord Viewer")
        print("2. Scale Viewer")
        print("3. Note Conversion")
        user_input = input("Please enter the number of your choice: ")
        if user_input == "q": 
            break
        if user_input == "1":
            chord_viewer()
        elif user_input == "2":
            scale_viewer()
        elif user_input == "3":
            note_conversion()
        else:
            print("Invalid input. Please try again.")
            continue

'''
Displays chord attributes given chord name, spelling, or coordinates.

Example (equivalent) inputs: 'Minor 7th', '1 b3 5 b7', '0 3 7 10', '1101110'

Coordinates are 7-digits, first is the string with the root on it (1-6), rest are
  fret numbers (1-) or 0 if the string is not played.

ex: '1101110' corresponds to the diagram: 
| x | | | x
O | O O O |
| | | | | |
'''
def chord_viewer():
    print()
    print("--------------------Chord Viewer---------------------")
    print("This method accepts input of the types 'name', 'std', 'int', and 'fret'")
    print("  i.e. a chord's name, standard or integer spelling, or 7-digit coordinates \n  and returns the chord attributes (And diagram if 'fret' is used)")
    print("  Example: Chord(name='Diminished 7th', standard_spelling='1 b3 b5 bb7', integer_spelling='(0, 3, 6, 9)')")
    print()
    while True: 
        user_input = input("Enter a string in the format <Input Type> <Input>: ")
        if user_input == "q":
            break
        else:
            parts = user_input.split(maxsplit=1)
            if len(parts) != 2:
                print("Invalid input. Please try again.")
                continue
            else:
                input_type = parts[0]
                data = parts[1].strip("'")  # Remove enclosing single quotes

                if input_type == "name":
                    chord = mo.Chord(data)
                elif input_type == "std":
                    chord = mo.Chord(None, data)
                elif input_type == "int":
                    chord = mo.Chord(None, None, data)
                elif input_type == "fret":
                    chord = mo.ChordShape(data)
                    chord.print_diagram()
                    chord = chord.chord
                else:
                    print("Invalid input. Please try again.")
                    continue
                print(chord)
                print()

'''
Displays the fretboard diagram, name, and integer spelling of a scale given either 
the name (provided it's in music_data.scale_map) or the integer spelling.

Example (equivalent) inputs: 'Major', '0 2 4 5 7 9 11'
'''
def scale_viewer():
    print()
    print("--------------------Scale Viewer---------------------")
    print("This function displays scale diagrams given a scale's name or integer spelling.")
    print("  i.e. 'Major' / '0 2 4 5 7 9 11'")
    print()
    type = input("  Enter nothing for plain diagrams or\n  1: integer tones\n  2: Standard tones\n  'A', 'B'...: notes\n")
    while True:
        user_input = input("Enter a scale name or integer spelling: ")
        if user_input == "q": 
            break
        
        if user_input.replace(" ", "").isdigit():
            user_input = [int(digit) for digit in user_input.split()]
            scale = mo.Scale(None, user_input)
        else:
            scale = mo.Scale(user_input)
        
        print()
        if scale.diagram is not None:
            scale.print_diagram(type)
        print(scale)
    
def note_conversion():
    print("function not yet supported\n")

main()
menu()