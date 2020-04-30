#!/usr/bin/env python3
import pygsheets

import httplib2

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from pydrive.auth import GoogleAuth

import pandas as pd
import pprint

CRED_JSON = './conf/credential.json'
GSHEET_NAME = 'মোবি-ডিক, সেই তিমি'
SYLLABLE_FILE = './data/syllables'

# authorize and authenticate
_G = pygsheets.authorize(service_account_file=CRED_JSON)
credentials = ServiceAccountCredentials.from_json_keyfile_name(CRED_JSON, scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'])
credentials.authorize(httplib2.Http())

_service = discovery.build('sheets', 'v4', credentials=credentials)

_gauth = GoogleAuth()
_gauth.credentials = credentials

# open gsheet
_gsheet = _G.open(GSHEET_NAME)

# get syllables
ws_title = 'syllables'

ws = _gsheet.worksheet('title', ws_title)
df = ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=True, start='A2', end='B{0}'.format(ws.rows))

# get length of en syllable
df['l-en'] = df['en'].str.len()

# see if the syllable starts with vowel
df['vowel'] = df['en'].str[:1].str.contains('[aeiou]', case=False, regex=True)

# sort by vowel, l-en desc, en
df.sort_values(['vowel', 'l-en', 'en'], ascending=[True, False, True], inplace=True)

# save to data-file
df.to_csv(SYLLABLE_FILE, sep=':', encoding='utf-8', columns=['en', 'bn'], index=False, header=False)
