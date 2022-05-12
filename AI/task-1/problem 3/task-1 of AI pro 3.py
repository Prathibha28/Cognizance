from collections import Counter
sentence = ""
file = open("about.txt", "r")
data = file.read()

for txt in data:
    if txt=="," or txt ==".":
        pass
    else:
        sentence+=txt
words = sentence.split(" ")

count = len(words)
counting = Counter(words)
for i in range(0,len(words)):
    if len(words[i]) >= 6:
        print(words[i])
print("Number of words present in given file: " + str(count))

list_of_word_and_frequency = counting.most_common()
print("Most frequently used word in Text File is ", counting.most_common()[0][0])
file.close()
