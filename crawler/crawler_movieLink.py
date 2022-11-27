from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行excel操作
import json
import time
import sys


def main():
    baseurl = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1,%E6%96%87%E8%89%BA&year_range=1990,2009&start="
    getData(baseurl)
    
    # 1.爬取网页
    # 2.解析数据
    # 3.保存数据

#影片链接详情的规则
findLink = re.compile(r'"url":"(.*?)"')

#爬取网页
def getData(baseurl):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("影片链接",cell_overwrite_ok=True)
    savepath = ".\\电影链接2.xls"
    head = {
        "User-Agent": 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40"
        ,"Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        ,"Cookie":
        'bid=7I-rYzk1EPA; douban-fav-remind=1; gr_user_id=34772c8b-ed56-4648-867b-d4dd73a16a70; ll="118201"; _vwo_uuid_v2=D57F7B1BBF696E264F8FBFBD6D7C423F9|2219c0f5ae12e35ada65afcbafb16807; __yadk_uid=MjoCvLOqpduB16zofKu7zWuPxrOn4YgC; __utmv=30149280.14158; douban-profile-remind=1; viewed="4340446_1420819_3174519_3287274_17787354_1908129_1088284_6901609_1495193_1981115"; __gads=ID=df069244b1b5c273:T=1594895338:S=ALNI_Ma1Z-NdknSdW3kJJCKvJfK718Dw9A; __utmz=30149280.1599365041.77.69.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_doumail_num=0; push_noty_num=0; __utmc=30149280; __utmc=223695111; __utmz=223695111.1599379561.34.31.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utma=30149280.1458371768.1582025015.1599385040.1599400018.81; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599401087%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.689888332.1582888588.1599385040.1599401087.37; __utmb=223695111.0.10.1599401087; __utmb=30149280.4.10.1599400018; _pk_id.100001.4cf6=1614b5320e535cb9.1582888583.37.1599403945.1599386889.'
    }
    datalist = []
    cnt = 0
    for i in range(52,100): #### range记得改！！！！！！
        url = baseurl + str(i*20)
        request = urllib.request.Request(url,headers=head)
        response = urllib.request.urlopen(request)
        data = response.read().decode('utf-8')
        data = str(data)
        link = re.findall(findLink,data)
        if(len(link)!=20):
            print(i)
            sys.exit()
        l = len(link)

        for j in range(0,l):
            datalist.append(link[j])
            sheet.write(cnt,0,datalist[cnt])
            cnt += 1
        time.sleep(5)
        print(cnt)
        print(time.ctime())
        book.save(savepath)



if __name__ == "__main__":
    main()