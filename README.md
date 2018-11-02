This script is used to download whole youtube videos from a youtube playlist. 

## Dependencies
```pip install pytube pafy youtube-dl```

## Run
```
python download.py folder_name download_url video_time_limited
```
An example here:
```
python download.py Tensorflow 'https://www.youtube.com/watch?v=MrijcdNl_U4&list=PL-XeOa5hMEYxNzHM7YLRjIwE1k3VQpqEh' 180
```
Argument Explanation:
- folder_name: it will create a folder to save all videos in current folder.
- download_url: the playlist url with ' '
- video_time_limited: the max length of videos, the unit is second.
