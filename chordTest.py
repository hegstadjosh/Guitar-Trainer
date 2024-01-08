import g4f
import pprint

# Define the Chord class and a function to create instances for each chord from the file
class Chord:
    chord_map = {'Major 7th': ('1 3 5 7', (1, 5, 8, 12)),
                'Dominant 7th': ('1 3 5 b7', (1, 5, 8, 11)),
                'Minor 7th': ('1 b3 5 b7', (1, 4, 8, 11)),
                'Half-Diminished 7th (m7♭5)': ('1 b3 b5 b7', (1, 4, 7, 11)),
                'Diminished 7th': ('1 b3 b5 bb7', (1, 4, 7, 10)),
                'Minor Major 7th': ('1 b3 5 7', (1, 4, 8, 12)),
                'Augmented Major 7th': ('1 3 #5 7', (1, 5, 9, 12)),
                'Augmented 7th': ('1 3 #5 b7', (1, 5, 9, 11)),
                'Major 7 (b5)': ('1 3 b5 7', (1, 5, 7, 12)),
                'Dominant 7 (b5)': ('1 3 b5 b7', (1, 5, 7, 11)),
                'Major 6th': ('1 3 5 6', (1, 5, 8, 10)),
                'Minor 6th': ('1 b3 5 6', (1, 4, 8, 10)),
                'Dominant 9th': ('1 3 5 b7 9', (1, 5, 8, 11, 3)),
                'Dominant 11th': ('1 3 5 b7 9 11', (1, 5, 8, 11, 3, 6)),
                'Dominant 13th': ('1 3 5 b7 9 11 13', (1, 5, 8, 11, 3, 6, 10)),
                'Major 9th': ('1 3 5 7 9', (1, 5, 8, 12, 3)),
                'Major 11th': ('1 3 5 7 9 11', (1, 5, 8, 12, 3, 6)),
                'Major 13th': ('1 3 5 7 9 11 13', (1, 5, 8, 12, 3, 6, 10)),
                'Minor 9th': ('1 b3 5 b7 9', (1, 4, 8, 11, 3)),
                'Minor 11th': ('1 b3 5 b7 9 11', (1, 4, 8, 11, 3, 6)),
                'Minor 13th': ('1 b3 5 b7 9 11 13', (1, 4, 8, 11, 3, 6, 10)),
                'Minor Major 9': ('1 b3 5 7 9', (1, 4, 8, 12, 3)),
                'Major 7#11': ('1 3 5 7 #11', (1, 5, 8, 12, 7)),
                'Major 13#11': ('1 3 5 7 9 #11 13', (1, 5, 8, 12, 3, 7, 10)),
                'Thirteen Sharp 11': ('1 3 5 b7 9 #11 13', (1, 5, 8, 11, 3, 7, 10)),
                'Thirteen Flat 9': ('1 3 5 b7 9 b13', (1, 5, 8, 11, 3, 9)),
                'Seven Flat 9': ('1 3 5 b7 b9', (1, 5, 8, 11, 2)),
                'Seven Sharp 9': ('1 3 5 b7 #9', (1, 5, 8, 11, 4)),
                'Sus2': ('1 2 5', (1, 3, 8)),
                'Sus4': ('1 4 5', (1, 6, 8)),
                '7sus4': ('1 4 5 b7', (1, 6, 8, 11)),
                '9sus4': ('1 4 5 b7 9', (1, 6, 8, 11, 3)),
                'Seven Sus4 Flat9': ('1 4 5 b7 b9', (1, 6, 8, 11, 2)),
                'Thirteen Sus4': ('1 4 5 b7 9 13', (1, 6, 8, 11, 3, 10)),
                'Major (no5)': ('1 3', (1, 5)),
                'Minor (no5)': ('1 b3', (1, 4)),
                '7 (no5)': ('1 3 b7', (1, 5, 11)),
                'm7 (no5)': ('1 b3 b7', (1, 4, 11)),
                'Omit 3 (Power Chord)': ('1 5', (1, 8)),
                '7 Omit 3': ('1 5 b7', (1, 8, 11)),
                'Add9': ('1 3 5 9', (1, 5, 8, 3)),
                'mAdd9': ('1 b3 5 9', (1, 4, 8, 3)),
                'Add11': ('1 3 5 11', (1, 5, 8, 6)),
                'mAdd11': ('1 b3 5 11', (1, 4, 8, 6)),
                'Six Nine': ('1 3 5 6 9', (1, 5, 8, 10, 3)),
                'Minor Six Add Nine': ('1 b3 5 6 9', (1, 4, 8, 10, 3)),
                'Minor Seven Add 11': ('1 b3 5 b7 11', (1, 4, 8, 11, 6))}   
    

    def __init__(self, name, standard_spelling, integer_spelling):
        self.name = name
        if standard_spelling is None and integer_spelling is not None:
            # Convert from integer to standard
            self.standard_spelling = self.convert_spelling(integer_spelling, 1)
            self.integer_spelling = integer_spelling
        elif integer_spelling is None and standard_spelling is not None:
            # Convert from standard to integer
            self.integer_spelling = self.convert_spelling(standard_spelling, 0)
            self.standard_spelling = standard_spelling
        elif standard_spelling is not None and integer_spelling is not None:
            self.standard_spelling = standard_spelling
            self.integer_spelling = integer_spelling
        else:
            raise ValueError("At least one of standard_spelling or integer_spelling must be provided")

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

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
    
    @staticmethod
    def convert_spelling(spelling, conversion_type):
        if conversion_type == 0 and type(spelling) != str:
            spelling = ' '.join(spelling)  # Convert to string
        elif conversion_type == 1 and type(spelling) != set:
            spelling = set(spelling)  # Convert to set

        # Check if spelling is a chord name in chord_map
        for chord_name, spellings in Chord.chord_map.items():
            if spellings[conversion_type] == spelling:
                return spellings[conversion_type - 1]  # Return other spelling type

        # If mapping not found, convert manually (only using flats)

        # Mapping from standard to integer, including double sharps and flats
        standard_to_integer = {
            '1': 1, 'b2': 2, '2': 3, '#2': 4, 'x2': 5, 'b3': 4, '3': 5, 'x3': 6, '4': 6, '#4': 7, 'x4': 8,
            'b5': 7, '5': 8, '#5': 9, 'x5': 10, 'b6': 9, '6': 10, '#6': 11, 'x6': 12, 'bb7': 10, 'b7': 11, '7': 12
        }
        # Inverse mapping for integer to standard
        integer_to_standard = {v: k for k, v in standard_to_integer.items()}

        converted = []
        if conversion_type == 0:
            # Convert from standard to integer
            converted = [standard_to_integer.get(note, note) for note in spelling]
            converted = ' '.join(converted)  # Convert to string
        elif conversion_type == 1:
            # Convert from integer to standard
            converted = [integer_to_standard.get(note, note) for note in spelling]
            converted = set(converted)  # Convert to set

        return converted

class ChordGroup():
    chords = []
    for chord_name, chord_data in Chord.chord_map.items():
        chord = Chord(chord_name, chord_data[0], chord_data[1])
        chords.append(chord)

class ChordShape():
    def __init__(self, coords):
        self.fret = "O"
        self.r_fret = "0"

        self.myCoords = coords[1:]
        self.myRoot = coords[0]

        self.myDiagram = None
        self.myStrings = None
        self.diagram()              #initializes myDiagram and myStrings

        self.myNotes = None
        self.myChord = Chord("None", "None", "None")  
        self.findSpelling()   #Find the chord in list of chords with same spelling as this shape, assign to myChord

    def __repr__(self):
        return f"ChordShape(name='{self.myChord.name}', standard_spelling='{self.myChord.standard_spelling}', myRoot='{self.myRoot}', myCoords='{self.myCoords}')"

    def getCoords(self):
        return self.myCoords

    def getName(self):
        return self.myName

    def setName(self, name):
        self.myName = name

    def getRoot(self):
        return self.myRoot
    
    def findSpelling(self):
        base_notes = [0, 5, 10, 15, 19, 24]
        self.myNotes = [base_note + coord if coord is not None else None for base_note, coord in zip(base_notes, self.myCoords)]
        
        spelling = set()
        root_note = self.myNotes[self.myRoot - 1]
        for note in self.myNotes:
            if note is not None:
                spelling.add((note - root_note) % 12 + 1)

        for chord in ChordGroup.chords:
            if set(chord.integer_spelling) == spelling:
                self.myChord = chord
                break

    def diagram(self):
        strings = ["|"]*6
        self.myStrings = strings

        for i in range(0, len(self.myCoords)):
            if self.myCoords[i] == None:
                self.myStrings[i] = "x"

        diagram = [["|", "|", "|", "|", "|", "|"],
                   ["|", "|", "|", "|", "|", "|"],
                   ["|", "|", "|", "|", "|", "|"],
                   ["|", "|", "|", "|", "|", "|"],
                   ["|", "|", "|", "|", "|", "|"]]

        for i in range(1, len(self.myCoords)):
            if self.myCoords[i] != None:
                diagram[self.myCoords[i] + 1][i] = self.fret

        diagram[self.myCoords[self.myRoot - 1] + 1][self.myRoot - 1] = self.r_fret

        self.myDiagram = diagram

    def printDiagram(self):
        print(" ".join(self.myStrings))

        for innerArray in self.myDiagram:
            print(" ".join(innerArray))

def main():
    shapes = []
    shapes.append(ChordShape([1, 0, None, 0, 1, 0, None]))
    shapes.append(ChordShape([2, None, 0, 2, 1, 2, 0]))
    shapes.append(ChordShape([3, None, None, 0, 1, 1, 1]))
    for shape in shapes:
        shape.printDiagram()
        print()
        print(shape)
        print()

main()