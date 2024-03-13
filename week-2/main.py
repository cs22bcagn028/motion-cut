def word_count(sentence):
    wordsList = sentence.split(" ")
    return len(wordsList)

inputSentence = input("Enter any sentence \n")
print(f"number of words : {word_count(inputSentence)}")
