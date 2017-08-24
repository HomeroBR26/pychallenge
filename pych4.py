"""URL: http://www.pythonchallenge.com/pc/def/linkedlist.php
   NEXT: http://www.pythonchallenge.com/pc/def/peak.html"""
#! python3
import urllib.request
import re


def followchain():
    """Follow the chain of url links until you find something different."""
    nothing = "12345"

    while True:
        with urllib.request.urlopen("http://pythonchallenge.com/pc/def/linked"
                                    "list.php?nothing=" + nothing) as url:
            html = url.read().decode('utf-8')
            yield html
            try:
                nothing = re.search("nothing is (\d+)", html).group(1)
            except AttributeError:
                break


for link in followchain():
    print(link)
