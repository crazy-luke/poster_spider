from pathlib import Path
import requests
import pandas as pd


class ImageDownloader():
    def __init__(self, img_dir='download'):
        self.__img_dir = img_dir

    def __download(self, urls):
        Path(self.__img_dir).mkdir(parents=True, exist_ok=True)

        for url in urls:
            fp = f"{self.__img_dir}/{Path(url).name}"
            with open(fp, "wb") as f:
                print(f"download:{url} to {fp}")
                r = requests.get(url)
                f.write(r.content)

    def download(self, csv_file):
        df = pd.read_csv(csv_file)
        urls = []
        for i, item in df.iterrows():
            urls.append(item[1])
        self.__download(urls)
        print("download completed, total: {urls.count}")


if __name__ == '__main__':
    print("Test Downloader")
    ImageDownloader("../work_dir/download").download("../work_dir/top250.csv")
