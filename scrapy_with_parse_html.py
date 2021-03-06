import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

# request params:
# CategoryId=808
# CategoryType=SiteHome
# ItemListActionName=PostList
# PageIndex=3
# ParentCategoryId=0
# TotalPostCount=4000

def getHtml(url, values):
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'User-Agent':user_agent}
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url + '?' + data).read()
    html = response_result.decode('utf-8')

    return html


def sendHttpRequest(index):
    print('http request')
    url = 'http://www.cnblogs.com/mvc/AggSite/PostList.aspx'
    value = {
        'CategoryId':808,
        'CategoryType' : 'SiteHome',
        'ItemListActionName' :'PostList',
        'PageIndex' : index,
        'ParentCategoryId' : 0,
        'TotalPostCount' : 4000
    }

    result = getHtml(url, value)
    return result


def htmlParser(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'post_item_body'}, limit=20)

    for item in all_div:
        analyzeBlog(item)


# item = <class 'bs4.element.Tag'>
def find_all(item, attr, c):
    return item.find_all(attr, attrs={'class': c}, limit=1)


# get blog article title and link
def getBlogTitleAndLink(item, result):
    a_title = find_all(item, 'a', 'titlelnk')

    if a_title is not None:
        result["title"] = a_title[0].string
        result["href"] = a_title[0]["href"]


# get blog article summary
def getBlogSummary(item, result):
    p_summary = find_all(item, 'p', 'post_item_summary')

    if p_summary is not None:
        result["summary"] = p_summary[0].text


def analyzeBlog(item):
    result = {}
    getBlogTitleAndLink(item, result)
    getBlogSummary(item, result)
    print(result)


if __name__ == "__main__":
    html_data = sendHttpRequest(1)
    # print(html_data)
    htmlParser(html_data)
