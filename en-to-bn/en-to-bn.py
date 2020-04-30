#!/usr/bin/env python3
'''
usage:
cat ./test/moby-dick | python en-to-bn.py > ./out/out.txt
python rules-from-gsheet.py && cat ./test/moby-dick | python en-to-bn.py > ./out/out.txt

cat ./test/moby-dick | python3 en-to-bn.py > ./out/out.txt
python3 rules-from-gsheet.py && cat ./test/moby-dick | python3 en-to-bn.py > ./out/out.txt
'''

import sys
import fileinput

import ply.lex as lex
import token_rules
import re
import unicodedata

def unicode_data(u):
	for i, c in enumerate(u):
		print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
		print(unicodedata.name(c))

def post_process(text):
	r = '\u09CD'
	s = re.compile('\u09CD' + '\u09CD+')
	text = s.sub(r, text)

	r = ''
	s = re.compile('\u09CD' + 'অ')
	text = s.sub(r, text)

	r = '\u09BE'
	s = re.compile('\u09CD' + 'আ')
	text = s.sub(r, text)

	r = '\u09BF'
	s = re.compile('\u09CD' + 'ই')
	text = s.sub(r, text)

	r = '\u09C0'
	s = re.compile('\u09CD' + 'ঈ')
	text = s.sub(r, text)

	r = '\u09C1'
	s = re.compile('\u09CD' + 'উ')
	text = s.sub(r, text)

	r = '\u09C2'
	s = re.compile('\u09CD' + 'ঊ')
	text = s.sub(r, text)

	r = '\u09C3'
	s = re.compile('\u09CD' + 'ঋ')
	text = s.sub(r, text)

	r = '\u09C7'
	s = re.compile('\u09CD' + 'এ')
	text = s.sub(r, text)

	r = '\u09C8'
	s = re.compile('\u09CD' + 'ঐ')
	text = s.sub(r, text)

	r = '\u09CB'
	s = re.compile('\u09CD' + 'ও')
	text = s.sub(r, text)

	r = '\u09CC'
	s = re.compile('\u09CD' + 'ঔ')
	text = s.sub(r, text)

	r = ''
	s = re.compile('\u09CD' + '\u200C')
	text = s.sub(r, text)

	# r = '\g<name>'
	# s = re.compile('\u09CD' + '(?P<name> [ ;ঃ,।:;.,])')
	# text = s.sub(r, text)

	r = ' '
	s = re.compile('\u09CD' + ' ')
	text = s.sub(r, text)

	r = '-'
	s = re.compile('\u09CD' + '-')
	text = s.sub(r, text)

	r = ';'
	s = re.compile('\u09CD' + ';')
	text = s.sub(r, text)

	r = ':'
	s = re.compile('\u09CD' + ':')
	text = s.sub(r, text)

	r = ','
	s = re.compile('\u09CD' + ',')
	text = s.sub(r, text)

	r = '।'
	s = re.compile('\u09CD' + '।')
	text = s.sub(r, text)

	r = '?'
	s = re.compile('\u09CD' + '\?')
	text = s.sub(r, text)

	r = '\t'
	s = re.compile('\u09CD' + '\t')
	text = s.sub(r, text)

	r = ''
	s = re.compile('\u09CD$')
	text = s.sub(r, text)

	r = '\u09CD\u200C'
	s = re.compile('\u09CD' + '`')
	text = s.sub(r, text)

	# r = '\u09CE'
	# s = re.compile('ত' + '\u09CD+')
	# text = s.sub(r, text)

	return text

class EnParser(object):

	token_list = []

	def __init__(self, **kwargs):
		# bild the lexer
		self.lexer = lex.lex(module=token_rules, **kwargs)

	def run(self, data):
		self.token_list = []
		self.lexer.input(data)
		while True:
			tok = self.lexer.token()
			if not tok:
				break

			self.token_list.append(tok.value)

		s = ''.join(self.token_list)
		s = post_process(s)
		print(s.encode('utf-8').decode(sys.stdout.encoding))
		# print(s)

if __name__ == '__main__':
	en_parser = EnParser()
	for line in fileinput.input():
		line = line.rstrip()
		if line == '!q':
			sys.exit(0)

		if line.startswith('#'):
			continue

		en_parser.run(line)
