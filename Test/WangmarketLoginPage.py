# -*- coding: utf-8 -*-
'''
登录页面
'''
import shelve
import time

from Page.BasePage import BasePage


class WangmarketLoginPage(BasePage):
    def __init__(self,driver):
        super(WangmarketLoginPage, self).__init__(driver)
        driver.get('http://120.27.71.205:9004/login.do')
        BasePage.printSymbol(self)
        time.sleep(2)


    def setLoginInfos(self,username,password,verticode):
        self.sendKeys('//input[@name="username"]',username)
        self.sendKeys('//input[@name="password"]', password)
        self.sendKeys('//input[@name="code"]', verticode)

    def clickButton(self):
        self.click(self.findEelement('//button[text()="立即登陆"]'))

    def login(self,username,password,verticode):
        self.setLoginInfos(username,password,verticode)
        self.clickButton()
        print('*'*32)

    def run(self):
        self.login('test','test', 'aaaaa')
        time.sleep(1)
        cookie_db = shelve.open('wangmarket_db_cookies')
        cookie_db['wangmarket_cookie'] = self.driver.get_cookies()
        cookie_db.close()










