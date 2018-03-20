import urllib.parse
import urllib.request

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


def writeFile(data):
    html_file = open('blog.html', 'w')
    html_file.write(data)
    html_file.close()

if __name__ == "__main__":
    html_data = sendHttpRequest(1)
    writeFile(html_data)
