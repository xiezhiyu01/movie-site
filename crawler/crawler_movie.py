from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式
import urllib.request,urllib.error #制定url，获取网页数据
import xlrd,xlwt #进行excel操作
import sqlite3 #进行SQlite数据库操作
import time
import sys


def main():
    getData()

#爬取网页
def getData():
    savepath = ".\\影片信息5.xls"
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("影片信息",cell_overwrite_ok=True)
    # col = ("电影标题","评分","简介","图片链接","演员名字","演员链接","影评")
    old_book = xlrd.open_workbook('电影链接合集.xls')
    old_sheet = old_book.sheet_by_name('Sheet1')
    for i in range(1048,1226):
    #for i in range(7,8):
        time.sleep(5)
        url = old_sheet.cell(i,0).value
        html = askURL(url)

        data = []
        soup = BeautifulSoup(html,"html.parser")
        title = soup.find('span',property="v:itemreviewed").string
        data.append(title)
        print(title)

        rating = soup.find('strong',property="v:average").string
        data.append(rating)
        #print(rating)

        summary = soup.find('div',class_='indent',id="link-report")
        shortSummary = summary.find('span',property="v:summary")
        fullSummary = summary.find('span',class_="all hidden")
        if(fullSummary):
            data.append(str(fullSummary))
            #print(fullSummary)
        else:
            data.append(str(shortSummary))
            #print(shortSummary)

        movie = soup.find('div',class_="subject clearfix")

        mainpic = movie.find('img')['src']
        data.append(mainpic)
        #print(mainpic)

        star_name_list = []
        star_link_list = []
        for star in movie.find_all('a',rel="v:starring"):
            if(str(star['href'])[1] == 'c'):
                star_name_list.append(star.string)
                star_link_list.append(star['href'])
                #print(star_name_list[-1])
                #print(star_link_list[-1])
                if(len(star_name_list)==10):
                    break
        data.append(star_name_list)
        data.append(star_link_list)

        commentList = []
        for comment in soup.find_all('div',class_="comment-item"):
            fullComment = comment.find('span',class_="hide-item full")
            comment = comment.find('span',class_="short")
            if fullComment:
                comment = fullComment
            comment = comment.string
            if comment:
                #print(comment)
                commentList.append(comment)
            if (len(commentList) == 5):
                break
        if(len(commentList)<5):
            print("Lack Comment!!!!!")
        data.append(commentList)

        #print(len(data))
        

        for j in range(0,7):
            sheet.write(i,j,str(data[j])) 
        book.save(savepath)
        


#得到一个指定url的网页内容
def askURL(url):
    head = {
        "User-Agent": 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40"
        ,"Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        ,"Cookie":
        'bid=7I-rYzk1EPA; douban-fav-remind=1; gr_user_id=34772c8b-ed56-4648-867b-d4dd73a16a70; ll="118201"; _vwo_uuid_v2=D57F7B1BBF696E264F8FBFBD6D7C423F9|2219c0f5ae12e35ada65afcbafb16807; __yadk_uid=MjoCvLOqpduB16zofKu7zWuPxrOn4YgC; __utmv=30149280.14158; douban-profile-remind=1; viewed="4340446_1420819_3174519_3287274_17787354_1908129_1088284_6901609_1495193_1981115"; __gads=ID=df069244b1b5c273:T=1594895338:S=ALNI_Ma1Z-NdknSdW3kJJCKvJfK718Dw9A; push_doumail_num=0; push_noty_num=0; __utmc=30149280; __utmc=223695111; __utmz=30149280.1599448753.84.70.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; __utmz=223695111.1599448753.40.33.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599453139%2C%22https%3A%2F%2Fsearch.douban.com%2Fmovie%2Fsubject_search%3Fsearch_text%3D%25E4%25BF%25A1%25E6%259D%25A1%26cat%3D1002%22%5D; _pk_id.100001.4cf6=1614b5320e535cb9.1582888583.41.1599453139.1599449809.; _pk_ses.100001.4cf6=*; __utma=30149280.1458371768.1582025015.1599448753.1599453139.85; __utmb=30149280.0.10.1599453139; __utma=223695111.689888332.1582888588.1599448753.1599453139.41; __utmb=223695111.0.10.1599453139'
    }
    url = url.replace('\\','')
    print(url)
    request = urllib.request.Request(url=url,headers=head) 

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()