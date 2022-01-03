# Exercise 10-10

filename = 'alexander_the_great.txt'

with open(filename, encoding='utf-8') as alexander_text:
    whole_text = alexander_text.read()
    word_counter = whole_text.lower().count('the ')

print(f"The 'alexander_the_great.txt' file has the word 'the' written "
      f"{word_counter} times.")