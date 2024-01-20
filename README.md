# POSTER_SPIDER
本项目会爬取 [豆瓣电影 Top 250](https://movie.douban.com/top250) 封面照片，合成 1张 6K 分辨率海报墙
![poster](res/poster_thumbnail.jpg)

## Running
运行项目根目录下的 poster.py, 成功后会在根目录生成文件`poster.jpg` 
The quick way:

```
python poster.py
```

## Requirements
```
pip install beautifulsoup4
pip install requests
pip install pandas 
pip install pillow
pip install scrapy
```


## Documents
1. `spider_scrapy` 和 `spider_bs4` 功能完全相同：爬取数据保存为 top250.csv
   * 单独运行 spider_scrapy
  
    ```
    cd spider_scrapy 
    scrapy crawl `top250` -o top250.csv 
    ```
   * 单独运行 spider_bs4
   ```
    cd spider_bs4
    python top250.py
   ```

2. `process.imagedownloader`   下载 top250.csv 中的图片
3. `process.imageprocessor` 合成 top250.csv 中的图片


## Scrapy

[Best Practice](spider_scrapy/readme.md)