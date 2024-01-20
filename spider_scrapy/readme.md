# Scrapy 

### Best Practice

1. 创建项目
    ```
    scrapy startproject project_name

    example: 
      scrapy startproject spider_scrapy
    ```

2. 创建爬虫
    ```
    cd project_name
    scrapy genspider name domain

    example: 
      scrapy genspider top250 douban.com
    ```

3. 通过 [scrapy shell](#ss) 分析网页
    ```
    item = response.css('div.item')
    name = item.css('span.title::text').get()
    ...
    ```
4. 编写代码
   * parse 方法
   * ...

5. 修改 settings (optinal)
   * USER_AGENT
   * ROBOTSTXT_OBEY
   * ...

6. middlewares 中间件 (optinal)
   * PROXY_LIST IP代理
   * ...

7. Splash Setup (optinal)
    * docker 启动 splash, [方法](https://splash.readthedocs.io/en/stable/install.html)
   * settings.py 配置 [Splash Setup](https://github.com/scrapy-plugins/scrapy-splash)
   * start_requests 方法中用SplashRequest 代替 scrapy.Request


8. 运行
    ```
    scrapy crawl `xxx` -o xxx.csv  

    example: scrapy crawl 'top250' -o top250.csv
    ```


<span id="ss"></span>

#### Scrapy Shell

1. fetch
  * 常规
  ```
  scrapy shell 'xxx'
  ```
  * useragent
  ```
  scrapy shell -s USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

  fetch('xxx')
  ```
  * splash
  ```
  scrapy shell -s USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

  fetch('http://127.0.0.1:8050/render.html?url=xxx')
  
  ```
  
2. css选择
  1 to select nodes, use nodename.clsssname
  2 to select text nodes, use ::text
  3 to select attribute values, use ::attr(name)
  4 get(),  getall() 
  5 example
    ```
    response.css('a.test').get()    //第一个
    response.css('a.test').getall()  //全部
    response.css('a.test::text').get()  //文本
    response.css("a::attr(href)").getall()  //属性1 ::attr(...)
    response.css('a.product-item-link').attrib['href']  //属性2 .attrib['href'] 
    response.css('spance.price::text').get().replace('$','')  //替换
    response.css('div.xxx').css('div.yyy').css('span::text').get()  //层级
    ```


3. 官网
   * [scrapy-doc](https://docs.scrapy.org/en/latest/topics/commands.html?#startproject)
   * [response-objects](https://docs.scrapy.org/en/latest/topics/request-response.html#response-objects)
   * [selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
