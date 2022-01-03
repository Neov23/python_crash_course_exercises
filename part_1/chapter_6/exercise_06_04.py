# Exercise 6-4 (Copy/Paste from 6-3, since it still applies as solution here)

glossary = {
    'algorithm': 'A series of definite commands to execute',
    'comment': 'A comment that can be read only in the code',
    'integer': 'A number without any decimal',
    'variable': 'An argument that has a certain value',
    'loop': 'Self repeating'
    }

for variable in glossary:
    print(f"{variable.title()}: {glossary[variable]}.")