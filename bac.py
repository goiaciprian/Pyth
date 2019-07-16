
import requests
from bs4 import BeautifulSoup

HTTP = 'http://bacalaureat.edu.ro/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3829.0 Safari/537.36 Edg/77.0.197.1'
}


def check():
    page = requests.get(HTTP, headers=headers)
    soup = BeautifulSoup(page, 'html.parser')  # schimbare in clas
    print(soup)


check()
