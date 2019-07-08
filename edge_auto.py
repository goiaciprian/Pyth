#!usr/bin/env python3

from selenium import webdriver


def pbinfo():
    browser = webdriver.Edge()
    browser.get('www.pbinfo.ro')
    user = browser.find_element_by_id('user')
    user.send_keys('vsDeus')
    passs = browser.find_element_by_id('parola')
    passs.send_keys('8fdafa80otilia')
    secondGood = browser.find_element_by_xpath(
        "//*[@id='form-login']/div/div[2]/div[4]/button")
    secondGood.click()


if __name__ == "__main__":
    pbinfo()
