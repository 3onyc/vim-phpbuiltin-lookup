from __future__ import print_function

from bs4 import BeautifulSoup
import sys
import re

tagRegex = re.compile(r'<[^>]+>')

def cleanup(html):
    cleaned = tagRegex.sub(' ', html)
    cleaned = (' '.join(cleaned.replace('\n', '').split())).replace(' , ', ', ')

    return cleaned

def main(): 
    with open(sys.argv[1]) as doc:
        soup = BeautifulSoup(doc.read(), 'lxml')

    for elem in soup.find_all(class_='methodsynopsis'):
        print(cleanup(str(elem)))

if __name__ == "__main__":
    main()
