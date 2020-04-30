#!/usr/bin/env python3

import os
import json
from functional import seq
import parse_song

_outputfile = './songs-data.json'
_outdir = u'./songs/'

def main():
    donelist = os.listdir(_outdir)
    out = []

    for f in donelist:
        if f.endswith(".json"):
            print(f)
            with open(_outdir + f, 'r') as data_file:
                song = json.loads(data_file.read())

                out.append(song)

    out = sorted(out, key=lambda k: k['নাম'])
    print(len(donelist))
    print(len(out))
    with open(_outputfile, 'w') as jsonFile:
        print(json.dumps(out, indent=2, ensure_ascii=False), file=jsonFile)

if __name__ == '__main__':
    main()
