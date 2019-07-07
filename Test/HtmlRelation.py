# -*- coding: utf-8 -*-
'''
Test
2019-07-05 14:30 
PyCharm
页面
'''
import re

class HtmlRelation(object):
    def __init__(self, inputDir,outputDir):
        self.inputDir = inputDir
        self.outputDir = outputDir
        self.over_html_list = []
        self.ready_html_list = []
        self.result_dict = {}
        self.level = 0

    def runList(self,html_list):
        if len(html_list) < 1:
            return
        else:
            self.level = self.level + 1
            print('\n')
            for html_name in html_list:
                old_name = html_name
                html_name = html_name.replace('"','')
                self.runList(self.runHtml(html_name))
                html_list.remove(old_name)
                return



    def runHtml(self,html_name):
        if self.over_html_list.count(html_name) > 0:
            return []
        else:
            self.over_html_list.append(html_name)
            self.over_html_list = list(set(self.over_html_list))
            htmlpath = self.inputDir+html_name
            file = open(htmlpath, mode='r', encoding='utf-8')
            html_str = file.read()
            pattern = r'\"[^\"\'\/]{1,}.html\"'
            match_list = re.findall(pattern, html_str, re.I)
            match_list = list(set(match_list))
            if match_list.count('"'+html_name+'"') > 0:
                match_list.remove('"'+html_name+'"')
            print("%s|%s ： %s" % (html_name, len(match_list), match_list))
            file.close()
        return match_list


    def getHtmlList(self,html_path,i):

        try:
            htmlpath = self.inputDir + html_path
            file = open(htmlpath, mode='r', encoding='utf-8')
            html_str = file.read()
            pattern = r'\"[^\"\'\/]{1,}.html\"'
            match_list = re.findall(pattern, html_str, re.I)
            match_list = list(set(match_list))
            # print("%s:%s|%s ： %s" % (i, html_path, len(match_list), match_list))
            file.close()
        except ValueError as err:
            print(print("%s:%s|%s" % (i, html_path, err)))
        return match_list



