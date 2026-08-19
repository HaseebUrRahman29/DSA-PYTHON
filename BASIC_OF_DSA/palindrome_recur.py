#CHECK IF A STRING IS PALINDROME
word="racecar"
first_character=0
last_num=len(word)
last_character=last_num-1
def pali(word,first_character,last_character):
    if first_character>=last_character:
        return True
    if word[first_character] != word[last_character]:
        return False
    return pali(word,first_character+1,last_character-1)

print(pali(word,first_character,last_character))