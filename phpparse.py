from __future__ import print_function
try:
    from HTMLParser import HTMLParser  # Python 2
except ImportError:
    from html.parser import HTMLParser # Python 3

import sys
import re

TAG_REGEX = re.compile(r'<[^>]+>')


class SynopsisParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)

        self.in_synopsis_level = 0
        self.reset_data()

    def in_synopsis(self):
        return self.in_synopsis_level > 0

    def reset_data(self):
        self.synopsis_data = []

    @staticmethod
    def is_synopsis_tag(attr):
        return "methodsynopsis" in attr.get("class", "")

    def handle_starttag(self, tag, attributes):
        attr = dict(attributes)
        if self.is_synopsis_tag(attr):
            self.in_synopsis_level += + 1
            self.reset_data()

        elif self.in_synopsis_level > 0:
            self.in_synopsis_level += 1

    def handle_endtag(self, tag):
        if self.in_synopsis():
            self.in_synopsis_level -= 1

            if not self.in_synopsis():
                synopsis = cleanup(" ".join(self.synopsis_data))
                if "public" not in synopsis and "private" not in synopsis and "protected" not in synopsis:
                    print(synopsis)

    def handle_data(self, data):
        if self.in_synopsis():
            self.synopsis_data.append(data)


def cleanup(html):
    cleaned = TAG_REGEX.sub(' ', html)
    cleaned = (' '.join(cleaned.replace('\n', '').split())).replace(' , ', ', ')

    return cleaned


def main():
    with open(sys.argv[1]) as doc:
        SynopsisParser().feed(doc.read())

if __name__ == "__main__":
    main()
