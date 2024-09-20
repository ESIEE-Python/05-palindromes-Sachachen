"""op"""
#### Fonction secondairefrom
import string
def ispalindrome(p):
    """op"""
    # votre code ici
    # s = ''.join(map(chr, p))
    palindrome = False
    s = p.lower()
    table = str.maketrans("çéèêàôë","ceeeaoe")
    s = s.replace(" ", "")
    table1 = s.maketrans('', '', string.punctuation)
    s = s.translate(table).translate(table1)
    if s[::-1]== s :
        palindrome = True
    return palindrome

#### Fonction principale


def main():
    """j"""
    # vos appels à la fonction secondaire ici

    for s in ["Radar", "kayak", "levél", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
