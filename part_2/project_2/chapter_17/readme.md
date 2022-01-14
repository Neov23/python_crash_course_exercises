# Working with APIs

- [Exercise 17-1](exercise_17_01.py):
Modify the API call in python_repos.py so it generates a chart showing the
most popular projects in other languages. Try languages such as JavaScript,
Ruby, C, Java, Perl, Haskell, and Go.

- [Exercise 17-2](exercise_17_02.py):
Using the data from hn_submissions.py, make a bar chart showing the most
active discussions currently happening on Hacker News. The height of each bar
should correspond to the number of comments each submission has. The label for
each bar should include the submission’s title and should act as a link to the
discussion page for that submission.

- [Exercise 17-3](exercise_17_03/exercise_17_03.py):
In python_repos.py, we printed the value of status_code to make sure the API
call was successful. Write a program called test_python_repos.py that uses
unittest to assert that the value of status_code is 200. Figure out some other
assertions you can make — for example, that the number of items returned is
expected and that the total number of repositories is greater than a certain
amount.
**Modules:**
  - [python_repos.py](exercise_17_03/python_repos.py)
