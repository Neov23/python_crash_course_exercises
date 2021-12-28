# Άσκηση 10-10

filename = 'alexander_the_great.txt'

with open(filename, encoding='utf-8') as alexander_file:
    lines = alexander_file.read()
    i = lines.lower().count('the ')

print(i)
