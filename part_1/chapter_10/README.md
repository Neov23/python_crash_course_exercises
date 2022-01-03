# Files and Exceptions

- [Exercise 10-1](exercise_10_01/exercise_10_01.py):
Open a blank file in your text editor and write a few lines summarizing what
you've learned about Python so far. Start each line with the phrase In Python
you can... Save the file as learning_python.txt in the same directory as your
exercises from this chapter. Write a program that reads the file and prints
what you wrote three times. Print the contents once by reading in the entire
file, once by looping over the file object, and once by storing the lines in
a list and then working with them outside the with block.</br>
**Modules:**
  - [learning_python.txt](exercise_10_01/learning_python.txt)
</br>

- [Exercise 10-2](exercise_10_02/exercise_10_02.py):
You can use the replace() method to replace any word in a string with a
different word. Here's a quick example showing how to replace 'dog' with 'cat'
in a sentence:</br>
message = "I really like dogs."
message.replace('dog', 'cat')
'I really like cats.'</br>
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.</br>
**Modules:**
  - [learning_python.txt](exercise_10_02/learning_python.txt)
</br>

- [Exercise 10-3](exercise_10_03/exercise_10_03.py):
Write a program that prompts the user for their name. When they respond, write
their name to a file called guest.txt.</br>
**Modules:**
  - [guest.txt](exercise_10_03/guest.txt)
</br>

- [Exercise 10-4](exercise_10_04/exercise_10_04.py):
Write a while loop that prompts users for their name. When they enter their
name, print a greeting to the screen and add a line recording their visit in
a file called guest_book.txt. Make sure each entry appears on a new line in
the file.</br>
**Modules:**
  - [guest_book.txt](exercise_10_04/guest_book.txt)
</br>

- [Exercise 10-5](exercise_10_05/exercise_10_05.py):
Write a while loop that asks people why they like programming. Each time
someone enters a reason, add their reason to a file that stores all the
responses.</br>
**Modules:**
  - [reasons_to_love_programming.txt](exercise_10_05/reasons_to_love_programming.txt)
</br>

- [Exercise 10-6](exercise_10_06.py):
One common problem when prompting for numerical input occurs when people
provide text instead of numbers. When you try to convert the input to an int,
you’ll get a ValueError. Write a program that prompts for two numbers. Add
them together and print the result. Catch the TypeError if either input value
is not a number, and print a friendly error message. Test your program by
entering two numbers and then by entering some text instead of a number.
</br>

- [Exercise 10-7](exercise_10_07.py):
Wrap your code from Exercise 10-6 in a while loop so the user can continue
entering numbers even if they make a mistake and enter text instead of a
number.
</br>

- [Exercise 10-8](exercise_10_08/exercise_10_08.py):
Make two files, cats.txt and dogs.txt. Store at least three names of cats in
the first file and three names of dogs in the second file. Write a program that
tries to read these files and print the contents of the file to the screen.
Wrap your code ina try-except block to catch the FileNotFound error, and print
a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block executes
properly.</br>
**Modules:**
  - [cat.txt](exercise_10_08/cat.txt)
  - [dog.txt](exercise_10_08/dog.txt)
</br>

- [Exercise 10-9](exercise_10_09/exercise_10_09.py):
Modify your except block in Exercise 10-8 to fail silently if either file is
missing.</br>
**Modules:**
  - [cat.txt](exercise_10_08/cat.txt)
  - [dog.txt](exercise_10_08/dog.txt)
</br>

- [Exercise 10-10](exercise_10_10/exercise_10_10.py):
Visit Project Gutenberg (<https://gutenberg.org/>) and find a few texts you’d
like to analyze. Download the text files for these works, or copy the raw text
from your browser into a text file on your computer.</br>
You can use the count() method to find out how many times a word or phrase
appears in a string. For example, the following code counts the number of
times 'row' appers in a string:</br>
line = "Row, row, row your boat"
line.count('row')
2
line.lower().count('row')
3</br>
Notice that converting the string to lowercase using lower() catches all
appearances of the word you’re looking for, regardless of how it’s
formatted.</br>
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word ‘the’ appears in each text. This will be an
approximation because it will also count words such as ‘then’ and ‘tehre’. Try
counting ‘the ‘, with a space in the string, and see how much lower your count
is.</br>
**Modules:**
  - [alexander_the_great.txt](exercise_10_10/alexander_the_great.txt)
</br>

- [Exercise 10-11](exercise_10_11/README.md):
Write a program that prompts for the user’s favorite number. Use json.dump()
to store this number in a file. Write a separate program that reads in this
value and prints the message, “I know your favorite number! It’s _____.”
</br>

- [Exercise 10-12](exercise_10_12/exercise_10_12.py):
Combine the two programs from Exercise 10-11 into one file. If the number is
already stored, report the favorite number to the user. If not, prompt for the
user’s favorite number and store it in a file. Run the program twice to see
that it works.</br>
**Modules:**
  - [favorite_number.json](exercise_10_12/favorite_number.json)
**NOTE!** Above file does not exist, unless program is run at least once.
</br>

- [Exercise 10-13](exercise_10_13/exercise_10_13.py):
The final listing for remember_me.py assumes either that the user has already
entered their username or that the program is running for the first time. We
should modify it in case the current user is not the person who last used the
program.</br>
Before printing a welcome back message in greet_user(), ask the user if this
is the correct username. If it’s not, call get_new_username() to get the
correct username.</br>
**Modules:**
  - [username.json](exercise_10_13/username.json)
**NOTE!** Above file does not exist, unless program is run at least once.
