"""
This program works as a dictionary for words or phrases that is saved
within the dictionary. Follow the printed commands to to translate, print
all the words or even add new ones
"""

def main():

    #The english dicitionary
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    #The spanish dictionary
    spanish_english = {"casa": "home", "gracias": "thanks", "hola": "hey"}
    print("Dictionary contents: ")
    # prints the key contents of the dict in every loop.
    print(", ".join(sorted(english_spanish.keys())))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")

            if word not in english_spanish:
                print("The word", word, "could not be found from "
                                        "the dictionary.")
            else:
                print(f"{word} in Spanish is {english_spanish[word]}")

        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            new_word = {english_word: spanish_word}
            new_word2 = {spanish_word: english_word}
            english_spanish.update(new_word)
            spanish_english.update(new_word2)
            print("Dictionary contents: ")
            print(", ".join(sorted(english_spanish.keys())))

        elif command == "R":
            removed_word = input("Give the word to be removed: ")
            if removed_word not in english_spanish:
                print("The word", removed_word, "could not be found from "
                                        "the dictionary.")
            else:
                del english_spanish[removed_word]
        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()
            print("Spanish-English")
            for word2 in sorted(spanish_english):
                print(word2, spanish_english[word2])
            print()
        elif command == "T":

            txt = input("Enter the text to be translated into Spanish: ")
            lst = txt.split(" ")
            lst2 = []

            #Created a loop to replace the list entry with the new entry from
            #the dictionary, and place them all into a new list then printing
            #out the new one.
            for i in range(len(lst)):
                #if the str from the lst in the dict, replace the old with new
                if lst[i] in english_spanish:
                    new_txt = lst[i].replace(lst[i], english_spanish[lst[i]])
                #If not in dict, return the old lst entry. Made this to avoid
                #dict error.
                elif lst[i] not in english_spanish:
                    new_txt = lst[i]
                lst2.append(new_txt)
            print("The text, translated by the dictionary: ")
            print(' '.join(lst2))


        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")



if __name__ == "__main__":
    main()
