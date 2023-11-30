import unittest
from mourse import english_to_morse, morse_to_english, MorseError
#import mourse 

class TestMorseCodeConverter(unittest.TestCase):

    def test_english_to_morse_valid_input(self):
        text_to_encrypt = "HELLO WORLD"
        result = english_to_morse(text_to_encrypt)
        expected_result = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        self.assertEqual(result, expected_result)

    def test_english_to_morse_invalid_input(self):
        with self.assertRaises(MorseError):
            english_to_morse("123")  # Invalid input containing numbers

    def test_morse_to_english_valid_input(self):
        morse_to_decrypt = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        result = morse_to_english(morse_to_decrypt)
        expected_result = "HELLO WORLD"
        self.assertEqual(result, expected_result)

    def test_morse_to_english_invalid_input(self):
        with self.assertRaises(MorseError):
            morse_to_english("... 123 ...")  # Invalid Morse code containing numbers

    def test_morse_to_english_invalid_morse_code(self):
        with self.assertRaises(MorseError) as context:
            morse_to_english(".... .-. --- .- .a")  # Invalid Morse code

    # Optionally, you can check the error message if needed
            expected_error_message = "Error: Invalid Morse code character '.a'."
            self.assertEqual(str(context.exception), expected_error_message)

if __name__ == '__main__':
    unittest.main()
