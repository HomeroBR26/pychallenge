"""URL: http://www.pythonchallenge.com/pc/def/peak.html
   NEXT: http://www.pythonchallenge.com/pc/def/channel.html"""
#! python3
import pickle

answer = pickle.load(open("banner.p", 'rb'))

for elem in answer:
    strline = ''
    for item in elem:
        for char in range(item[1]):
            strline += item[0]
    print(strline)
