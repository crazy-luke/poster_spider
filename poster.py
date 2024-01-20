from spider_bs4.top250 import DoubanSpider as Spider
from process.imagedownloader import ImageDownloader
from process.imageprocessor import ImageProcessor


def poster():
    csv_file = "work_dir/top250.csv"
    img_dir = "work_dir/download"

    Spider().crawler(csv_file)
    ImageDownloader(img_dir).download(csv_file)
    ImageProcessor(img_dir).create_poster(csv_file)


if __name__ == '__main__':
    poster()
