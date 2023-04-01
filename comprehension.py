def gen_board(size, initial_val=None):
   return[[initial_val for x in range(size)] for y in range(size)]

chickens = [
   {"name": 'Henry', "sex": 'Rooster'},
   {"name": 'Lady Gray', "sex": 'Hen'},
   {"name": 'Junior', "sex": 'Rooster'},
   {"name": 'Stevie Chicks', "sex": 'Hen'},
   {"name": 'Rocket', "sex": 'Hen'},
   {"name": 'Butters', "sex": 'Rooster'},
]
hens = [bird["name"] for bird in chickens if bird["sex"]== "Hen"]

# ['Lady Gray', 'Stevie Chicks', 'Rocket']


# We want to translate the list into [FAIL, PASS, PASS, FAIL] etc
scores = [55, 89, 99, 87, 60, 70, 74, 76, 50, 82]
# grades = ["PASS" for score in scores if score >= 70]
# That will only give us pass. If we want two outcomes, we write a statement like so:
# [PASS if passing_score else FAIL for thing in things]
grades = ["PASS" if score >= 70 else "FAIL" for score in scores]

# Functions inside a comprehension:
def get_letter(ltr):
    morse_lookup = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..','E':'.','F':'..-.','G':'--.', 'H':'....','I':'..', 'J':'.---','K':'-.-', 'L':'.-..','M':'--', 'N':'-.','O':'---', 'P':'.--.','Q':'--.-','R':'.-.','S':'...', 'T':'-','U':'..-', 'V':'...-','W':'.--', 'X':'-..-','Y':'-.--', 'Z':'--..','1':'.----', '2':'..---','3':'...--', '4':'....-','5':'.....', '6':'-....','7':'--...', '8':'---..','9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.','-':'-....-', '(':'-.--.',')':'-.--.-'}
    return morse_lookup.get(ltr.upper(), '')

msg = [get_letter(char) for char in 'SOS']

def get_morse_code(string):
    return " ".join([get_letter(char) for char in string])