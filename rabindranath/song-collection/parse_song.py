#!/usr/bin/env python3

import sys
import json
import urllib
from datetime import datetime
from bs4 import BeautifulSoup

_title = 'দুই হাতে--কালের মন্দিরা'
_category = 'বিচিত্র'
_output_file = './songs/' + _title + '.json'
_html_source = './songs/' + _title + '.html'

_counter = 1
_starttime = datetime.now()

def save_song(filepath, js):
    with open(filepath.encode(sys.getfilesystemencoding()), 'w') as jsonFile:
        print(json.dumps(js, indent=2, ensure_ascii=False), file=jsonFile)

def parse(soup, title, category, filepath):
    div = soup.find_all('div', class_='content')[0]
    tags = div.find_all('span', class_='bn')
    lines = [t.string for t in tags]
    tags = div.find_all('span', class_='trivia')
    info = dict([(t[0].string.strip(':'), t[1].strip()) for t in [x.contents for x in tags]])
    js = {**{'নাম': title, 'পর্যায়': category}, **info, **{'কথা': lines}}
    save_song(filepath, js)
    return js

def get_and_parse(song, savedir):
    global _counter
    global _starttime

    t1 = datetime.now()
    _counter = _counter + 1
    html = urllib.request.urlopen(song['url']).read()
    d = parse(BeautifulSoup(html, "html.parser"), song['title'], song['category'], savedir + song['title'] + '.json')
    t2 = datetime.now()
    print("{: 4}  {}  {}  - {}".format(_counter, str(t2-t1), str(t2- _starttime), song['title']))
    return d

def main():
    s = parse(BeautifulSoup(open(_html_source), "html.parser"), _title, _category, _output_file)

    with open(_output_file, 'w') as jsonFile:
        print(json.dumps(s, indent=2, ensure_ascii=False), file=jsonFile)

if __name__ == '__main__':
    main()
