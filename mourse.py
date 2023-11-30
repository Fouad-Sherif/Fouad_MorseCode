class MorseError(Exception):
    pass

morse = { 
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..'
}

def english_to_morse(input_text):
    input_text = input_text.upper()
    
    if not input_text.replace(" ", "").isalpha():
        raise MorseError("Error: Input text should only contain letters and spaces.")
    
    result = []
    for letter in input_text:
        if letter in morse:
            result.append(morse[letter])
        elif letter == " ":
            result.append("/")
        else:
                raise MorseError("the letter is not in the dictionary pls enter only alphabtes from a to z")
    return ' '.join(result)

def morse_to_english(input_morse):
    if not all(char in set(" .-") for char in input_morse):
        raise MorseError("Error: Input text should only contain Morse code characters (dot, dash, and space).")
    
    words = input_morse.split("  ")  
    result = []
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            for key, value in morse.items():
                if value == letter:
                    result.append(key)
        result.append(' ')
    return ''.join(result).strip()

def main():
    while True:
        print("Menu:")
        print("1. Enter a text to encrypt: ")
        print("2. Enter a text to decrypt: ")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            text_to_translate = input("Enter a text to encrypt: ")
            try:
                result = english_to_morse(text_to_translate)
                print(f"Morse Code: {result}")
            except MorseError as e:
                print(e)
        elif choice == '2':
            morse_to_translate = input("Enter a text to decrypt: ")
            try:
                result = morse_to_english(morse_to_translate)
                print(f"English: {result}")
            except MorseError as e:
                print(e)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# if __name__ == "__main__":
#     main()

