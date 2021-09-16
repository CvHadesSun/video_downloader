from lib import download_youtube_clip, read_txt
import os
from tqdm import tqdm

out_folder = '/Volumes/Samsung_T5/MOMO'
url_txt = '/Volumes/Samsung_T5/MOMO/url.txt'

# video_file = download_youtube_clip("https://www.youtube.com/watch?v=znH2chuO1k4",out_folder)

if __name__ == "__main__":
   assert os.path.isdir(out_folder)
   assert os.path.isfile(url_txt)
   #
   urls = read_txt(url_txt)
   for i in tqdm(len(urls)):
       _ = download_youtube_clip(urls[i],out_folder)
