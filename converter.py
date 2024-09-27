# converter.py

from morse_code import MORSE_CODE_DICT

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char != ' ':
            morse_char = MORSE_CODE_DICT.get(char, '')
            if morse_char:
                morse_code.append(morse_char)
        else:
            morse_code.append('/')
    return ' '.join(morse_code)

def morse_to_text(morse):
    inverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = []
        for letter in letters:
            decoded_char = inverse_dict.get(letter, '')
            decoded_letters.append(decoded_char)
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)
