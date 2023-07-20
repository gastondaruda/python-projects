def replace_word():
    str = "Hi guys, I am Tomi, hi hi hi"
    word_to_replace = input("Word to replace")
    word_replacement = input("Enter new word")
    if str.find(word_to_replace) == -1:
        print(f"La palabra {word_to_replace} no existe")
    else:
        print(str.replace(word_to_replace, word_replacement))
    
replace_word()