morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def convert_to_morze(text):
    text = text.upper()
    result = ""
    for char in text:
        if char in morze_dict:
            result += morze_dict.get(char) + " "
    return result[:-1]

#the second version how to do it
 """def convert_to_morze(text):
     text = text.upper()
     result = list()
     for char in text:
         if char in morze_dict:
             result.append(morze_dict.get(char))
     return ' '.join(result)"""


text = input("Enter text to convert: ")
print(convert_to_morze(text))
