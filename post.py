#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

sys.dont_write_bytecode = True

#import codecs

#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

import pytumblr
from info import *
from parts import *

import json
import cgi

import cgitb
cgitb.enable(display = 0, logdir = "/tmp")

print hh

form = cgi.FieldStorage()
ms = ''
if not form.has_key('type'):
	ms += ' type'
if not form.has_key('account'):
	ms += ' account'
if ms != '':
	print '<strong>error: missing field(s):%s</strong>' % ms
else:
	type = form.getfirst('type', '')
	account = form.getfirst('account', '')

	print '<h1> Tumblr posting page </h1>'

	if type == 'text':
		a = ['title', 'body']
	elif type == 'quote':
		a = ['quote', 'source']
	elif type == 'link':
		a = ['title', 'url', 'desc']
	elif type == 'chat':
		a = ['title', 'conv']
	else:
		print '<strong>error: unknown type: %s</strong>' % type

	if type == 'text' and ((not form.has_key('title')) or (not form.has_key('body'))):
		print '<strong>error: %s: fill at least a box</strong>' % (type)
	else:
		aa = []
		for i in range(len(a)):
			if form.has_key(a[i]):
				s = form.getfirst(a[i], '')
			else:
				s = ''
			aa.append(s)

		client = pytumblr.TumblrRestClient(ck, cs, oat, oas)

		if type == 'text':
			ret = client.create_text(account, state = 'published', title = aa[0], body = aa[1])
		elif type == 'quote':
			ret = client.create_quote(account, state = 'published', quote = aa[0], source = aa[1])
		elif type == 'link':
			ret = client.create_link(account, title = aa[0], url = aa[1], description = aa[2])
		elif type == 'chat':
			ret = client.create_chat(account, title = aa[0], conversation = aa[1])

		print '<br><br>'
		print '<a href="./">Go back</a>'
		print '<br><br>'

		postid = ret['id']
		postjson = client.posts(account, id = postid)
		url = postjson['posts'][0]['post_url'].decode('utf8').encode('utf8')
		url_short = postjson['posts'][0]['short_url'].decode('utf8').encode('utf8')

		print 'id = %d' % postid
		print '<br><br>'
		print '<a href="%s">%s</a>' % (url, url)
		print '<br><br>'
		print '<a href="%s">%s</a>' % (url_short, url_short)
		print '<br><br>'
		print '<pre>'
		print json.dumps(postjson, indent = 1)
		print '</pre>'

print ' </body>'
print '</html>'
