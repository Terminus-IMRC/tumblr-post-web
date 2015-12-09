#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

sys.dont_write_bytecode = True

#import codecs

#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

from parts import *
from info import *

import cgi

import cgitb
cgitb.enable(display = 0, logdir = "/tmp")

print hh

form = cgi.FieldStorage()
ms = ''
if not form.has_key('type'):
	ms += ' type'
if ms != '':
	print '<strong>error: missing field(s):%s</strong>' % ms
else:
	type = form.getfirst('type', '')

	print '<h1> Tumblr posting page / input </h1>'
	print '<form method="post" action="post.py">'
	print '<input type="hidden" name="type" value="%s">' % type

	if type == 'text':
		print 'Title:'
		print '<br>'
		print '<input type="text" name="title">'
		print '<br>'
		print 'Body:'
		print '<br>'
		print '<textarea name="body"></textarea>'
		print '<br>'
	elif type == 'quote':
		print 'Quote:'
		print '<br>'
		print '<textarea name="quote" required="required"></textarea>'
		print '<br>'
		print 'Source:'
		print '<br>'
		print '<input type="text" name="source">'
		print '<br>'
	elif type == 'link':
		print 'Title:'
		print '<br>'
		print '<input type="text" name="title">'
		print '<br>'
		print 'URL:'
		print '<input type="text" name="url" required="required">'
		print '<br>'
		print 'Desc:'
		print '<textarea name="desc"></textarea>'
		print '<br>'
	elif type == 'chat':
		print 'Title:'
		print '<br>'
		print '<input type="text" name="title">'
		print '<br>'
		print 'Conv:'
		print '<br>'
		print '<textarea name="conv" required="required"></textarea>'
		print '<br>'
	else:
		print '<strong>error: unknown type: %s</strong>' % type

	print '<br>'

	a = accounts
	for i in range(len(a)):
		if i == 0:
			checked_string = ' checked'
		else:
			checked_string = ''
		print '<input type="radio" id="r2-%d" name="account" value="%s"%s>' % (i, a[i], checked_string)
		print '<label for="r2-%d">%s</label>' % (i, a[i])

	print '<br>'
	print '<br>'

	print '<input type="submit" value="post">'

	print '</form>'

print ' </body>'
print '</html>'
