#zadanie palindromy
#plan:
#1. funkcja sprawdzajaca czy slowo jest palindromem
#na razie to slowo bedzie wpiswywane na sztywno w kodzie

test_words = [
    "Kajak",
    "A to kanapa pana Kota",
    "Python",
    "Anna",
    "Kobyła ma mały bok!",
    "To nie jest palindrom"
]
print(f"Testowane słowa to: {test_words}")
def is_palindrome(word):
    new_word = "" #tu będziemy składać słowo
    for char in word: # przechodzimy przez każdą literę w słowie
        if char.isalnum(): #sprawdzamy czy znak jest alfanumeryczny (litera lub cyfra)
            new_word += char.lower()  # zamiana na małe litery, by "A" i "a" były równe
    reversed_word = new_word[::-1] #odwracamy słowo
    return new_word == reversed_word # porównujemy oryginalne słowo z odwróconym

print("\n--- Testowanie funkcji is_palindrome ---\n")
for test_word in test_words:
    if is_palindrome(test_word):
        print(f'"{test_word}" jest palindromem.\n')
    else:
        print(f'"{test_word}" nie jest palindromem.\n')
