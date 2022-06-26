intro = input("Enter your introduction: ")
characterCount = 0
wordCount = 1
for i in intro:
    characterCount = characterCount + 1
    print(characterCount)
    if(i == " "):
        wordCount = wordCount + 1
print(intro)
print("numberOfWordCount")
print(wordCount)
print("numberOfChracterCount")
print(characterCount)