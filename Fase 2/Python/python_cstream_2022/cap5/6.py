f = open("c:\\Users\\enriq\\python_cstream_2022\\cap5\\passwords.txt", "rt")
content = f.read()
f.close()

#print(type(content))
word_list = content.split("\n")
#print(word_list)

list_of_words_with_e = []
for word in word_list:
    if "e" in word:
        list_of_words_with_e.append(word.upper())

print(list_of_words_with_e, len(list_of_words_with_e))

