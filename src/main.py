from zyjared.color import Color
from zyjared.fs import clean_directory

print(f'{Color("Hello World!").red().bold()}')

removed = clean_directory('.', ['.*tempCodeRunnerFile.py'], ['.*__pycache__'])
print(removed)