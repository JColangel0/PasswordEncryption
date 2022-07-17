alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z", ",", "<", ".", ">", "/", "?", ";", ":",
            "[", "]", "{", "}", "~", "`", "!", "@", "#", "$", "%", "^",
            "&", "*", "(", ")", "_", "-", "+", "=", "1", "2", "3", "4",
            "5", "6", "7", "8", "9", "0", "'", " ", "|"]

markToken = "|"


def numeralize(letter):
    i = 0
    while i < len(alphabet):
        if alphabet[i] == letter:
            return i
        i += 1


def denumeralize(number):
    return alphabet[number]


def hash(sequence):
    sequence *= 12
    sequence += 497
    sequence *= 132
    sequence -= 201

    return sequence


def dehash(sequence):
    sequence += 201
    sequence /= 132
    sequence -= 497
    sequence /= 12

    return int(sequence)


def Encrypt(uncoded):
    indexes = []
    for x in uncoded:
        indexes.append(x)
    i = 0
    while i < len(indexes):
        if isinstance(indexes[i], str):
            indexes[i] = numeralize(indexes[i])
        indexes[i] = hash(indexes[i])
        i += 1
    f = open(
        "passwords.txt", "a")
    for x in indexes:
        f.write(str(x))
        f.write(markToken)
    f.write("\n\n")
    f.close()
    decider()


def Decrypt():
    letters = []
    with open("passwords.txt") as f:
        data = f.read()
        j = 0
        marker = 0
        while j < len(data):
            if data[j] == markToken:
                dehashed = dehash(int(data[marker:j]))
                letters.append(denumeralize(dehashed))
                marker = j+1
            elif data[j] == "\n":
                letters.append("\n")
            j += 1
    passkey = ""
    for x in letters:
        passkey += x
    print(passkey)
    decider()


def decider():
    function = input(
        "Enter 'E' to Encrypt a new password, 'A' to access your passwords, or 'X' to exit: ")
    runtime(function)


def runtime(designator):
    if designator == 'E' or designator == 'e':
        site = input("What site is this password for? ")
        newPassword = input("Enter your new password: ")
        Encrypt(site+": "+newPassword)
    elif designator == 'A' or designator == 'a':
        Decrypt()
    elif designator == 'X' or designator == 'x':
        return
    else:
        decider()


decider()
