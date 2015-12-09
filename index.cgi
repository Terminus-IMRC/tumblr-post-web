#!/usr/bin/env python3

import os.path, sys
from parts import *

print('Content-Type: text/html')
print('\r')

pbname = os.path.basename(sys.argv[0])

print(hh)
print('<h1> Tumblr / branch </h1>')
print('<form method="post" action="input.py">')

a = ['Text', 'Quote', 'Link', 'Chat']
for i in range(len(a)):
	if a[i] == 'Quote':
		checked_string = ' checked'
	else:
		checked_string = ''
	print('<input type="radio" id="r%d" name="type" value="%s"%s>' % (i, a[i].lower(), checked_string))
	print('<label for="r%d">%s</label>' % (i, a[i]))

print('<br><br>')
print('<input type="submit" value="Next">')
print('</form>')
print
print('</body>')
print('</html>')
