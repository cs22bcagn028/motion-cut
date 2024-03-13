def word_count(sentence):
    if(sentence == ""):
        return 0
    wordsList = sentence.split(" ") # this will convert the string into a list with each word as an element in the list. All because of the delimeter " " (space) 
    return len(wordsList)

inputSentence = input("Enter any sentence \n")

if(word_count(inputSentence) == 0):
    print("Invalid input! You must enter some string to check the working of the program :)")
else:
    print(f"number of words : {word_count(inputSentence)}")
