sentence = input("enter the paragraph: ")

dictionary = []

for word in sentence:
    
    count = 0
    for i in range(0,len(dictionary)):
        if word == dictionary[i]:
            count += 1

    if count < 1:
        dictionary.append(word)

print(dictionary)
