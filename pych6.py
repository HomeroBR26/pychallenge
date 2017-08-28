"""URL: http://www.pythonchallenge.com/pc/def/channel.html
   NEXT: """
#! python3
import zipfile
import re


def readzip(nothing):
    zfile = zipfile.ZipFile('channel.zip')
    comments = ''

    while True:
        with zfile.open(nothing + '.txt', 'r') as txt:
            contents = str(txt.readlines())
            yield contents
            comments += str(zfile.getinfo(nothing + '.txt').comment)
            try:
                nothing = re.search("nothing is (\d+)", contents).group(1)
            except AttributeError:
                break
    print(comments)

for file in readzip('90052'):
    print(file)
