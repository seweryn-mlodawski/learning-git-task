#zadanie palindromy
#plan:
#1. funkcja sprawdzajaca czy slowo jest palindromem
#na razie to slowo bedzie wpiswywane na sztywno w kodzie
word = "Alejaja"
reversed_word = word[::-1] #odwracamy slowo
print(reversed_word)

def is_palindrome(word):
    new_word = "" # tutaj bedziemy trzymac slowo
    for char in word:
        if char.isalnum(): #sprawdzamy czy znak jest alfanumeryczny
            new_word += char
    reversed_word = new_word[::-1] #odwracamy slowo
    return new_word == reversed_word
