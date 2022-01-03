# Exercise 6-3

glossary = {
    'algorithm': 'A series of definite commands to execute',
    'comment': 'A comment that can be read only in the code',
    'integer': 'A number without any decimal',
    'variable': 'An argument that has a certain value',
    'loop': 'Self repeating'
    }

for variable in glossary:
    print(f"{variable.title()}: {glossary[variable]}.")