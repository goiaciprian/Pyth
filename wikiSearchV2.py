#!/usr/bin/env python3

from json import loads
from urllib.request import urlopen
from pprint import pprint


def searchWiki(search: str, lang: str="ro") -> list:
    __listaCuvinte = search.split()
    __searchWords = str(__listaCuvinte[0])
    for i in __listaCuvinte[1::]:
        __searchWords += "_" + str(i)
    __api = f"https://{lang.lower()}.wikipedia.org/w/api.php?action=opensearch&search={__searchWords}"
    try:
        __URLdata = urlopen(__api).read().decode('utf-8')
    except Exception as e:
        print(e)
    __data = loads(__URLdata)
    __answerList = []
    for nume, link in enumerate(__data[3]):
        __answerList.append((__data[1][nume], link))
    return __answerList


if __name__ == "__main__":
    from sys import argv
    pprint(searchWiki(argv[1]))
