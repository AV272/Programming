# Поиск шаблонов
import re
 
text = "The ants go marching one by one"
 
strings = ['the', 'one']
 
for string in strings:
    match = re.search(string, text) # поиск совпадений
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span() # начальная и конечная позиция совпавшей строки
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))
