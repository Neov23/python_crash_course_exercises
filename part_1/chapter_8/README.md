# Functions

- [Exercise 8-1](exercise_08_01.py):
Write a function called display_message() that prints one sentence telling
everyone what you are learning about in this chapter. Call the function, and
make sure the message displays correctly.
</br>

- [Exercise 8-2](exercise_08_02.py):
Write a function called favorite_book() that accepts one parameter, title. The
function should print a message, such as One of my favorite books is Alice in
Wonderland. Call the function, making sure to include a book title as an
argument in the function call.
</br>

- [Exercise 8-3](exercise_08_03.py):
Write a function called make_shirt() that accepts a size and the text of a
message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.</br>
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
</br>

- [Exercise 8-4](exercise_08_04.py):
Modify the make_shirt() function so that shirts are large by default with a
message that reads I love Python. Make a large shirt and a medium shirt with
the default message, and a shirt of any size with a different message.
</br>

- [Exercise 8-5](exercise_08_05.py):
Write a function called describe_city() that accepts the name of a city and
its country. The function should print a simple sentence, such as Reykjavik is
in Iceland. Give the parameter for the country a default value. Call your
function for three different cities, at least one of which is not in the
default country.
</br>

- [Exercise 8-6](exercise_08_06.py):
Write a function called city_country() that takes in the name of a city and
its country. The function should return a string formatted like this:</br>
"Santiago, Chile"</br>
Call your function with at least three city-country pairs, and print the value
that's returned.
</br>

- [Exercise 8-7](exercise_08_07.py):
Write a function called make_album() that builds a dictionary describing a
music album. The function should take in an artist name and an album title,
and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album
information correctly.</br>
Add an optional parameter to make_album() that allows you to store the nubmer
of tracks on an album. If the calling line includes a value for the number of
tracks, add that value to the album's dictionary. Make at least one new
function call that includes the nubmer of tracks on an album.
</br>

- [Exercise 8-8](exercise_08_08.py):
Start with your program from Exercise 8-7. Write a while loop that allows
users to enter an album's artist and title. Once you have that information,
call make_album() with the user's input and print the dictionary that's
created. Be sure to include a quit value in the while loop.
</br>

- [Exercise 8-9](exercise_08_09.py):
Make a list containing a series of short text messages. Pass the list to a
function called show_messages(), which prints each text message.
</br>

- [Exercise 8-10](exercise_08_10.py):
Start with a copy of your program from Exercise 8-9. Write a function called
send_messages() that prints each text message and moves each message to a new
list called sent_messages as it's printed. After calling the function, print
both of your lists to make sure the messages were moved correctly.
</br>

- [Exercise 8-11](exercise_08_11.py):
Start with your work from Exercise 8-10. Call the function send_messages()
with a copy of the list of messages. After calling the function, print bot
 of your lists to show that the original list has retained its messages.
</br>

- [Exercise 8-12](exercise_08_12.py):
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the
function call provides, and it should print a summary of the sandiwch that is
being ordered. Call the function three tiems, using a different number of
arguments each time.
</br>

- [Exercise 8-13](exercise_08_13.py):
Start with a copy of "*user_profile*.*py*". Create a profile for yourself,
by calling the function "build_profile()", using your name, your last name
three other value-key pairs that describe you.
</br>

- [Exercise 8-14](exercise_08_14.py):
Write a function that stores information about a car in a dictionary. the
function should always receive a manufacturer and a model name. It should then
accept an arbitrary number of keyword arguments. Call the function with the
required information and two other name-value pairs, such as a color or an
optional feature. Your function should work for a call like this one:</br>
car = make_car('subaru', 'outback', color='blue', tow_package=True)</br>
Print the dictionary that's returned to make sure all the information was
stored correctly.
</br>

- [Exercise 8-15](exercise_08_15/exercise_08_15.py):
Put the functions for the example printing_models.py in a separate file called
printing_functions.py. Write an import statement at the top of
printing_models.py, and modify the file to use the imported functions.</br>
**Modules:**
  - [printing_functions.py](exercise_08_15/printing_functions.py)
