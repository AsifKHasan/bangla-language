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

A				= Str('\x41')
I				= Str('\x42')
II				= Str('\x43')
U				= Str('\x44')
UU				= Str('\x45')
REE				= Str('\x46')
E				= Str('\x47')
AI				= Str('\x48')
O				= Str('\x49')
AU				= Str('\x4A')

_AA				= '\x76'
_I				= '\x77'
_II				= '\x78'
_U1				= '\x79'
_U2				= '\x7A'
_U3				= '\u2013'
_U4				= '\u201C'
_UU1			= '\x7E'
_UU2			= '\x81'
_UU3			= '\x82'
_UU4			= '\u201A'
_REE1			= '\x83'
_REE2			= '\x84'
_REE3			= '\x85'
_REE4			= '\u2026'
_E1				= '\x86'
_E2				= '\x87'
_E3				= '\u2020'
_E4				= '\u2021'
_AI1			= '\x88'
_AI2			= '\x89'
_AU1			= '\x8A'
_AU2			= '\u0160'

KA				= Str('\x4B')
KHA				= Str('\x4C')
GA				= Str('\x4D')
GHA				= Str('\x4E')
NGA				= Str('\x4F')
CA				= Str('\x50')
CHA				= Str('\x51')
JA				= Str('\x52')
JHA				= Str('\x53')
NYA				= Str('\x54')
TTA				= Str('\x55')
TTHA			= Str('\x56')
DDA				= Str('\x57')
DDHA			= Str('\x58')
NNA				= Str('\x59')
TA				= Str('\x5A')
THA				= Str('\x5F')
DA				= Str('\x60')
DHA				= Str('\x61')
NA				= Str('\x62')
PA				= Str('\x63')
PHA				= Str('\x64')
BA				= Str('\x65')
BHA				= Str('\x66')
MA				= Str('\x67')
YA				= Str('\x68')
RA				= Str('\x69')
LA				= Str('\x6A')
SHA				= Str('\x6B')
SSA				= Str('\x6C')
SA				= Str('\x6D')
HA				= Str('\x6E')
RRA				= Str('\x6F')
RHA				= Str('\x70')
YYA				= Str('\x71')

KHANDATA		= Str('\x72')
ANUSVARA		= Str('\x73')
VISARGA			= Str('\x74')
CHANDRABINDU	= '\x75'
HASANT			= Str('\x26')

KA_KA			= Str('\xB0')
KA_TTA			= Str('\xB1')
KA_TA			= Str('\xB3')
KA_MA			= Str('\xB4')
KA_RA			= Str('\xB5')
KA_SSA			= Str('\xB6')
KA_SSA_MA		= Str('\xB2')
KA_SA			= Str('\xB7')

GA_GA			= Str('\xB9')
GA_DA			= Str('\xBA')
GA_DHA			= Str('\xBB')

NGA_KA			= Str('\xBC')
NGA_KHA			= Str('\x01')
NGA_GA			= Str('\xBD')

CA_CA			= Str('\x01')
CA_CHA			= Str('\x01')

JA_JA			= Str('\xBE')
JA_JHA			= Str('\xC0')
JA_NYA			= Str('\xC1')

NYA_CA			= Str('\xC2')
NYA_CHA			= Str('\xC3')
NYA_JA			= Str('\xC4')
NYA_JHA			= Str('\xC5')

TTA_TTA			= Str('\xC6')

DDA_DDA			= Str('\xC7')

NNA_TTA			= Str('\xC8')
NNA_TTHA		= Str('\xC9')
NNA_DDA			= Str('\xCA')

TA_TA			= Str('\xCB')
TA_THA			= Str('\xCC')
TA_MA			= Str('\xCD')
TA_RA			= Str('\xCE')

DA_DA			= Str('\xCF')
DA_DHA			= Str('\xD7')
DA_BA			= Str('\xD8')
DA_BHA			= Str('\x01')
DA_MA			= Str('\xD9')

DHA_BA			= Str('\x01')

NA_TA			= Str('\x01')
NA_TA_RA		= Str('\x01')
NA_TTHA			= Str('\xDA')
NA_DDA			= Str('\xDB')
NA_DHA			= Str('\xDC')
NA_THA			= Str('\x01')
NA_DA			= Str('\x01')
NA_SA			= Str('\xDD')

PA_TTA			= Str('\xDE')
PA_TA			= Str('\xDF')
PA_PA			= Str('\xE0')
PA_SA			= Str('\xE1')

BA_JA			= Str('\xE2')
BA_DA			= Str('\xE3')
BA_DHA			= Str('\xE4')
BA_BA			= Str('\x01')

BHA_RA			= Str('\xE5')

MA_MA			= Str('\x01')
MA_NA			= Str('\xE6')
MA_PHA			= Str('\xE7')
MA_PA			= Str('\x01')
MA_BA			= Str('\x01')
MA_BHA			= Str('\x01')
MA_LA			= Str('\x01')

LA_KA			= Str('\xE9')
LA_GA			= Str('\xEA')
LA_TTA			= Str('\xEB')
LA_DDA			= Str('\xEC')
LA_PA			= Str('\xED')
LA_PHA			= Str('\xEE')

SHA_CA			= Str('\xF0')
SHA_CHA			= Str('\xF1')

SSA_KA			= Str('\x01')
SSA_KA_RA		= Str('\x01')
SSA_TTA			= Str('\xF3')
SSA_TTHA		= Str('\xF4')
SSA_NNA			= Str('\xF2')
SSA_PA			= Str('\x01')
SSA_PHA			= Str('\xF5')
SSA_MA			= Str('\x01')

SA_KA			= Str('\x01')
SA_KHA			= Str('\xF6')
SA_TTA			= Str('\xF7')
SA_TA			= Str('\x01')
SA_TA_RA		= Str('\x01')
SA_THA			= Str('\x01')
SA_NA			= Str('\xF8')
SA_PA			= Str('\x01')
SA_PHA			= Str('\xF9')
SA_BA			= Str('\x01')
SA_MA			= Str('\x01')

HA_NA			= Str('\xFD')
HA_BA			= Str('\x01')
HA_MA			= Str('\xFE')

RRA_GA			= Str('\xFF')


_KA				= '\x8B'
_KA_RA			= '\x8C'
_TA1			= '\x8F'
_TA2			= '\u2014'
_TA_U			= '\x91'
_TA_RA			= '\x90'
_THA1			= '\x92'
_THA2			= '\u2019'
_NA1			= '\x9C'
_NA2			= '\xA5'
_PA				= '\x95'
_BA1			= '\x5E'
_BA2			= '\xA1'
_BA3			= '\xA6'
_BHA			= '\xA2'
_BHA_RA			= '\xA3'
_MA				= '\xA7'
_YA				= '\xA8'
_RA1			= '\xAA'
_RA2			= '\xAB'
_RA3			= '\xD6'
_LA1			= '\xAC'
_LA2			= '\xAD'


NGA_			= Str('\x8D')
CA_				= Str('\x94')
NNA_			= Str('\u0000')
DA_				= Str('\x98', '\x99')
NA_				= Str('\x9A', '\x9B', '\u203a', '\u0161')
PA_				= Str('\xFA')
BA_				= Str('\x9F')
MA_				= Str('\xA4')
RA_				= '\xA9'
SSA_			= Str('\xAE')
SA_				= Str('\xAF')


GA_U			= Str('\xB8')
RA_U			= Str('\xC0')
RA_UU			= Str('\x01')
SHA_U			= Str('\xEF')
HA_REE			= Str('\xFC')
HA_U			= Str('\xFB')

USCORE			= Str('\xD0')
DASH			= Str('\x2D')
LS_QUOTE		= Str('\xC8')
RS_QUOTE		= Str('\x27')
LD_QUOTE		= Str('\xCD')
RD_QUOTE		= Str('\x01')

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
	(CA_		, U_CA + U_CONJUNCT),
	(NNA_		, U_NNA + U_CONJUNCT),
	(DA_		, U_DA + U_CONJUNCT),
	(NA_		, U_NA + U_CONJUNCT),
	(PA_		, U_PA + U_CONJUNCT),
	(BA_		, U_BA + U_CONJUNCT),
	(MA_		, U_MA + U_CONJUNCT),
	(SSA_		, U_SSA + U_CONJUNCT),
	(SA_		, U_SA + U_CONJUNCT),

	(AnyChar	, TEXT		)
]

pre_kars = {
	_I		: U__I,
	_E1		: U__E,
	_E2		: U__E,
	_E3		: U__E,
	_E4		: U__E,
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
	_UU4	: U__UU,
	_REE1	: U__REE,
	_REE2	: U__REE,
	_REE3	: U__REE,
	_REE4	: U__REE,
	_AU1	: U__AU,
	_AU2	: U__AU
	}

composite_kars = {
	_AA: {
		_E1: U__O,
		_E2: U__O,
		_E3: U__O,
		_E4: U__O
		},
	_AU1: {
		_E1: U__AU,
		_E2: U__AU,
		_E3: U__AU,
		_E4: U__AU
		},
	_AU2: {
		_E1: U__AU,
		_E2: U__AU,
		_E3: U__AU,
		_E4: U__AU
		}
	}

incompletes = [U__AA , U__I , U__II , U__U , U__UU , U__REE , U__E , U__AI , U__O , U__AU]

suffix_tokens = {
		_TA1	: U_CONJUNCT + U_TA,
		_TA2	: U_CONJUNCT + U_TA,
		_THA1	: U_CONJUNCT + U_THA,
		_THA2	: U_CONJUNCT + U_THA,
		_NA1	: U_CONJUNCT + U_NA,
		_NA2	: U_CONJUNCT + U_NA,
		_BA1	: U_CONJUNCT + U_BA,
		_BA2	: U_CONJUNCT + U_BA,
		_BA3	: U_CONJUNCT + U_BA,
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


def post_process(tokens):
	# do some post processing on tokenlist
	pass


def apply_saved_tokens(scanner):
	process_chandrabindu(scanner)
	tokenlist.extend(scanner.savedtokens)
	scanner.savedtokens = []
	scanner.begin('')


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
	# search through the tokenlist to find the place where to put the RA_
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
	(Str(_AA)							, post_kar),
	(Str(_II)							, post_kar),
	(Str(_U1, _U2, _U3, _U4)			, post_kar),
	(Str(_UU1, _UU2, _UU3, _UU4)		, post_kar),
	(Str(_REE1, _REE2, _REE3, _REE4)	, post_kar),
	(Str(_AU1, _AU2)					, post_kar),

	(Str(_I)							, pre_kar),
	(Str(_E1, _E2, _E3, _E4)			, pre_kar),
	(Str(_AI1, _AI2)					, pre_kar),

	(Str(_TA1, _TA2)					, suffix_token),
	(Str(_THA1, _THA2)					, suffix_token),
	(Str(_NA1, _NA2)					, suffix_token),
	(Str(_BA1, _BA2, _BA3)				, suffix_token),
	(Str(_MA)							, suffix_token),
	(Str(_YA)							, suffix_token),
	(Str(_LA1)							, suffix_token),
	(Str(_LA2)							, suffix_token),
	(Str(_RA1, _RA2, _RA3)				, suffix_token),

	(Str(RA_)							, ref),

	(Str(CHANDRABINDU)					, chandrabindu)
]


def main():
	if (len(sys.argv) < 2):
		print('Usage:', sys.argv[0], 'input_file', 'output_file')
		exit(-1)
	#lexicon = Lexicon(states + full_tokens)
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
	#post_process(tokenlist)
	s = ''.join(tokenlist).replace(U_CONJUNCT + U_CONJUNCT, U_CONJUNCT)
	print(s, end='')


if __name__ == '__main__':
	main()
