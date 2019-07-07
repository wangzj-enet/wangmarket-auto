# -*- coding: utf-8 -*-
'''
AddColumn
2019-07-06 11:42 
PyCharm
页面
'''

import time


from Page.BasePage import BasePage


class AddColumn(BasePage):
    def __init__(self, driver):
        super(AddColumn, self).__init__(driver)
        # driver.get('http://120.27.71.205:9004/template/index.do')
        BasePage.printSymbol(self)
        time.sleep(1)

    def run(self):
        self.clickLanmuguanli()
        self.driver.switch_to_frame("iframe")
        self.clickAddColumn()
        time.sleep(0.2)
        self.driver.switch_to_frame("layui-layer-iframe1")

    def clickLanmuguanli(self):
        self.click(self.findEelement('//html/body/div[1]/div[1]/ul/li[5]/a/span'))
        time.sleep(2)

    def clickAddColumn(self):
        self.click(self.findEelement('//html/body/div[1]/button'))
        time.sleep(2)

    def setType2ColumnInfos(self,name):
        # print(self.driver.page_source)

        self.sendKeys('//form/div[1]/div/div[1]/div[1]/div/input[@name="name"]',name)
        self.click(self.findEelement('//input[@placeholder="顶级栏目"]'))
        self.click(self.findEelement('//dl/dd[text()="顶级栏目"]'))

        self.click(self.findEelement('// div / input[@placeholder="请选择"]'))
        self.click(self.findEelement('//dl/dd[@lay-value="7"]'))


        self.click(self.findEelement('//form/div[1]/div/div[1]/div[4]/div/div/div/input[@placeholder="请选择"]'))
        self.click(self.findEelement('//dl/dd[@lay-value="%s"]' %(name)))


        # self.click(self.findEelement('//form/div[1]/div/div[1]/div[5]/div/div/div/input[@placeholder="请选择"]'))
        # self.click(self.findEelement('//dl/dd[@lay-value="%s"]' %(name)))
        self.sendKeys('//input[@name="codeName"]', name)
        self.sendKeys('//input[@name="listNum"]', 10)
        time.sleep(1)




    def clickType2Button(self):
        self.click(self.findEelement('//html/body/form/div[2]/div/button[1]'))
        time.sleep(1)



    def setType3ColumnInfos(self,parentname,name):
        # print(self.driver.page_source)
        time.sleep(0.1)
        self.sendKeys('//form/div[1]/div/div[1]/div[1]/div/input[@name="name"]',name)
        self.click(self.findEelement('//input[@placeholder="顶级栏目"]'))
        self.click(self.findEelement('//dl/dd[@lay-value="%s"]' %(parentname)))

        self.click(self.findEelement('//form /div[1]/div/div[1]/div[3]/div/div/div/input[@placeholder="请选择"]'))
        self.click(self.findEelement('//dl/dd[@lay-value="8"]'))


        self.click(self.findEelement('//form/div[1]/div/div[1]/div[5]/div/div/div/input[@placeholder="请选择"]'))
        self.click(self.findEelement('//form/div[1]/div/div[1]/div[5]/div/div/dl/dd[@lay-value="%s"]' %(name)))
        ''
        self.sendKeys('//input[@name="codeName"]', name)
        time.sleep(0.1)




    def clickType3Button(self):
        self.click(self.findEelement('//html/body/form/div[2]/div/button[1]'))
        time.sleep(0.1)



