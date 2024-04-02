import winsound
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '|'}


user_input = input('Enter your text ~> ')

#!---------------------------text to morse code---------------------------

def text2morse(text):
    morse_code = ' '.join(MORSE_CODE_DICT[c] for c in text.upper())
    return morse_code

morse_code = text2morse(user_input)
print(f'\nYour morse code ~> {morse_code}')
print('\nReading morse code...')

#!---------------------------morse code to text---------------------------

REVERSE_MORSE_CODE_DICT = {v:k for k,v in MORSE_CODE_DICT.items()}

def morse2text(morse):
    text = ''.join(REVERSE_MORSE_CODE_DICT[c] for c in morse.split(' '))
    return text

text = morse2text(morse_code)
print('\n' + text)

#!---------------------------  run  ---------------------------

if __name__ == '__main__':
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 1000 # Set Duration To 1000 ms == 1 second

    for i in morse_code:
        if i == '-':
            # read morse code
            winsound.Beep(frequency, duration)
        elif i == '.' :
            # read morse code
            winsound.Beep(frequency, duration-500)
        elif i == ' ' or i == '|':
            # Pause between words
            time.sleep(0.4) 
        else:
            print('ERROR!!')
