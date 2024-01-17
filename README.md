To understand this repo you don't really need to know music theory.
However, you have to know
  There are generally 12 notes in music (A-G#)
  Scales are sets of unique notes
  Chords are sets of not-necessarily unique notes
  A guitar has 6 strings with note values of E,A,D,G,B,E (standard tuning)
    Each fret on a guitar (notches along the string's length) increases the 
    played string's note by one tone or half-step

So scales and chords can be represented by 'integer spellings', or the integer
(0-11) values that make them up. 

Major 7th Chord: 0, 4, 7, 11
Major Scale:     0, 2, 4, 5, 7, 9, 11

And the open (unfretted) strings on a guitar correspond to 7, 12, 17, 22, 26, 31 

Standard music theory uses different notation for spellings, where flats (b) decrement
the note value by 1 and sharps (#) increment. Here's a dictionry of standard: integer spellings:

tones_to_integer = {
    '1': 0, 'b2': 1, '2': 2, '#2': 3, 'x2': 4, 'b3': 3, '3': 4, 'x3': 5, '4': 5, '#4': 6, 'x4': 7,
    'b5': 6, '5': 7, '#5': 8, 'x5': 9, 'b6': 8, '6': 9, '#6': 10, 'x6': 11, 'bb7': 9, 'b7': 10, '7': 11
}

For this program, 'fretboard coordinates' are 7-digits. The first is the string with the root on it 
(1-6), the rest are fret numbers (1-) or 0 if the string is not played.

ex: '1101110' corresponds to the diagram: 
| x | | | x
O | O O O |
| | | | | |
'''
