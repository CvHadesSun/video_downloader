from pytube import YouTube


def download_youtube_clip(url, download_folder):
    return YouTube(url).streams.filter(progressive=True, file_extension='mp4').first().download(
        output_path=download_folder)


def read_txt(txt_file):
    url_list = []
    with open(txt_file, "r") as fp:
        lines = fp.readlines()
        fp.close()
    for l in lines:
        url = l.rstrip()
        url_list.append(url)
    return url_list
