# README

This is a simple movie retrieval website built by Django, containing information about 1,000 movies and their actors. The data comes from https://www.douban.com/ and is obtained by python crawler.

## Overview

* Movie list

![屏幕截图(8)](C:\Users\XieZhiyu\Pictures\Screenshots\屏幕截图(8).png)



![屏幕截图(9)](C:\Users\XieZhiyu\Pictures\Screenshots\屏幕截图(9).png)

* Actor list

![屏幕截图(11)](C:\Users\XieZhiyu\Pictures\Screenshots\屏幕截图(11).png)

* Movie information page

![](C:\Users\XieZhiyu\Pictures\Screenshots\微信图片_20200912102436.jpg)

* Actor information page

![微信图片_20200912102759](C:\Users\XieZhiyu\Pictures\Screenshots\微信图片_20200912102759.jpg)

* Search movies by actor name:

![微信图片_20200912103806](C:\Users\XieZhiyu\Pictures\Screenshots\微信图片_20200912103806.png)

* Search actors by movie name:

![微信图片_20200912104046](C:\Users\XieZhiyu\Pictures\Screenshots\微信图片_20200912104046.png)

* Search movie review:

![微信图片_20200912104128](C:\Users\XieZhiyu\Pictures\Screenshots\微信图片_20200912104128.png)



* URLs
  * `/` 影视列表
  * `/explorecelebrity` 演员列表
  * `/movie/<int:id>` 影视信息页
  * `/celebrity/<int:id>` 演员信息页
  * `/search` 搜索结果页（eg. `/search/?keyword=aaa&option=comment&page=1`）

