import re
import string
from urllib import request
#断点调试
class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.2.7kf1tcl3b8e'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '</i>([\s\S]*?)</span>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        # print(root_html[0])
        anchors = []
        result = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            anchors.append(name)
            # number = re.findall(Spider.number_pattern,html)
        #     anchor = {'name':name,'number':number}
        # #     anchors.append(anchor)
        # res = r'\n([\s\S]*?)\n'
        results = []
        # print(anchors[0])
        for x in anchors:
            name = x[0]
            number = x[1]
            result = {'name':name,'number':number}
            results.append(result)
        return results

    def __refine(self,results):
        l = lambda res:{
            'name':res['name'].strip(),
            'number':res['number'].strip(),
        }
        return map(l,results)

        # print(results[0])
        # for x in anchors:
        #     r = re.findall(res,x)
        #     result.append(r)
        # print(result[0])

    def __sort(self,results):
        return sorted(results,key = self.__sort_seed,reverse = True)

    def __sort_seed(self,result):
        r = re.findall('(\d+(\.\d+)?)',result['number'])
        # print (r[0][0])
        number = float(r[0][0])
        if '万' in result['number']:
            number *= 10000
        return number

        # return result['number']

    def __show(self,results):
        for rank in range(0,len(results)):
            print('rank ' + str(rank + 1)
            + ' ：' + results[rank]['name']
            + '    ' + results[rank]['number'] )

        # for result in results:
        #     print(result['name'] + '------' +result['number']) 

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)
        # print(anchors)

spider = Spider()
spider.go()

# <div class = "video-info">包含主播姓名和观看人数</div>
#     <span class = "video-nickname">主播姓名</span>
#     <span class = "video-number">观看人数</span>