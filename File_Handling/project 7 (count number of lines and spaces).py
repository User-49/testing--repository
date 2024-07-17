file = open('Project 7_text_file.txt', 'r')
text = file.readlines()
spaces = 0
lines = len(text)
for i in text:
    for k in i:
        spaces += k.count(' ')
print('Number of spaces in text: ', spaces)
print('Number of lines in text: ', lines)
