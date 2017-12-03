import string
import sys

text = "apple orange banana banana orange"
print("Вхідний текст:",text)

words = {} #dict
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for word in text.lower().split():
    word = word.strip(strip)
    if len(word) > 2:
        words[word] = words.get(word, 0) + 1

for i in sorted(words.items(), key=lambda x: (x[0])): #(i[0]-->keys, i[1]-->values)    
        if i[1] == max(words.values()):
            print("Слово '{0}' зустрічається найчастіше [{1}] і є найменшим в лексикографічному порядку".format(i[0],  max(words.values())))
            break

