import g4f
import pprint
import sys
import music_data
from collections import deque

base_notes = [0, 5, 10, 15, 19, 24] #Standard tuning EADGBE in integer notation

# Define the Chord class and a function to create instances for each chord from the file
class Chord:
    """
    Represents a musical chord with standard and integer spellings.

    Attributes:
        name (str): The name of the chord.
        standard_spelling (str): The standard notation of the chord.
        integer_spelling (set of int): The integer representation of the chord.
    """
        
    

    def __init__(self, name, standard_spelling = "", integer_spelling = []):
        """
        Initializes a Chord instance.

        Parameters:
            name (str): The name of the chord.
            standard_spelling (str): The standard notation of the chord.
            integer_spelling (set of int): The integer representation of the chord.
        """
        
        self.name = name
        if not standard_spelling and integer_spelling:
            # Convert from integer to standard
            self.standard_spelling = music_data.convert_spelling(integer_spelling, 1)
            self.integer_spelling = integer_spelling
        elif not integer_spelling and standard_spelling:
            # Convert from standard to integer
            self.integer_spelling = music_data.convert_spelling(standard_spelling, 0)
            self.standard_spelling = standard_spelling
        elif standard_spelling and integer_spelling:
            self.standard_spelling = standard_spelling
            self.integer_spelling = integer_spelling
        else:
            raise ValueError("At least one of standard_spelling or integer_spelling must be provided")
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_standard_spelling(self):
        return self.standard_spelling

    def set_standard_spelling(self, standard_spelling):
        self.standard_spelling = standard_spelling

    def get_integer_spelling(self):
        return self.integer_spelling

    def set_integer_spelling(self, integer_spelling):
        self.integer_spelling = integer_spelling

    def __repr__(self):
        return f"Chord(name='{self.name}', standard_spelling='{self.standard_spelling}', integer_spelling='{self.integer_spelling}')"

class ChordGroup():  
    """
    A collection of Chord objects initialized from a predefined chord map.
    """

    chords = []
    for chord_name, chord_data in music_data.chord_map.items():
        chord = Chord(chord_name, chord_data[0], chord_data[1])
        chords.append(chord)

class ChordShape(Chord):
    """
    Represents the shape of a chord on a guitar fretboard.

    Attributes:
        coords (list of int): Coordinates on the fretboard.
        root (int): The root note position.
        diagram (list): Visual representation of the chord shape.
        myStrings (list): String representation for the chord diagram.
        chord (Chord): Associated Chord object.
    """

    def __init__(self, coords):
        """
        Initializes a ChordShape instance.

        Parameters:
            coords (list of int): Coordinates representing the chord shape on the fretboard.
        """

        self.fret = "O"
        self.r_fret = "0"

        self.root = coords[0]
        self.coords = coords[1:]
        self.notes
        self.spelling
        self.findSpelling()
        self.notes_of_shape(coords)
        self.coords_matrix

        self.chord = None

        self.diagram = Diagram(self.coords)

           #Find th  e chord in list of chords with same spelling as this shape, assign to chord

    def __repr__(self):
        return f"ChordShape(name='{self.chord.name}', standard_spelling='{self.chord.standard_spelling}', root='{self.root}', coords='{self.coords}')"

    def getCoords(self):
        return self.coords

    def getName(self):
        return self.myName

    def setName(self, name):
        self.myName = name

    def getRoot(self):
        return self.root
    
    def notes_of_shape(self):
        #Find the absolute notes of the shape
        self.notes = [base_note + coord - 1 if coord != 0 else None for base_note, coord in zip(base_notes, self.coords)]
        root_note = self.notes[self.root - 1]


    def findSpelling(self):
        spelling = set()
        root_note = self.notes[self.root - 1]
        for note in self.notes:
            if note is not None:
                spelling.add((note - root_note) % 12)
        self.spelling = spelling
        self.match_chord()
    
    def coords_to_2D(self):
        min_fret = min(coord - 1 for coord in self.coords if coord != 0)
        max_fret = max(coord - 1 for coord in self.coords if coord != 0)
        twoD_coords = [[None for _ in range(6)] for _ in range(max_fret - min_fret + 1)]
        
    def match_chord(self):
        if self.chord is None:
            for chord in ChordGroup.chords:
                if set(chord.integer_spelling) == spelling:
                    self.chord = chord
                    return
            
        self.chord = Chord("None", music_data.convert_spelling(spelling, 1), spelling) #TODO how to name chord?

    def printDiagram(self):
        for innerArray in self.diagram:
            print(" ".join(innerArray))

class Scale():
    def __init__(self, name, integer_spelling):
        self.integer_spelling = integer_spelling
        self.coords = Scale.create_coords(integer_spelling)
        self.diagrams = Scale.create_diagrams(integer_spelling)
        self.notes = []
        self.chords = []

    @staticmethod
    def create_coords(integer_spelling):
        r_height = 1
        coords = []
        for root in range(0, 5):
            root_note = (base_notes[root] + r_height) % 12
            queue = deque([(n + root_note) % 12 for n in integer_spelling].sort())

            for string in range(0, 6): 
                first_fret = 0
                count = 0
                scale_note = scale_note if scale_note is not None else queue.popleft()
                for fret in range(0, 5): 
                    fret_distance = fret - first_fret
                    fret_note = (base_notes[string] + fret) % 12
                    if fret_note == scale_note and fret_distance < 4:
                        if count == 0:
                            first_fret = fret
                        count += 1

                        coords[root][fret][string] = scale_note - root_note if scale_note >= root_note else scale_note - root_note + 12 #put the integer scale tone in the right place
                        queue.append(scale_note)
                        scale_note = queue.popleft()

        return coords

    def create_diagrams(integer_spelling):
        coords = Scale.create_coords(integer_spelling)

        diagrams = []
        for i in range(0, len(coords)):
            diagrams.append(Diagram(coords[i]))
        
        return diagrams
            

class Diagram: #TODO
    def __init__(self, root, coords):
        self.root = root
        self.coords = coords
        min_fret = None
        max_fret = None

        num_frets = max(5, max_fret - min_fret)

    for i in range(0, len(self.coords)):
        if self.coords[i] != 0:
            self.coords[i] = self.coords[i] - min_fret + 1
        
    
    diagram = [["|", "|", "|", "|", "|", "|"] for _ in range(num_frets + 2)]
    diagram[1].append(" " + str(min_fret))

    for i in range(0, len(self.coords)):
        if self.coords[i] != 0:
            diagram[self.coords[i]][i] = self.fret
        else:
            diagram[0][i] = "x"

    diagram[self.coords[self.root - 1]][self.root - 1] = self.r_fret

def main():
    penta = Scale("Pentatonic", (1, 3, 5, 8, 10))
    print(penta.coords)

main()
def displayChord():
    """
    Interactive loop for displaying chord shapes based on user input.
    """

    while True:
        user_input = input("Enter command (q to quit): ")
        if user_input == 'q':
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter 7-digit numbers.")
            continue

        coordinates = [int(digit) for digit in user_input]  

        shape = ChordShape(coordinates)
        shape.printDiagram()
        print()
        print(shape)
        print()

