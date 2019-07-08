#!usr/bin/env python3

from selenium import webdriver
import sys

if sys.platform == 'linux':
    path = '/mnt/d/vsc/drivers/chromedriver.exe'
elif sys.platform == 'win32':
    path = 'D:\\vsc\\drivers\\chromedriver.exe'


browser = webdriver.Chrome(path)


def pbinfo():
    browser.maximize_window()
    browser.get('https://www.pbinfo.ro/')
    user = browser.find_element_by_xpath("//*[@id='user']")
    user.send_keys("vsDeus")
    passs = browser.find_element_by_xpath("//*[@id='parola']")
    passs.send_keys("8fdafa80otilia")
    log_in = browser.find_element_by_xpath(
        "//*[@id='form-login']/div/div[2]/div[4]/button")
    log_in.click()
    browser.get(
        "https://www.pbinfo.ro/?pagina=probleme-lista&tag=12&start=30")


if __name__ == "__main__":
    pbinfo()
