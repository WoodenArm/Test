import os

name = 'Микола'
filename = f'{name}.txt'
with open(filename, 'w') as file_object:
    filename = os.path.join('retro', 'cheatsheet.txt')
    with open(filename) as f:
        string = f.read()
    string = file_object.write(string)