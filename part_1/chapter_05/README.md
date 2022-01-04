# if Statements

- [Exercise 5-1](exercise_05_01.py):
Write and check a few conditions. Display a statement that will describe each
check and your bypass for the results check. Your code should look like
this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

  - Check carefully your results and confirm that you understand why each line
is valued as True or False
  - Create at least 10 conditions. Value at least five of them as "True" and
the other five conditions as "False".

- [Exercise 5-2](exercise_05_02.py):
You don't have to limit the number of conditional checks to ten. If you want
to try more conditional checks, write more conditions. Create at least one
"True" and one "False" for each of the conditions:

  - Check equality and inequality in strings.
  - Check with "lower()" method.
  - Numeric checks that include equality **and** inequality.
  - Check with keywords "and" and "or".
  - Check if an element is part of a list.
  - Check if an element is not part of a list.

- [Exercise 5-3](exercise_05_03.py):
Imagine an alien was just shot down in a game. Create a variable called
alien_color and assign it a value of 'green', 'yellow', or 'red'.

  - Write an if statement to test whether the alien’s color is green. If it is,
print a message that the player just earned 5 points.
  - Write one version of this program that passes the if test and another tha
fails. (The version that fails will have no output.)

- [Exercise 5-4](exercise_05_04.py):
Choose a color for an alien as you did in Exercise 5-3, and write an if-else
chain.

  - If the alien’s color is green, print a statement that the player just
earned 5 points for shooting the alien.
  - If the alien’s color isn’t green, print a statement that the player just
earned 10 points.
  - Write one version of this program that runs the if block and another that
runs the else block.

- [Exercise 5-5](exercise_05_05.py):
Turn your if-else chain from Exercise 5-4 into an if-elif-else cahin.

  - If the alien is green, print a message that the player earned 5 points.
  - If the alien is yellow, print a message that the player earned 10 points.
  - If the alien is red, print a message that the player earned 15 points.
  - Write three versions of this program, making sure each message is printed
for the appropriate color alien.

- [Exercise 5-6](exercise_05_06.py):
Write an if-elif-else cahin that determines a person’s stage of life. Set a
value for the variable age, and then:

  - If the person is less than 2 years old, print a message that the person is
a baby.
  - If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
  - If the person is at least 4 years old but less than 13, print a message
that the person is a kid.
  - If the person is at least 13 years old but less than 20, print a message
that the person is a teen.
  - If the person is at least 20 years old but less than 65, print a message
that the person is a adult.
  - If the person is age 65 or older, print a message that the person is an
elder.

- [Exercise 5-7](exercise_05_07.py):
Make a list of your favorite fruits, and then write a series of independent if
statements that check for certain fruits in your list.

  - Make a list of your three favorite fruits and call it favorite_fruits.
  - Write five if statements. Each should check whether a certain kind of
fruit is in your list. If the fruit is in your list, the if block should print
a statement, such as "You really like bananas!"

- [Exercise 5-8](exercise_05_08.py):
Make a list of five or more usernames, including the name 'admin'. Imagine you
are writing code that will print a greeting to each user after they log in to
a website. Loop through the list, and print a greeting to each user:

  - If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
  - Otherwise, print a generic greeting, such as Hello Eric, thank you for
loggin in again.

- [Exercise 5-9](exercise_05_09.py):
Add an if test to hello_admin.py to make sure the list of users is not empty.

  - If the list is empty, print the message We need to find some users!
  - Remove all of the usernames from your list, and make sure the correct
message is printed.

- [Exercise 5-10](exercise_05_10.py):
Do the following to create a program that simulates how websites ensure that
everyone has a unique username.

  - Make a list of five or more usernames called current_users. Make another
list of five usernames called new_users. Make sure one or two of the new
usernames are also in the current_users list.
  - Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a new
username. If a username has not been used, print a message saying that the
username is available.
  - Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.

- [Exercise 5-11](exercise_05_11.py):
Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most
ordinal numbers end in th, except 1, 2, and 3.

  - Store the numbers 1 through 9 in a list.
  - Loop through the list.
  - Use an if-elif-else chain inside the loop to print the proper ordinal
ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
8th 9th", and each result should be on a separate line.
