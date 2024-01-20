import scrapy


class Top250Spider(scrapy.Spider):
    name = "top250"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        items = response.css('div.item')
        for item in items:
            yield {
                'title': item.css('span.title::text').get(),
                'img': item.css('img::attr(src)').get()
            }

        next_page = response.css('span.next').css('a::attr(href)').get()
        if next_page is not None:
            next_url = f"{self.start_urls[0]}{next_page}"
            yield response.follow(next_url, callback=self.parse)
