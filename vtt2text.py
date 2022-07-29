import re
import datetime
import sys
import youtube_dl
import os

class Regexes:
    timeRegex = r"\d\d\:\d\d\:\d\d\.\d\d\d\s-->\s\d\d\:\d\d\:\d\d\.\d\d\d(.*)"
    titleRegex = r"WEBVTT\nKind: captions\nLanguage:.*\n"
    twoLineRegex = r"\n\n"
    unRegex1 = r"(\s)+\n"
    unRegex2 = r"\n"
    all = [timeRegex, titleRegex, twoLineRegex, unRegex1, unRegex2]

def download_subs(url, parent_folder):
    youtube_dl_options = {
        'writesubtitles': True, 
        'writeautomaticsub': True, 
        'youtube_include_dash_manifest': False,
        'skip_download': True,
        'outtmpl': f"{parent_folder}/%(title)s.%(ext)s"
    }

    with youtube_dl.YoutubeDL(youtube_dl_options) as youtube_dl_client:
        title = youtube_dl_client.extract_info(url)["title"]
        youtube_dl_client.download([url])

    return title

def substitute(path):
    with open(path, "r") as f:
        content = f.read()

    for regex in Regexes.all:
        content = re.sub(regex, "", content)

    return content.strip().split("\n")[0]

def overwrite(content, path):
    current_datetime = datetime.datetime.now().strftime("%d-%m-%Y")

    new_filename = f"{path[:len(path) - 7]}-{current_datetime}.txt"
    with open(new_filename, "x") as f:
        f.write(content)

def main():
    url = "https://youtu.be/GBvlMvivCnI"
    lang = "en"
    parent_folder = os.getcwd()
    title = download_subs(url, parent_folder)
    path = f"{parent_folder}/{title}.{lang}.vtt"
    content = substitute(path)
    overwrite(content, path)

main()
