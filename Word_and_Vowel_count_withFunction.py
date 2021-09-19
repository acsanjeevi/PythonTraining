data=0
file = open("file_read_program.txt", "rt")

def Word_and_vowel_count():
    data = file.read()
    print('Number of words in text file :', len(data))
    vowel_count =  0
    for i in data:
        if(i=='a'):
             vowel_count +=1
             print("Total Number of Vowel 'a' = ", vowel_count)
Word_and_vowel_count()
