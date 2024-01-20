import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path


class DoubanSpider():

    def __fetch_all_htmls(self):
        htmls = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }

        page_indexs = range(0, 250, 25)  # 构造分页列表

        for idx in page_indexs:
            url = "https://movie.douban.com/top250"
            if idx > 0:
                url += f"?start={idx}&filter="
            print(f"craw html: {url}")
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                raise Exception(f"error, code is:{r.status_code}")
            r.encoding = "utf-8"
            htmls.append(r.text)
        return htmls

    def __parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find("div", class_="article").find(
            "ol", class_="grid_view").find_all("div", class_="item")

        datas = []
        for item in items:
            img_url = item.find("div", class_='pic').find("img")['src']
            title = item.find("div", class_='info').find(
                "div", class_="hd").find("span", class_="title").get_text()
            print(f"title:{title} , img_url:{img_url}")
            data = {
                "title": title,
                "img_url": img_url
            }

            datas.append(data)
        return datas

    def crawler(self, output_file):
        htmls = self.__fetch_all_htmls()
        all_datas = []
        for html in htmls:
            data = self.__parse(html)
            all_datas.extend(data)
        df = pd.DataFrame(all_datas)
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_file, index=False)


if __name__ == '__main__':
    DoubanSpider().crawler("top250.csv")
