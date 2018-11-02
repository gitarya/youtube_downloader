from pytube import Playlist
from pytube import YouTube
import os
import sys
import pafy



def download_url(link, dir, time_limited):
    '''
    link: the playlist url
    dir: the save path
    '''
    pl = Playlist(link)
    playlist_url = pl.parse_links()
    for i in range(len(playlist_url)):
        URL = "https://www.youtube.com" + playlist_url[i]
        video_length = pafy.new(URL).length
        if int(video_length) < int(time_limited):
            YouTube(URL).streams.first().download(dir)


if __name__ == '__main__':
    dir = './image/' + sys.argv[1]
    link = sys.argv[2]
    time_limited = sys.argv[3]
    if not os.path.exists(dir):
        os.makedirs(dir)
    download_url(link, dir, time_limited)
