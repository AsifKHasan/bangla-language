#!/usr/bin/env python3
import fileinput

import ply.lex as lex
from ply.lex import TOKEN

tokens = ['BREAKER', 'DARI', 'CARET', 'type1_tokens']

conversion_map = {}

def build_conversion_map(file_path):
	for line in fileinput.input(file_path, openhook=fileinput.hook_encoded("utf-8")):
		line = line.strip()
		if line == '' or line.startswith('#'):
			continue

		pair = line.split(':')
		if len(pair) >= 1:
			syllable = pair[0].strip()
			mapped_value = ''

		if len(pair) >= 2:
			mapped_value = pair[1].strip()

		conversion_map[syllable] = mapped_value

build_conversion_map('./data/syllables')

tokens = tokens + [k for k in conversion_map]

def build_type1_tokens():
	s = r'('
	for k in conversion_map:
		s = s + k + r'|'

	s = s[:-1]
	s = s + r')'

	return s

type1_tokens = build_type1_tokens()

@TOKEN(type1_tokens)
def t_type1_tokens(t):
	t.value = conversion_map[t.value]
	return t

def t_BREAKER(t):
	r'\~'
	t.value = '\u200C'
	return t

def t_DARI(t):
	r'\.'
	t.value = '।'
	return t

def t_CARET(t):
	r'\^'
	t.value = 'ঁ'
	return t

# error handling rule
def t_error(t):
	print("Illegal character '{0}' at position {1}".format(t.value[0], t.lexpos))
	t.lexer.skip(1)

literals = "+-*/\ \t;:,@#$%&()[]{}!।?<>'_`"
