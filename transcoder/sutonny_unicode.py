#!/usr/bin/env python3

import sys
from plex import *

N0				= Str('\x30')
N1				= Str('\x31')
N2				= Str('\x32')
N3				= Str('\x33')
N4				= Str('\x34')
N5				= Str('\x35')
N6				= Str('\x36')
N7				= Str('\x37')
N8				= Str('\x38')
N9				= Str('\x39')

A				= Str('\x49')
I				= Str('\x41')
II				= Str('\x42')
U				= Str('\x43')
UU				= Str('\x44')
REE				= Str('\x45')
E				= Str('\x46')
AI				= Str('\x47')
O				= Str('\x48', '\x53')
AU				= Str('\x40')

_AA				= '\x4A'
_I				= '\x4B'
_II				= '\x4C'
_U1				= '\x4D'
_U2				= '\xE1'
_U3				= '\u0394'
_U4				= '\u2206'
_UU1			= '\x4E'
_UU2			= '\xEB'
_UU3			= '\u2021'
_REE1			= '\x4F'
_REE2			= '\xED'
_E1				= '\x50'
_E2				= '\xDF'
_AI1			= '\x51'
_AI2			= '\u2030'
_AU				= '\x52'

KA				= Str('\x54')
KHA				= Str('\x55')
GA				= Str('\x56')
GHA				= Str('\x57')
NGA				= Str('\x58')
CA				= Str('\x59')
CHA				= Str('\x5A')
JA				= Str('\x5C')
JHA				= Str('\x5E')
NYA				= Str('\x00')
TTA				= Str('\x61')
TTHA			= Str('\x62')
DDA				= Str('\x63')
DDHA			= Str('\x64')
NNA				= Str('\x65')
TA				= Str('\x66')
THA				= Str('\x67')
DA				= Str('\x68')
DHA				= Str('\x69')
NA				= Str('\x6A')
PA				= Str('\x6B')
PHA				= Str('\x6C')
BA				= Str('\x6D')
BHA				= Str('\x6E')
MA				= Str('\x6F')
YA				= Str('\x70')
RA				= Str('\x72')
LA				= Str('\x75')
SHA				= Str('\x76')
SSA				= Str('\x77')
SA				= Str('\x78')
HA				= Str('\x79')
RRA				= Str('\x7A')
RHA				= Str('\x7C')
YYA				= Str('\x7E')

ANUSVARA		= Str('\xC4')
VISARGA			= Str('\u201D')
CHANDRABINDU	= '\xC5'
KHANDATA		= Str('\u201C')
HASANT			= Str('\x26')

KA_KA			= Str('\xD1')
KA_TTA			= Str('\xD6')
KA_TA			= Str('\xDC')
KA_MA			= Str('\x00')
KA_RA			= Str('\xE2')
KA_SSA			= Str('\xE3')
KA_SSA_MA		= Str('\xE7')
KA_SA			= Str('\xE9')
GA_GA			= Str('\x00')
GA_DA			= Str('\x00')
GA_DHA			= Str('\xEA')
NGA_KA			= Str('\xEF')
NGA_KHA			= Str('\u2044')
NGA_GA			= Str('\xF1')
CA_CA			= Str('\xF3')
CA_CHA			= Str('\xF2')
JA_JA			= Str('\xF6')
JA_JHA			= Str('\x00')
JA_NYA			= Str('\xF9')
NYA_CA			= Str('\xFB')
NYA_CHA			= Str('\x00')
NYA_JA			= Str('\u2020')
NYA_JHA			= Str('\u0192')
TTA_TTA			= Str('\xA2')
DDA_DDA			= Str('\x60')
NNA_TTA			= Str('\xB5')
NNA_TTHA		= Str('\xA3')
NNA_DDA			= Str('\xA7')
TA_TA			= Str('\u2022')
TA_THA			= Str('\u2122')
TA_MA			= Str('\xAE')
TA_RA			= Str('\xA9')
DA_DA			= Str('\xA8')
DA_DHA			= Str('\u2260')
DA_BA			= Str('\xC6')
DA_BHA			= Str('\xD8')
DA_MA			= Str('\u221E')
DHA_BA			= Str('\xB1')
NA_TA			= Str('\u2202')
NA_TA_RA		= Str('\u03C0')
NA_TTHA			= Str('\x00')
NA_DDA			= Str('\x00')
NA_DHA			= Str('\xBA')
NA_THA			= Str('\u222B')
NA_DA			= Str('\xAA')
NA_SA			= Str('\xBF')
PA_TTA			= Str('\xA1')
PA_TA			= Str('\xAC')
PA_PA			= Str('\u221A')
PA_SA			= Str('\u2248')
BA_JA			= Str('\x00')
BA_DA			= Str('\xBB')
BA_DHA			= Str('\u2026')
BA_BA			= Str('\xE6')
BHA_RA			= Str('\xC3')
MA_MA			= Str('\xFF')
MA_NA			= Str('\xD5')
MA_PHA			= Str('\u0153')
MA_PA			= Str('\u0152')
MA_BA			= Str('\u2019')
MA_BHA			= Str('\xF7')
MA_LA			= Str('\u0178')
LA_KA			= Str('\u2039')
LA_GA			= Str('\u203A')
LA_TTA			= Str('\uFB01')
LA_DDA			= Str('\x00')
LA_PA			= Str('\xB7')
LA_PHA			= Str('\x00')
SHA_CA			= Str('\xC1')
SHA_CHA			= Str('\xF1')
SSA_KA			= Str('\xCF')
SSA_KA_RA		= Str('\u2018')
SSA_TTA			= Str('\xD3')
SSA_TTHA		= Str('\xD4')
SSA_NNA			= Str('\xCC')
SSA_PA			= Str('\uf8ff')
SSA_PHA			= Str('\xD2')
SSA_MA			= Str('\xDA')
SA_KA			= Str('\xDB')
SA_KHA			= Str('\x00')
SA_TTA			= Str('\u02C6')
SA_TA			= Str('\u02DC')
SA_TA_RA		= Str('\u02D8')
SA_THA			= Str('\u02D9')
SA_NA			= Str('\u02DA')
SA_PA			= Str('\xB8')
SA_PHA			= Str('\xB0')
SA_BA			= Str('\u02DD')
SA_MA			= Str('\u02DB')
HA_NA			= Str('\xFD', '\xA4')
HA_BA			= Str('\xF8')
HA_MA			= Str('\xAF')
RRA_GA			= Str('\x00')

_KA				= '\x8B'
_KA_RA			= '\x8C'
_TA				= '\x8F'
_TA_U			= '\x91'
_TA_RA			= '\x90'
_THA			= '\x92'
_NA				= '\xFA'
_PA				= '\x95'
_BA1			= '\xF4'
_BA2			= '\xF5'
_BHA			= '\xA2'
_BHA_RA			= '\xA3'
_MA				= '\xEC'
_YA				= '\x71'
_RA1			= '\x73'
_RA2			= '\xB4'
_RA3			= '\u2211'
_LA1			= '\xE4'
_LA2			= '\xEE'

NGA_			= Str('\u2013')
#CA_				= Str('\x94')
DA_				= Str('\x08')
#NA_				= Str('\x9A')
#PA_				= Str('\xFA')
#BA_				= Str('\x9F')
#MA_				= Str('\xA4')
RA_				= '\x74'
#SSA_			= Str('\xAE')
#SA_				= Str('\xAF')

GA_U			= Str('\xE8')
RA_U			= Str('\xC0')
RA_UU			= Str('\u201E')
SHA_U			= Str('\xCA')
HA_REE			= Str('\xC2')
HA_U			= Str('\xC9')

USCORE			= Str('\xD0')
DASH			= Str('\x2D', '\u220F')
LS_QUOTE		= Str('\xC8')
RS_QUOTE		= Str('\x27')
LD_QUOTE		= Str('\xCD')
RD_QUOTE		= Str('\x00')

DARI			= Str('\xC7')

U_CONJUNCT		= '\u09CD'

U_N0			= '\u09E6'
U_N1			= '\u09E7'
U_N2			= '\u09E8'
U_N3			= '\u09E9'
U_N4			= '\u09EA'
U_N5			= '\u09EB'
U_N6			= '\u09EC'
U_N7			= '\u09ED'
U_N8			= '\u09EE'
U_N9			= '\u09EF'

U_A				= '\u0985'
U_AA			= '\u0986'
U_I				= '\u0987'
U_II			= '\u0988'
U_U				= '\u0989'
U_UU			= '\u098A'
U_REE			= '\u098B'
U_LEE			= '\u098C'
U_E				= '\u098F'
U_AI			= '\u0990'
U_O				= '\u0993'
U_AU			= '\u0994'

U_KA			= '\u0995'
U_KHA			= '\u0996'
U_GA			= '\u0997'
U_GHA			= '\u0998'
U_NGA			= '\u0999'
U_CA			= '\u099A'
U_CHA			= '\u099B'
U_JA			= '\u099C'
U_JHA			= '\u099D'
U_NYA			= '\u099E'
U_TTA			= '\u099F'
U_TTHA			= '\u09A0'
U_DDA			= '\u09A1'
U_DDHA			= '\u09A2'
U_NNA			= '\u09A3'
U_TA			= '\u09A4'
U_THA			= '\u09A5'
U_DA			= '\u09A6'
U_DHA			= '\u09A7'
U_NA			= '\u09A8'
U_PA			= '\u09AA'
U_PHA			= '\u09AB'
U_BA			= '\u09AC'
U_BHA			= '\u09AD'
U_MA			= '\u09AE'
U_YA			= '\u09AF'
U_RA			= '\u09B0'
U_LA			= '\u09B2'
U_SHA			= '\u09B6'
U_SSA			= '\u09B7'
U_SA			= '\u09B8'
U_HA			= '\u09B9'
U_RRA			= '\u09DC'
U_RHA			= '\u09DD'
U_YYA			= '\u09DF'

U_ANUSVARA		= '\u0982'
U_VISARGA		= '\u0983'
U_CHANDRABINDU	= '\u0981'

U_KHANDATA		= '\u09CE'
U_HASANT		= '\u09CD'

U__AA			= '\u09BE'
U__I			= '\u09BF'
U__II			= '\u09C0'
U__U			= '\u09C1'
U__UU			= '\u09C2'
U__REE			= '\u09C3'
U__E			= '\u09C7'
U__AI			= '\u09C8'
U__O			= '\u09CB'
U__AU			= '\u09CC'

U_DARI		  	= '\u09F7'

full_tokens = [
	(N0			, U_N0		),
	(N1			, U_N1		),
	(N2			, U_N2		),
	(N3			, U_N3		),
	(N4			, U_N4		),
	(N5			, U_N5		),
	(N6			, U_N6		),
	(N7			, U_N7		),
	(N8			, U_N8		),
	(N9			, U_N9		),

	(A			, U_A		),
	(I			, U_I		),
	(II			, U_II		),
	(U			, U_U		),
	(UU			, U_UU		),
	(REE		, U_REE		),
	(E			, U_E		),
	(AI			, U_AI		),
	(O			, U_O		),
	(AU			, U_AU		),

	(KA			, U_KA		),
	(KHA		, U_KHA		),
	(GA			, U_GA		),
	(GHA		, U_GHA		),
	(NGA		, U_NGA		),
	(CA			, U_CA		),
	(CHA		, U_CHA		),
	(JA			, U_JA		),
	(JHA		, U_JHA		),
	(NYA		, U_NYA		),
	(TTA		, U_TTA		),
	(TTHA		, U_TTHA	),
	(DDA		, U_DDA		),
	(DDHA		, U_DDHA	),
	(NNA		, U_NNA		),
	(TA			, U_TA		),
	(THA		, U_THA		),
	(DA			, U_DA		),
	(DHA		, U_DHA		),
	(NA			, U_NA		),
	(PA			, U_PA		),
	(PHA		, U_PHA		),
	(BA			, U_BA		),
	(BHA		, U_BHA		),
	(MA			, U_MA		),
	(YA			, U_YA		),
	(RA			, U_RA		),
	(LA			, U_LA		),
	(SHA		, U_SHA		),
	(SSA		, U_SSA		),
	(SA			, U_SA		),
	(HA			, U_HA		),
	(RRA		, U_RRA		),
	(RHA		, U_RHA		),
	(YYA		, U_YYA		),

	(ANUSVARA	, U_ANUSVARA),
	(VISARGA	, U_VISARGA),
	(KHANDATA	, U_KHANDATA),
	(HASANT		, U_HASANT + '\u200C'),

	(USCORE		, '_'	   ),
	(DASH		, '-'	   ),
	(LS_QUOTE	, '\''	  ),
	(RS_QUOTE	, '\''	  ),
	(LD_QUOTE	, '"'	   ),
	(RD_QUOTE	, '""'	  ),

	(DARI		, U_DARI	),

	(GA_U		, U_GA  + U__U),
	(RA_U		, U_RA  + U__U),
	(RA_UU		, U_RA  + U__UU),
	(SHA_U		, U_SHA + U__U),
	(HA_REE		, U_HA  + U__REE),
	(HA_U		, U_HA  + U__U),

	(KA_KA		, U_KA  + U_CONJUNCT + U_KA),
	(KA_TTA		, U_KA  + U_CONJUNCT + U_TTA),
	(KA_SSA_MA	, U_KA  + U_CONJUNCT + U_SSA + U_CONJUNCT + U_MA),
	(KA_TA		, U_KA  + U_CONJUNCT + U_TA),
	(KA_MA		, U_KA  + U_CONJUNCT + U_MA),
	(KA_RA		, U_KA  + U_CONJUNCT + U_RA),
	(KA_SSA		, U_KA  + U_CONJUNCT + U_SSA),
	(KA_SA		, U_KA  + U_CONJUNCT + U_SA),
	(GA_GA		, U_GA  + U_CONJUNCT + U_GA),
	(GA_DA		, U_GA  + U_CONJUNCT + U_DA),
	(GA_DHA		, U_GA  + U_CONJUNCT + U_DHA),
	(NGA_KA		, U_NGA + U_CONJUNCT + U_KA),
	(NGA_KHA	, U_NGA + U_CONJUNCT + U_KHA),
	(NGA_GA		, U_NGA + U_CONJUNCT + U_GA),
	(CA_CA		, U_CA  + U_CONJUNCT + U_CA),
	(CA_CHA		, U_CA  + U_CONJUNCT + U_CHA),
	(JA_JA		, U_JA  + U_CONJUNCT + U_JA),
	(JA_JHA		, U_JA  + U_CONJUNCT + U_JHA),
	(JA_NYA		, U_JA  + U_CONJUNCT + U_NYA),
	(NYA_CA		, U_NYA + U_CONJUNCT + U_CA),
	(NYA_CHA	, U_NYA + U_CONJUNCT + U_CHA),
	(NYA_JA		, U_NYA + U_CONJUNCT + U_JA),
	(NYA_JHA	, U_NYA + U_CONJUNCT + U_JHA),
	(TTA_TTA	, U_TTA + U_CONJUNCT + U_TTA),
	(DDA_DDA	, U_DDA + U_CONJUNCT + U_DDA),
	(NNA_TTA	, U_NNA + U_CONJUNCT + U_TTA),
	(NNA_TTHA	, U_NNA + U_CONJUNCT + U_TTHA),
	(NNA_DDA	, U_NNA + U_CONJUNCT + U_DDA),
	(TA_TA		, U_TA  + U_CONJUNCT + U_TA),
	(TA_THA		, U_TA  + U_CONJUNCT + U_THA),
	(TA_MA		, U_TA  + U_CONJUNCT + U_MA),
	(TA_RA		, U_TA  + U_CONJUNCT + U_RA),
	(DA_DA		, U_DA  + U_CONJUNCT + U_DA),
	(DA_DHA		, U_DA  + U_CONJUNCT + U_DHA),
	(DA_BA		, U_DA  + U_CONJUNCT + U_BA),
	(DA_BHA		, U_DA  + U_CONJUNCT + U_BHA),
	(DA_MA		, U_DA  + U_CONJUNCT + U_MA),
	(DHA_BA		, U_DHA + U_CONJUNCT + U_BA),
	(NA_TA		, U_NA  + U_CONJUNCT + U_TA),
	(NA_TA_RA	, U_NA  + U_CONJUNCT + U_TA + U_CONJUNCT + U_RA),
	(NA_TTHA	, U_NA  + U_CONJUNCT + U_TTHA),
	(NA_DDA		, U_NA  + U_CONJUNCT + U_DDA),
	(NA_DHA		, U_NA  + U_CONJUNCT + U_DHA),
	(NA_THA		, U_NA  + U_CONJUNCT + U_THA),
	(NA_DA		, U_NA  + U_CONJUNCT + U_DA),
	(NA_SA		, U_NA  + U_CONJUNCT + U_SA),
	(PA_TTA		, U_PA  + U_CONJUNCT + U_TTA),
	(PA_TA		, U_PA  + U_CONJUNCT + U_TA),
	(PA_PA		, U_PA  + U_CONJUNCT + U_PA),
	(PA_SA		, U_PA  + U_CONJUNCT + U_SA),
	(BA_JA		, U_BA  + U_CONJUNCT + U_JA),
	(BA_DA		, U_BA  + U_CONJUNCT + U_DA),
	(BA_DHA		, U_BA  + U_CONJUNCT + U_DHA),
	(BA_BA		, U_BA  + U_CONJUNCT + U_BA),
	(BHA_RA		, U_BHA + U_CONJUNCT + U_RA),
	(MA_MA		, U_MA  + U_CONJUNCT + U_MA),
	(MA_NA		, U_MA  + U_CONJUNCT + U_NA),
	(MA_PA		, U_MA  + U_CONJUNCT + U_PA),
	(MA_PHA		, U_MA  + U_CONJUNCT + U_PHA),
	(MA_BA		, U_MA  + U_CONJUNCT + U_BA),
	(MA_BHA		, U_MA  + U_CONJUNCT + U_BHA),
	(MA_LA		, U_MA  + U_CONJUNCT + U_LA),
	(LA_KA		, U_LA  + U_CONJUNCT + U_KA),
	(LA_GA		, U_LA  + U_CONJUNCT + U_GA),
	(LA_TTA		, U_LA  + U_CONJUNCT + U_TTA),
	(LA_DDA		, U_LA  + U_CONJUNCT + U_DDA),
	(LA_PA		, U_LA  + U_CONJUNCT + U_PA),
	(LA_PHA		, U_LA  + U_CONJUNCT + U_PHA),
	(SHA_CA		, U_SHA + U_CONJUNCT + U_CA),
	(SHA_CHA	, U_SHA + U_CONJUNCT + U_CHA),
	(SSA_KA		, U_SSA + U_CONJUNCT + U_KA),
	(SSA_KA_RA	, U_SSA + U_CONJUNCT + U_KA + U_CONJUNCT + U_RA),
	(SSA_TTA	, U_SSA + U_CONJUNCT + U_TTA),
	(SSA_TTHA	, U_SSA + U_CONJUNCT + U_TTHA),
	(SSA_NNA	, U_SSA + U_CONJUNCT + U_NNA),
	(SSA_PA		, U_SSA + U_CONJUNCT + U_PA),
	(SSA_PHA	, U_SSA + U_CONJUNCT + U_PHA),
	(SSA_MA		, U_SSA + U_CONJUNCT + U_MA),
	(SA_KA		, U_SA  + U_CONJUNCT + U_KA),
	(SA_KHA		, U_SA  + U_CONJUNCT + U_KHA),
	(SA_TTA		, U_SA  + U_CONJUNCT + U_TTA),
	(SA_TA		, U_SA  + U_CONJUNCT + U_TA),
	(SA_TA_RA	, U_SA  + U_CONJUNCT + U_TA + U_CONJUNCT + U_RA),
	(SA_THA		, U_SA  + U_CONJUNCT + U_THA),
	(SA_NA		, U_SA  + U_CONJUNCT + U_NA),
	(SA_PA		, U_SA  + U_CONJUNCT + U_PA),
	(SA_PHA		, U_SA  + U_CONJUNCT + U_PHA),
	(SA_BA		, U_SA  + U_CONJUNCT + U_BA),
	(SA_MA		, U_SA  + U_CONJUNCT + U_MA),
	(HA_NA		, U_HA  + U_CONJUNCT + U_NA),
	(HA_BA		, U_HA  + U_CONJUNCT + U_BA),
	(HA_MA		, U_HA  + U_CONJUNCT + U_MA),
	(RRA_GA		, U_RRA + U_CONJUNCT + U_GA),

	(NGA_		, U_NGA + U_CONJUNCT),
	(DA_		, U_DA + U_CONJUNCT),

	(AnyChar	, TEXT		)
]

pre_kars = {
	_I		: U__I,
	_E1		: U__E,
	_E2		: U__E,
	_AI1	: U__AI,
	_AI2	: U__AI
	}

post_kars = {
	_AA		: U__AA,
	_II		: U__II,
	_U1		: U__U,
	_U2		: U__U,
	_U3		: U__U,
	_U4		: U__U,
	_UU1	: U__UU,
	_UU2	: U__UU,
	_UU3	: U__UU,
	_REE1	: U__REE,
	_REE2	: U__REE,
	_AU		: U__AU
	}

composite_kars = {
	_AA: {
		_E1: U__O,
		_E2: U__O
		},
	_AU: {
		_E1: U__AU,
		_E2: U__AU,
		}
	}

incompletes = [U__AA , U__I , U__II , U__U , U__UU , U__REE , U__E , U__AI , U__O , U__AU]

suffix_tokens = {
		_NA		: U_CONJUNCT + U_NA,
		_BA1	: U_CONJUNCT + U_BA,
		_BA2	: U_CONJUNCT + U_BA,
		_MA		: U_CONJUNCT + U_MA,
		_YA		: U_CONJUNCT + U_YA,
		_LA1	: U_CONJUNCT + U_LA,
		_LA2	: U_CONJUNCT + U_LA,
		_RA1	: U_CONJUNCT + U_RA,
		_RA2	: U_CONJUNCT + U_RA,
		_RA3	: U_CONJUNCT + U_RA
	}

tokenlist = []


def chandrabindu(scanner, text):
	# just save it for later
	scanner.savedtokens.append(U_CHANDRABINDU)


def pre_kar(scanner, text):
	# just save it for later
	apply_saved_tokens(scanner)
	scanner.savedtokens.append(pre_kars[text])


def process_chandrabindu(scanner):
	if U_CHANDRABINDU in scanner.savedtokens:
		# see if the CHANDRABINDU is before any kars, if so, move it after
		scanner.savedtokens.remove(U_CHANDRABINDU)
		scanner.savedtokens.append(U_CHANDRABINDU)


def post_process():
	# do some post processing on tokenlist
	pass


def apply_saved_tokens(scanner):
	process_chandrabindu(scanner)
	tokenlist.extend(scanner.savedtokens)
	scanner.savedtokens = []
	scanner.begin('')
	post_process()


def post_kar(scanner, text):
	# for some post_kars, check saved pre_kars and decide what should be produced
	if text in composite_kars:
		if scanner.savedtokens:
			st = scanner.savedtokens.pop()
			if st in composite_kars[text]:
				scanner.savedtokens.append(composite_kars[text][st])
			else:
				scanner.savedtokens.append(st)
				scanner.savedtokens.append(post_kars[text])
		else:
			scanner.savedtokens.append(post_kars[text])
	else:
		scanner.savedtokens.append(post_kars[text])

	# handle cases where U__E precedes a U__AA or U__AU
	if tokenlist and tokenlist[len(tokenlist)-1] == U__E:
		if scanner.savedtokens:
			if scanner.savedtokens[len(scanner.savedtokens)-1] == U__AA:
				tokenlist.pop()
				scanner.savedtokens.pop()
				scanner.savedtokens.append(U__O)
			elif scanner.savedtokens[len(scanner.savedtokens)-1] == U__AU:
				tokenlist.pop()
				scanner.savedtokens.pop()
				scanner.savedtokens.append(U__AU)

	apply_saved_tokens(scanner)

def ref(scanner, text):
	# search through the tokenlist to find the place where to put the R_
	templist = []
	while 1:
		try:
			lasttoken = tokenlist.pop()
			templist.insert(0, lasttoken)
			if lasttoken in incompletes:
				pass
			else:
				break
		except IndexError as e:
			break

	tokenlist.append(U_RA + U_CONJUNCT)
	tokenlist.extend(templist)

def suffix_token(scanner, text):
	# see if the immediate previous token is a kar or not, if kar append before it
	if tokenlist:
		lasttoken = tokenlist.pop()
		if lasttoken in incompletes:
			tokenlist.append(suffix_tokens[text])
			tokenlist.append(lasttoken)
		else:
			tokenlist.append(lasttoken)
			tokenlist.append(suffix_tokens[text])


states = [
	(Str(_AA)					, post_kar),
	(Str(_II)					, post_kar),
	(Str(_U1, _U2, _U3, _U4)	, post_kar),
	(Str(_UU1, _UU2, _UU3)		, post_kar),
	(Str(_REE1, _REE2)			, post_kar),
	(Str(_REE1, _REE2)			, post_kar),
	(Str(_AU)					, post_kar),

	(Str(_I)					, pre_kar),
	(Str(_E1, _E2)				, pre_kar),
	(Str(_AI1, _AI2)			, pre_kar),

	(Str(_NA)					, suffix_token),
	(Str(_BA1, _BA2)			, suffix_token),
	(Str(_MA)					, suffix_token),
	(Str(_YA)					, suffix_token),
	(Str(_LA1)					, suffix_token),
	(Str(_LA2)					, suffix_token),
	(Str(_RA1, _RA2, _RA3)		, suffix_token),

	(Str(RA_)					, ref),

	(Str(CHANDRABINDU)			, chandrabindu)
]


def main():
	if (len(sys.argv) < 2):
		print('Usage:', sys.argv[0], 'input_file', 'output_file')
		exit(-1)
	lexicon = Lexicon(states + full_tokens)
	filename = sys.argv[1]
	f = open(filename, "r")
	scanner = Scanner(lexicon, f, filename)
	scanner.begin('')
	scanner.savedtokens = []
	while 1:
		token = scanner.read()
		if token[0] is not None:
			tokenlist.append(token[0])
			apply_saved_tokens(scanner)
		else:
			break

	apply_saved_tokens(scanner)
	for tt in tokenlist:
		print(tt, end='')


if __name__ == '__main__':
	main()
