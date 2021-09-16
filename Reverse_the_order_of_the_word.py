# Reverse the order of the words in sentance
sentance=0
input_word = input()
input_word = input_word.split()
reverse_word=(" ".join(input_word[-1::-1]))
sentance=reverse_word.replace("defeated", "lost to")
print(sentance)


