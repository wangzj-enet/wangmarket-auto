# -*- coding: utf-8 -*-
'''
WebTest
2019-07-06 11:35 
PyCharm
页面
'''
import time

from selenium import webdriver

from Test.AddColumn import AddColumn
from Test.HtmlRelation import HtmlRelation
from Test.WangmarketLoginPage import WangmarketLoginPage


class WebTest(object):
    def __init__(self):
        print('')

    def getType2(self):
        type_2 = 'landscape-grass7b82|case-cateb25b|about|gallery-all7b82|sports-grass|g3|commercialb159|landscape-grassb159|index354c|case-cate7b82|news-all7b82|c3dbe0|sports-grass7b82|c17b82|customized|artificial_plant_wall|gallery-all|case-cateefee|interlocking-floor|c1b159|case-cateb159|c2|gallery-alldbe0|artificial_plant_wallb159|c37b82|gallery-all8782|news|gallery-all6bbc|case-cate8782|customizedb159|sports|interlocking-floorb159|g1|landscape-grass|c18782|c3b159|product|g37b82|installation-supplies|sports7b82|installation-suppliesb159|c3|case-cate6bbc|gallery-allb159|g1b159|gallery|c1dbe0|sports8782|c1|sportsb159|g17b82|sports-grassb159|case-cate8362|news-allb159|case-catedbe0|case-cate|g3b159'
        type_2_list = type_2.split('|')
        # print('type-2:%s' % (type_2_list))
        return  type_2_list
    def getType3(self):
        type_3 = '1318|1268|commercial-flooring-skyjade-b|football-green-super-u|premium-s|sj-6810|tennis-turf|sj-52121|natalie-d|1590|lily-tower-pine|dense-su|1321|sj-8304|single-layer-dm-series-interlocking-floor|1327|1675|1322|index-4|contact|case-cate1a82|c38782|winter-du|1581|1700|football-grass-royal-x|super-w|milan-441-1|1693|commercial-flooring-skyjade-m|lux|sj-8401|sj-8201|commercial-flooring-skyjade-y|1317|1694|wooden-pattern-basketball-flooring|customized-pvc-flooring|cherry-green|football-green-super-d|1679|1676|1323|g-pe|cherry-blue|1698|pop-fur-5-0t|brackets-type-interlocking-floor|football-grass-super-s-w|1585|sj-8501|competition-wood|paradise-mu|1667|train-sand-badminton-flooring|sj-8303|sj-6811|1587|commercial-flooring-skyjade-r|football-green-royal-t|eco-new|1688|sj-5602|spring-u|1669|sj-6813|football-grass-max-s|baseball-grass|double-layer-series-interlocking-floor|faq|1672|1325|sj-102|lotus-pink|1687|dense-d|125th-canton-fair|wpc-decking1|lotus-purple|cherry-pink|1737|1697|milan-441-5|1691|maple-leaves|football-grass-eco-t|clover|1589|summer-lu|sj-8203|news-all|artificial_plant_wall7b82|1592|train-grid-4-5t|colorful-grass|sj-8502|1696|golf-putting-green|rose-leaves|milan-441-4|1202|sports-pvc-flooring-rolled-type|sj-8301|premium-w|1677|sj-8101|sj-6819|1680|1678|install|pp-materials-suspended-sports-flooring-outdoor|football-grass-super-swu|1702|personalized-customization-series|sj-58221-pop-fur|1695|natural-m|1326|1673|1320|artificial-grass-installation-tools|competion-gem-pattern-multi-sport|1588|124th-canton-fair-artificial-grass-skyjade|dense-su2|football-green-super-w|1666|1582|sj-6812|sj-8403|football-green-super-s|1319|sj-402|train-sand-4-5mm|1584|luxury|sj-303|1699|1685|1690|1671|sj-10121|1324|sj-301|rhododendron-purple|non-infill-grass|paradise-u|install-details|commercial-flooring-skyjade-s|sj-202|1586'
        type_3_list = type_3.split('|')
        # print('type-3:%s' % (type_3_list))
        return  type_3_list

    def getType2ColumnHtmlNameList(self):
        column_html_name_list = []
        column_html_name_list.append('%s' % ('index'))
        column_html_name_list.append('%s' % ('contact'))

        column_html_name_list.append('%s' % ('about'))
        column_html_name_list.append('%s' % ('faq'))
        column_html_name_list.append('%s' % ('c1'))
        column_html_name_list.append('%s' % ('c2'))
        column_html_name_list.append('%s' % ('c3'))
        column_html_name_list.append('%s' % ('news'))
        column_html_name_list.append('%s' % ('product'))

        column_html_name_list.append('%s' % ('artificial_plant_wall'))
        column_html_name_list.append('%s' % ('gallery'))
        column_html_name_list.append('%s' % ('installation-supplies'))
        column_html_name_list.append('%s' % ('landscape-grass'))
        column_html_name_list.append('%s' % ('sports-grass'))
        column_html_name_list.append('%s' % ('c18782'))
        column_html_name_list.append('%s' % ('interlocking-floor'))
        column_html_name_list.append('%s' % ('commercialb159'))
        return  column_html_name_list

    def getType3ColumnHtmlNameList(self):
        column_html_name_list = []
        column_html_name_list.append('%s' % ('football-grass-eco-t'))
        column_html_name_list.append('%s' % ('index'))
        column_html_name_list.append('%s' % ('football-grass-super-swu'))
        column_html_name_list.append('%s' % ('football-green-super-d'))
        column_html_name_list.append('%s' % ('super-w'))
        column_html_name_list.append('%s' % ('football-green-super-w'))
        column_html_name_list.append('%s' % ('football-green-super-u'))
        column_html_name_list.append('%s' % ('football-grass-max-s'))
        column_html_name_list.append('%s' % ('baseball-grass'))
        column_html_name_list.append('%s' % ('football-grass-super-s-w'))
        column_html_name_list.append('%s' % ('football-grass-royal-x'))
        column_html_name_list.append('%s' % ('faq'))
        column_html_name_list.append('%s' % ('football-green-royal-t'))
        column_html_name_list.append('%s' % ('football-green-super-s'))
        #zhongjian1
        column_html_name_list.append('%s' % ('sj-8501'))
        column_html_name_list.append('%s' % ('sj-8502'))
        column_html_name_list.append('%s' % ('sj-6811'))
        column_html_name_list.append('%s' % ('sj-6819'))
        column_html_name_list.append('%s' % ('sj-6810'))
        column_html_name_list.append('%s' % ('sj-8401'))
        column_html_name_list.append('%s' % ('sj-10121'))
        column_html_name_list.append('%s' % ('sj-6813'))
        column_html_name_list.append('%s' % ('sj-8403'))
        column_html_name_list.append('%s' % ('sj-8304'))
        column_html_name_list.append('%s' % ('sj-6812'))
        column_html_name_list.append('%s' % ('customized-pvc-flooring'))
        column_html_name_list.append('%s' % ('personalized-customization-series'))
        column_html_name_list.append('%s' % ('sj-8501'))
        column_html_name_list.append('%s' % ('sj-6811'))
        column_html_name_list.append('%s' % ('sj-6819'))
        column_html_name_list.append('%s' % ('sj-6810'))
        column_html_name_list.append('%s' % ('sj-8401'))
        column_html_name_list.append('%s' % ('sj-10121'))
        column_html_name_list.append('%s' % ('sj-6813'))
        column_html_name_list.append('%s' % ('sj-8403'))
        column_html_name_list.append('%s' % ('sj-6812'))
        column_html_name_list.append('%s' % ('customized-pvc-flooring'))
        column_html_name_list.append('%s' % ('personalized-customization-series'))
        column_html_name_list.append('%s' % ('sj-8501'))
        column_html_name_list.append('%s' % ('sj-6811'))
        column_html_name_list.append('%s' % ('sj-6819'))
        column_html_name_list.append('%s' % ('sj-6810'))
        column_html_name_list.append('%s' % ('sj-8401'))
        column_html_name_list.append('%s' % ('sj-10121'))
        column_html_name_list.append('%s' % ('sj-6813'))
        column_html_name_list.append('%s' % ('sj-8403'))
        column_html_name_list.append('%s' % ('sj-8304'))
        column_html_name_list.append('%s' % ('sj-6812'))
        column_html_name_list.append('%s' % ('1678'))
        column_html_name_list.append('%s' % ('natural-m'))
        column_html_name_list.append('%s' % ('paradise-mu'))
        column_html_name_list.append('%s' % ('eco-new'))
        column_html_name_list.append('%s' % ('1676'))
        column_html_name_list.append('%s' % ('dense-d'))
        column_html_name_list.append('%s' % ('dense-su2'))
        column_html_name_list.append('%s' % ('summer-lu'))
        column_html_name_list.append('%s' % ('1675'))
        column_html_name_list.append('%s' % ('spring-u'))
        column_html_name_list.append('%s' % ('dense-su'))
        column_html_name_list.append('%s' % ('paradise-u'))
        column_html_name_list.append('%s' % ('pop-fur-5-0t'))
        column_html_name_list.append('%s' % ('sj-5602'))
        column_html_name_list.append('%s' % ('train-grid-4-5t'))
        column_html_name_list.append('%s' % ('train-sand-4-5mm'))
        column_html_name_list.append('%s' % ('sj-52121'))
        column_html_name_list.append('%s' % ('sj-102'))
        column_html_name_list.append('%s' % ('sj-202'))
        column_html_name_list.append('%s' % ('1737'))
        column_html_name_list.append('%s' % ('commercial-flooring-skyjade-b'))
        column_html_name_list.append('%s' % ('sj-301'))
        column_html_name_list.append('%s' % ('competition-wood'))
        column_html_name_list.append('%s' % ('sj-402'))
        column_html_name_list.append('%s' % ('1592'))
        column_html_name_list.append('%s' % ('1268'))
        column_html_name_list.append('%s' % ('1590'))
        column_html_name_list.append('%s' % ('install'))
        column_html_name_list.append('%s' % ('1581'))
        column_html_name_list.append('%s' % ('1589'))
        column_html_name_list.append('%s' % ('1586'))
        column_html_name_list.append('%s' % ('1587'))
        column_html_name_list.append('%s' % ('artificial-grass-installation-tools'))
        column_html_name_list.append('%s' % ('1588'))
        column_html_name_list.append('%s' % ('install-details'))
        column_html_name_list.append('%s' % ('1582'))
        column_html_name_list.append('%s' % ('1584'))
        column_html_name_list.append('%s' % ('1585'))
        column_html_name_list.append('%s' % ('pop-fur-5-0t'))
        column_html_name_list.append('%s' % ('sj-5602'))
        column_html_name_list.append('%s' % ('competition-wood'))
        column_html_name_list.append('%s' % ('double-layer-series-interlocking-floor'))
        column_html_name_list.append('%s' % ('train-sand-4-5mm'))
        column_html_name_list.append('%s' % ('brackets-type-interlocking-floor'))
        column_html_name_list.append('%s' % ('1737'))
        column_html_name_list.append('%s' % ('commercial-flooring-skyjade-b'))
        column_html_name_list.append('%s' % ('sj-301'))
        column_html_name_list.append('%s' % ('single-layer-dm-series-interlocking-floor'))
        column_html_name_list.append('%s' % ('commercial-flooring-skyjade-y'))
        column_html_name_list.append('%s' % ('sj-402'))
        column_html_name_list.append('%s' % ('natalie-d'))
        column_html_name_list.append('%s' % ('winter-du'))
        column_html_name_list.append('%s' % ('lux'))
        column_html_name_list.append('%s' % ('1666'))


        return column_html_name_list
    def getColumnType2Type3Over(self):
        column_type2_type3_over = []
        column_type2_type3_over.append('index')
        column_type2_type3_over.append('product')
        str = 'landscape-grass7b82|case-cateb25b|about|gallery-all7b82|sports-grass|g3|commercialb159|landscape-grassb159|index354c|case-cate7b82|news-all7b82|c3dbe0|sports-grass7b82|c17b82|customized|artificial_plant_wall|gallery-all|case-cateefee|interlocking-floor|c1b159|case-cateb159|c2|gallery-alldbe0|artificial_plant_wallb159|c37b82'
        ss_list = str.split('|')
        column_type2_type3_over.extend(ss_list)
        column_type2_type3_over.append('c3')
        column_type2_type3_over.append('sports')
        column_type2_type3_over.append('sportsb159')
        column_type2_type3_over.append('news')
        column_type2_type3_over.append('c1')
        column_type2_type3_over.append('case - cate8782')
        column_type2_type3_over.append('installation-supplies')
        str2 ='interlocking-floorb159|case-cate8362|g17b82|gallery-allb159|c3b159|c18782|c1dbe0|news-allb159|g1|customizedb159|landscape-grass|installation-suppliesb159|g37b82|sports7b82|g3b159|sports8782|gallery-all6bbc|case-catedbe0|gallery-all8782|gallery|sports-grassb159|case-cate'
        ss_list2 = str2.split('|')
        column_type2_type3_over.extend(ss_list2)
        return  column_type2_type3_over

    def getDoTytpe2List(self):
        do_type2_list = list(set(self.getType2()).difference(set(self.getType2ColumnHtmlNameList())))
        print(len(do_type2_list))
        print(do_type2_list)

    def openAddColumnPage(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.delete_all_cookies()
        login_page = WangmarketLoginPage(driver)
        login_page.run()
        addColumn = AddColumn(driver)
        return driver,addColumn

    def addDoType2List(self):
        driver,addColumn = self.openAddColumnPage()
        for do_type2 in self.getDoTytpe2List():
            driver.refresh()
            addColumn.run()
            addColumn.setType2ColumnInfos(do_type2)
            addColumn.clickType2Button()
            print(do_type2)
            time.sleep(1)

    def addDoType2(self):
        driver, addColumn = self.openAddColumnPage()
        driver.refresh()
        addColumn.run()
        addColumn.setType2ColumnInfos('commercial')
        addColumn.clickType2Button()

    def addDoType3List(self,driver, addColumn,parent_page_name,type3_page_list):

        over_type3_list = self.getType3ColumnHtmlNameList()
        do_type3_list = list(set(type3_page_list).difference(set(over_type3_list)))
        print('*' * 32)
        for do_type3 in do_type3_list:
            driver.refresh()
            try:
                addColumn.run()
                addColumn.setType3ColumnInfos(parent_page_name, do_type3)
                addColumn.clickType3Button()
                over_type3_list.append(do_type3)
                print("column_html_name_list.append('%s' % ('" + do_type3 + "'))")
            except ValueError:
                print('%s:%s  ===error' %(do_type3,parent_page_name))
                driver.refresh()
            time.sleep(0.2)

        print('*'*32)

    def getType3ListByParentName(self,name):
        html_name_list = []
        outputDir = r'E:\\temp-dev\\web-fenlei'
        inpputDir = r'E:\\temp-dev\\SKYJADE1.1\\'
        htmlRelation = HtmlRelation(inpputDir, outputDir)
        old_html_name_list = htmlRelation.getHtmlList('page_%s.html' % (name), 0)
        for html_name in old_html_name_list:
            html_name_list.append(html_name.replace('"', '').replace('page_', ''))
        print('all:%s' % (html_name_list))
        do_html_name_list = list(set(html_name_list).difference(set(self.getType3ColumnHtmlNameList())))
        print('do:%s' % (do_html_name_list))
        do_type3_list = []
        for do_html_name in do_html_name_list:
            do_html_name_old = do_html_name
            do_html_name = do_html_name.replace('.html', '')
            if self.getType3().count(do_html_name) > 0:
                do_type3_list.append(do_html_name)
            elif self.getType2().count(do_html_name) > 0:
                continue

        return  list(set(do_type3_list).difference(set(self.getType3ColumnHtmlNameList())))

    def type2_type3_list(self):
        do_type2_type3_list = list(set(webTest.getType2()).difference(set(webTest.getColumnType2Type3Over())))
        print_type2_type3_list = []
        parent_name_plus = ''
        # do_type2_type3_list = []
        # do_type2_type3_list.append('news-all7b82')
        for parent_page_name in do_type2_type3_list:
            # parent_page_name = 'product'
            try:
                parent_name_plus = parent_name_plus + '|' + parent_page_name
                print('parent_name_plus: %s' % (parent_name_plus))
                print('parent_page_name: %s' % (parent_page_name))
                do_type3_list = webTest.getType3ListByParentName(parent_page_name)
                print('%s: %s' % (len(do_type3_list), do_type3_list))
                # type3_page_list = []
                # type3_page_list.append('football-grass-eco-t')
                webTest.addDoType3List(driver, addColumn, parent_page_name, do_type3_list)
                print_type2_type3_list.append(parent_page_name)
            except ValueError:
                print('%s  ===error' % (parent_page_name))
                for type2_type3_name in print_type2_type3_list:
                    print("column_html_name_list.append('%s' % ('" + type2_type3_name + "'))")

        print('*' * 32)
        for type2_type3_name in print_type2_type3_list:
            print("column_html_name_list.append('%s' % ('" + type2_type3_name + "'))")

    def type2_type3_simple(self,driver, addColumn,parent_name,parent_page_name):
        try:
            do_type3_list = webTest.getType3ListByParentName(parent_page_name)
            print('%s: %s' % (len(do_type3_list), do_type3_list))
            webTest.addDoType3List(driver, addColumn, parent_name, do_type3_list)
        except ValueError:
            print('%s  ===error' % (parent_page_name))
        print('*' * 32)


if __name__=='__main__':
     webTest = WebTest()
     driver, addColumn = webTest.openAddColumnPage()

     parent_name = 'news'
     parent_page_name = 'news-all7b82'
     webTest.type2_type3_simple(driver, addColumn,parent_name,parent_page_name)
































