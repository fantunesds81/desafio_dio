import webbrowser
import re

def get_youtube_url():
    url = input("Enter your YouTube URL: ")
    if re.match(r'^https?://(www\.)?youtube\.com/watch\?v=', url):
        return url
    else:
        print("Invalid YouTube URL. Please try again.")
        return get_youtube_url()

youtube_url = get_youtube_url()
download_url = youtube_url[:12] + 'ss' + youtube_url[12:]
webbrowser.open(download_url)
