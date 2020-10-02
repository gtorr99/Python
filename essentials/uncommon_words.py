str1 = "Hello there! What's up?"
str2 = "Hello there! How are you?"

count = {}

for word in str1.split():
    count[word] = count.get(word, 0) + 1

for word in str2.split():
    count[word] = count.get(word, 0) + 1

print([word for word in count if count[word] == 1])

print(count)