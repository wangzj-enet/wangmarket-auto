# -*- coding: utf-8 -*-
'''
MainTest
2019-07-05 14:37 
PyCharm
页面
'''
import os

from Test.HtmlRelation import HtmlRelation

outputDir = r'E:\\temp-dev\\web-fenlei'
inpputDir = r'E:\\temp-dev\\SKYJADE1.1\\'
indexHtml = r'page_index.html'


print('*'*32)
htmlRelation = HtmlRelation(inpputDir,outputDir)
# index_list = []
# index_list.append(indexHtml)
# htmlRelation.runList(index_list)
# i = 0
# for file in os.listdir(inpputDir):
#     i = i+1
#     htmlRelation.getHtmlList(file,i)

type_3 = '1318|1268|commercial-flooring-skyjade-b|football-green-super-u|premium-s|sj-6810|tennis-turf|sj-52121|natalie-d|1590|lily-tower-pine|dense-su|1321|sj-8304|single-layer-dm-series-interlocking-floor|1327|1675|1322|index-4|contact|case-cate1a82|c38782|winter-du|commercial|1581|1700|football-grass-royal-x|super-w|milan-441-1|1693|commercial-flooring-skyjade-m|lux|sj-8401|sj-8201|commercial-flooring-skyjade-y|1317|1694|wooden-pattern-basketball-flooring|customized-pvc-flooring|cherry-green|football-green-super-d|1679|1676|1323|g-pe|cherry-blue|1698|pop-fur-5-0t|brackets-type-interlocking-floor|football-grass-super-s-w|1585|sj-8501|competition-wood|paradise-mu|1667|train-sand-badminton-flooring|sj-8303|sj-6811|1587|commercial-flooring-skyjade-r|football-green-royal-t|eco-new|1688|sj-5602|spring-u|1669|sj-6813|football-grass-max-s|baseball-grass|double-layer-series-interlocking-floor|faq|1672|1325|sj-102|lotus-pink|1687|dense-d|125th-canton-fair|wpc-decking1|lotus-purple|cherry-pink|1737|1697|milan-441-5|1691|maple-leaves|football-grass-eco-t|clover|1589|summer-lu|sj-8203|news-all|artificial_plant_wall7b82|1592|train-grid-4-5t|colorful-grass|sj-8502|1696|golf-putting-green|rose-leaves|milan-441-4|1202|sports-pvc-flooring-rolled-type|sj-8301|premium-w|1677|sj-8101|sj-6819|1680|1678|install|pp-materials-suspended-sports-flooring-outdoor|football-grass-super-swu|1702|personalized-customization-series|sj-58221-pop-fur|1695|natural-m|1326|1673|1320|artificial-grass-installation-tools|competion-gem-pattern-multi-sport|1588|124th-canton-fair-artificial-grass-skyjade|dense-su2|football-green-super-w|1666|1582|sj-6812|sj-8403|football-green-super-s|1319|sj-402|train-sand-4-5mm|1584|luxury|sj-303|1699|1685|1690|1671|sj-10121|1324|sj-301|rhododendron-purple|non-infill-grass|paradise-u|install-details|commercial-flooring-skyjade-s|sj-202|1586'
type_3_list = type_3.split('|')
print('type-3:%s' %(type_3_list))

type_2 = 'landscape-grass7b82|case-cateb25b|about|gallery-all7b82|sports-grass|g3|commercialb159|landscape-grassb159|index354c|case-cate7b82|news-all7b82|c3dbe0|sports-grass7b82|c17b82|customized|artificial_plant_wall|gallery-all|case-cateefee|interlocking-floor|c1b159|case-cateb159|c2|gallery-alldbe0|artificial_plant_wallb159|c37b82|gallery-all8782|news|gallery-all6bbc|case-cate8782|customizedb159|sports|interlocking-floorb159|g1|landscape-grass|c18782|c3b159|product|g37b82|installation-supplies|sports7b82|installation-suppliesb159|c3|case-cate6bbc|gallery-allb159|g1b159|gallery|c1dbe0|sports8782|c1|sportsb159|g17b82|sports-grassb159|case-cate8362|news-allb159|case-catedbe0|case-cate|g3b159'
type_2_list = type_2.split('|')
print('type-2:%s' %(type_2_list))

type_1 = 'index'
type_1_list = type_1.split('|')
print('type-1:%s' %(type_1_list))
print('*'*32)
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


html_name_list = []
old_html_name_list = htmlRelation.getHtmlList('page_%s.html' %('product'),0)
for html_name in old_html_name_list:
    html_name_list.append(html_name.replace('"','').replace('page_',''))
print('all:%s' %(html_name_list))
do_html_name_list = list(set(html_name_list).difference(set(column_html_name_list)))
print('do:%s' %(do_html_name_list))
do_type3_list = []
for do_html_name in do_html_name_list:
    do_html_name_old = do_html_name
    do_html_name = do_html_name.replace('.html','')
    if type_3_list.count(do_html_name) >0:
        do_type3_list.append(do_html_name)


print(len(list(set(do_type3_list).difference(set(column_html_name_list)))))
print(list(set(do_type3_list).difference(set(column_html_name_list))))












