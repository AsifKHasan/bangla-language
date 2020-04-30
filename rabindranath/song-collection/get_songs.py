#!/usr/bin/env python3

import os
import json
from functional import seq
import parse_song

_datafile = './songs-url.json'
_outputfile = './songs-data.json'
_outdir = u'./songs/'

def output(songs):
    donelist = list(map(lambda f: f.replace('.json', '').replace(u'\u09c7\u09be', u'\u09cb'), os.listdir(_outdir)))
    #donelist = list(map(lambda f: f.replace('.json', ''), os.listdir(_outdir)))
    #print(len(donelist))
    out =  seq(songs).filter(lambda u: u['title'] not in donelist).list()
    print(len(out))
    out = seq(out).map(lambda s: parse_song.get_and_parse(s, _outdir)).list()

    with open(_outputfile, 'w') as jsonFile:
        print(json.dumps(out, indent=2, ensure_ascii=False), file=jsonFile)

def get_songs(urls):
    songs = (seq(urls)
             .sorted(key=lambda k: k['title'])
             .map(lambda u: {**u, **dict(zip(['title', 'category'], u['title'].split(': ')))})
             ).list()

    return songs

def load_data():
    with open(_datafile, 'r') as data_file:
        return json.loads(data_file.read())

def main():
    urls = load_data()
    songs = get_songs(urls)
    output(songs)

if __name__ == '__main__':
    main()
