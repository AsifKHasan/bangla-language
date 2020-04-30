#!/usr/bin/env python3

import json
from functional import seq

_songsfile = './songs-data.json'

def main():
    with open(_songsfile, 'r') as data_file:
        song = json.loads(data_file.read())

    print(len(song))
    
if __name__ == '__main__':
    main()
