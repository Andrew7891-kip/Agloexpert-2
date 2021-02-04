# def encrypt(message,key):
#     grid=[[] for _ in range(key)]
#     lowest=key-1
#     if key<=0:
#         raise ValueError("height can't be lower than 0")
#     if key==1 and len(message)<=key:
#         return message

#     for p,c in enumerate(message):
#         num=p%(lowest*2)
#         num=min(num,lowest*2-num)
#         grid[num].append(c)
#     grid=["".join(row) for row in grid]
#     output="".join(grid)

#     return output

# mess="i am andrew from eldoret"
# print(encrypt(mess,13))

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "&": ".-...",
    "@": ".--.-.",
    ":": "---...",
    ",": "--..--",
    ".": ".-.-.-",
    "'": ".----.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    # Exclamation mark is not in ITU-R recommendation
    "!": "-.-.--",
}
def encrypt(message):
    message=message.upper()
    cipher=""
    for letter in message:
        if letter != " ":
            cipher+= MORSE_CODE_DICT[letter]+ " "
        else:
            cipher+="/ "
    return cipher[:-1]

mess="Shuffles the character of a string by placing each of them"
print(encrypt(mess))

def decrypt(data):
    decipher=""
    letter=data.split(" ")
    for i in letter:
        if i != "/":
            decipher+= list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(i)]
        else:
            decipher+=" "
    return decipher
messa="... .... ..- ..-. ..-. .-.. . ... / - .... . / -.-. .... .- .-. .- -.-. - . .-. / --- ..-. / .- / ... - .-. .. -. --. / -... -.-- / .--. .-.. .- -.-. .. -.--. / . .- -.-. .... / --- ..-. / - .... . --"
print(decrypt(messa))