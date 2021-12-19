import itertools

alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N',
            'Ń', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']

code_table = [[0] * len(alphabet) for _ in alphabet]
for i, row in enumerate(code_table):
    for j, column in enumerate(row):
        code_table[i][j] = alphabet[(i+j) % len(alphabet)]


def get_keyword():
    kw = input("Wprowadź słowo-klucz\t").strip().upper()
    return kw


def encrypt(msg, kw):
    encrypted = []
    for msg_letter, kw_letter in zip(msg, itertools.cycle(kw)):
        encrypted.append(code_table[alphabet.index(msg_letter)][alphabet.index(kw_letter)])
    return ''.join(encrypted)


def decrypt(msg, kw):
    decrypted = []
    for msg_letter, kw_letter in zip(msg, itertools.cycle(kw)):
        decrypted.append(alphabet[code_table[alphabet.index(kw_letter)].index(msg_letter)])
    return ''.join(decrypted)


print("\tSZYFR VIGENERE'A //AKlamerus")
while 1:
    print("Co chcesz zrobić?\n1. Zaszyfrować wiadomość\n2. Odszyfrować wiadomość\n3. Wyjść")
    choice = int(input().strip())
    while choice not in (1, 2, 3):
        choice = int(input("Niepoprawna wartość, wybierz ponownie\n").strip())

    if choice == 3:
        break
    elif choice == 2:
        message = input("Podaj wiadomość do odszyfrowania:\n").strip().upper()
        keyword = get_keyword()
        decrypted_message = decrypt(message, keyword)
        print("Twoja odszyfrowana wiadomość brzmi:")
        print(''.join(decrypted_message), end="\n\n")
    else:
        message = input("Podaj wiadomość do zaszyfrowania:\n").strip().upper()
        keyword = get_keyword()
        encrypted_message = encrypt(message, keyword)
        print("Twoja zaszyfrowana wiadomość brzmi:")
        print(encrypted_message, end="\n\n")