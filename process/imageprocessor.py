from PIL import Image
from pathlib import Path
import pandas as pd


class ImageProcessor():

    def __init__(self, img_dir='download'):
        self.__img_dir = img_dir

    def combine_poster(self, filepaths):
        print("combine_poster")
        w = 270
        h = 400
        total_w = w*25
        total_h = h*10
        new_poster = Image.new(mode="RGB", size=(total_w, total_h))
        for idx, fp in enumerate(filepaths):
            start_w = (idx % 25)*w
            start_h = (idx // 25)*h
            img = Image.open(fp)
            fpw, fph = img.size
            new_poster.paste(
                im=img, box=(start_w, start_h, start_w+fpw, start_h+fph))
        new_poster.save("poster.jpg")

    def create_poster(self, csv_file):
        print("create_poster start")
        df = pd.read_csv(csv_file)
        filepaths = []
        for i, item in df.iterrows():
            filepath = f"{self.__img_dir}/{Path(item[1]).name}"
            filepaths.append(filepath)
        self.combine_poster(filepaths)
        print("create_poster completed")
