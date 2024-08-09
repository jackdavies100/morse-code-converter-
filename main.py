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
                    '(':'-.--.', ')':'-.--.-'}

def text_to_morse(answer):
    coded_words = []
    for letter in answer:
        if letter in MORSE_CODE_DICT:
            coded_words.append(MORSE_CODE_DICT[letter])
        else:
            coded_words.append(' ')
    return ' '.join(coded_words)

def morse_to_text(answer):
    words = answer.split(' ')
    decoded_text = ''
    for morse_code in words:
        for letter, code in MORSE_CODE_DICT.items():
            if code == morse_code:
                decoded_text += letter
                break
        else:
            decoded_text += ' '
    return decoded_text

def main():
    print('''   
:'######:::'#######::'########::'########:                                
'##... ##:'##.... ##: ##.... ##: ##.....::                                
 ##:::..:: ##:::: ##: ##:::: ##: ##:::::::                                
 ##::::::: ##:::: ##: ##:::: ##: ######:::                                
 ##::::::: ##:::: ##: ##:::: ##: ##...::::                                
 ##::: ##: ##:::: ##: ##:::: ##: ##:::::::                                
. ######::. #######:: ########:: ########:                                
:......::::.......:::........:::........::                                
'########::'########::'########::::'###::::'##:::'##:'########:'########::
 ##.... ##: ##.... ##: ##.....::::'## ##::: ##::'##:: ##.....:: ##.... ##:
 ##:::: ##: ##:::: ##: ##::::::::'##:. ##:: ##:'##::: ##::::::: ##:::: ##:
 ########:: ########:: ######:::'##:::. ##: #####:::: ######::: ########::
 ##.... ##: ##.. ##::: ##...:::: #########: ##. ##::: ##...:::: ##.. ##:::
 ##:::: ##: ##::. ##:: ##::::::: ##.... ##: ##:. ##:: ##::::::: ##::. ##::
 ########:: ##:::. ##: ########: ##:::: ##: ##::. ##: ########: ##:::. ##:
........:::..:::::..::........::..:::::..::..::::..::........::..:::::..::
                                                               
''')
    print("Welcome to the Morse code converter.")
    option_1 = input("Choose an option. To convert text to Morse code, enter 1,  to convert Morse code to text, enter 2: ")

    if option_1 == '1':
        text = input("Enter the text you want to convert to Morse code: ").upper()
        result = text_to_morse(text)
        print("Morse code:", result)
    elif option_1 == '2':
        morse_code = input("Enter the Morse code you want to convert to text (separate letters with spaces): ")
        result = morse_to_text(morse_code)
        print("Decoded text:", result)
    else:
        print("Invalid option. Please choose either 1 or 2.")

    main()

main()