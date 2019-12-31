from random import random

file = open("words.txt")
word = file.read().split("\n")
word = list(word[int(random()*len(word))])
inv_word = list("-" * len(word))
wrong_count = 0
game_playing = True
word_backup = "".join(word)

while game_playing:
    print("\n")
    print("".join(inv_word))
    print("Wrong Count : " , wrong_count)

    char = input("Enter a letter : ")
    if char in word :
        while char in word:
            inv_word[word.index(char)] = char
            word[word.index(char)] = "-"
    
    else : 
        wrong_count += 1
    
    if wrong_count == 6 :
        print("\nGAME LOST.")
        print("WORD WAS : ", word_backup.upper())
        game_playing = False
    
    if "".join(inv_word).count("-") == 0 :
        print("\nGAME WON!")
        print("THE WORD WAS : ", "".join(inv_word).upper())
        game_playing = False
