import http
import urllib.request, time, random

def webBrowser(url, header, tm):
    req = urllib.request.Request(url, headers = header)
    try:
        webPage = urllib.request.urlopen(req)
        data = webPage.read()
        time.sleep(tm)
        #information of web page
        print(type(webPage))
        print(webPage.geturl())
        #print(webPage.info())
        #print(webPage.getcode())
    except urllib.error.URLError as err:
        print(err)
    except urllib.error.HTTPError as err:
        print(err)
    except http.client.HTTPException as err:
        print(err)

def rand_url():
    #web list
    url_list = ['http://129.226.227.171/flush/officelynn']
    return url_list[random.randint(0, len(url_list)-1)] 

def rand_headers():
    #user_agent list
    user_agent_list = ['Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
        'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
        'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
        'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
    header = {'user-agent':user_agent_list[random.randint(0, len(user_agent_list)-1)]}
    return header


tm = 10;   #wait time(sec) for per web
idx = 0;  #loop count
tm_per_h = 30; #wait time(sec) for every 150 loops
while True:
    url = rand_url()
    header = rand_headers()
    webBrowser(url, header, tm)
    idx = idx+1
    if (idx+1)%150 == 0:
        time.sleep(tm_per_h)