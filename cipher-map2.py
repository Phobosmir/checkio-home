"""
Help Sofia write a decrypter for the passwords that Nikola will encrypt through the cipher map. A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, the encoder writes down the first four symbols of his password inside the windows (see fig. below). After that, the encoder turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears inside the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. Then, they write down the following four symbols and turns the grille once more. Lastly, they write down the final four symbols of the password. Without the same cipher grille, it is difficult to discern the password from the resulting square comprised of 16 symbols. Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.



Write a module that enables the robots to easily recall their passwords through codes when they return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string.

Example:

recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd'

recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy'
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
How it is used: Here you can learn how to work with 2D arrays. You also get to learn about the ancient Grille Cipher, a technique of encoding messages which has been used for half a millenium. The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo Cardano in 1550.

Precondition: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)

How to improve this mission? https://github.com/Bryukh-Checkio-Tasks/checkio-task-cipher-map.git { 10 }
"""
import itertools

def recall_password(cipher_grille, ciphered_password):
    mask = [[1 if v == 'X' else 0 for v in row] for row in cipher_grille]
    password = ''
    for _ in range(4):
        password += decrypt(mask, ciphered_password)
        mask = rotate(mask)
    return password

def decrypt(mask, ciphered_password):
    return ''.join(itertools.compress(itertools.chain.from_iterable(ciphered_password), itertools.chain.from_iterable(mask)))

def rotate(table):
    return list(itertools.zip_longest(*[[v for v in row] for row in table[::-1]]))

"""
other solution
def recall_password(cipher_grille, ciphered_password):
    answer = []
    for t in range(4): # 4 times rotate
        #get password
        answer += ([ciphered_password[i][j] for i in range(4) for j in range(4) if cipher_grille[i][j] == "X"])
        #rotation
        cipher_grille = list(zip(*cipher_grille[::-1]))
    return ''.join(answer)
"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
