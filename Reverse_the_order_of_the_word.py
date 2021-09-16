# Reverse the order of the words in sentance
sentance=0
reverse_word = input()
reverse_word = reverse_word.split()
x=(" ".join(reverse_word[-1::-1]))
sentance=x.replace("defeated", "lost to")
print(sentance)


