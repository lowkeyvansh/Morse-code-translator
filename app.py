MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def to_morse_code(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), char) for char in text)

def from_morse_code(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(char, char) for char in morse.split())

choice = input("Do you want to encode or decode (e/d)? ").lower()
if choice == 'e':
    text = input("Enter text to encode: ")
    print(to_morse_code(text))
elif choice == 'd':
    morse = input("Enter morse code to decode: ")
    print(from_morse_code(morse))
