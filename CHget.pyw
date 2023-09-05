import pyperclip

pyperclip.copy('''import sys\nsys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf8', closefd=False)''')