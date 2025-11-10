#zadanie palindromy
#plan:
#1. funkcja sprawdzajaca czy slowo jest palindromem
#na razie tekst bedzie wpiswywany na sztywno w kodzie

test_words = [
    "Kajak",
    "A to kanapa pana Kota",
    "Python",
    "Anna",
    "Kobyła ma mały bok!",
    "To nie jest palindrom"
]
print(f"\nTestowane słowa to: {test_words}")
def is_palindrome(word):
    """
    Funkcja sprawdza, czy tekst jest palindromem,
    ignoruje wielkość liter oraz znaki niebędące literami/cyframi.
    Argumenty:
        word (str): tekst do sprawdzenia (może zawierać spacje, interpunkcję, cyfry)
    Zwraca:
        bool: TRUE jeśli tekst jest palindromem, FALSE jeśli nie jest
    """
    new_word = ""                       #tu będziemy składać słowo
    for char in word:                   # przechodzimy przez każdą literę w słowie
        if char.isalnum():              #sprawdzamy czy znak jest alfanumeryczny (litera lub cyfra) - dzięki temu zignorujemy wykrzykniki, spacje itp.
            new_word += char.lower()    # zamiana na małe litery, by "A" i "a" były równe
    reversed_word = new_word[::-1]      #odwracamy słowo 
    return new_word == reversed_word    # porównujemy oryginalne słowo z odwróconym

print("\n--- Testowanie funkcji is_palindrome ---\n")
for test_word in test_words:            #iterujemy przez testowane słowa
    if is_palindrome(test_word):        #wywołujemy funkcję i sprawdzamy wynik
        print(f'"{test_word}" jest palindromem.\n')
    else:
        print(f'"{test_word}" NIE jest palindromem.\n')