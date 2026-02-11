

yt-dlp -x "https://www.youtube.com/watch?v=G6sOzBmxrLM" -o "/downloads/%(title)s.%(ext)s"
'''
https://www.spacebar.news/yt-dlp-best-way-to-download-videos-audio/
-o "D:\my_folder_location\%(upload_date)s\%(title)s [%(id)s].%(ext)s"



# Audio download with relative output path
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" -P "./downloads" "https://www.youtube.com/watch?v=Ah6kirkSwTg"


# Audio download best quality
yt-dlp -x --audio-format mp3 -f bestaudio "https://www.youtube.com/watch?v=Ah6kirkSwTg"

yt-dlp -o '~/Downloads/Tech/Abdul Kalam Biography' https://www.youtube.com/watch?v=t5b20oLaIaw
yt-dlp -o '~Downloads/%(uploader)/%(title)s/%(playlist)s.%(ext)s' https://www.youtube.com/watch?v=henyrE-izgY&list=PLA4uAeilYkMy9IYeOLjwQ-vw3Kbsjphxp


yt-dlp -v --cookies cookies.txt -o '~Downloads/' https://www.youtube.com/playlist?list=PLA4uAeilYkMyq0Q72KvnoJw2nzdM4_mV5

--cookies-from-browser chrome
--username  "clone278@gmail.com"  --password "1948V1nc3ntR4p1d3$3r13$C!"  
Un: clone278@gmail.com
Pw: 1948V1nc3ntR4p1d3$3r13$C!
yt-dlp --username 'clone278@gmail.com' --password '1948V1nc3ntR4p1d3$3r13$C!' -o '~Downloads/' https://www.youtube.com/playlist?list=PL-1Nqb2waX4XvCXzW2n6fj826P28IhEye


yt-dlp --cookies-from-browser firefox -o '~/Downloads/' https://www.youtube.com/playlist?list=PLCaa9Mqfv2ujyosinCMtAvmiP8nEZaO-z
yt-dlp -f "bestvideo+bestaudio/best" --cookies-from-browser firefox https://www.youtube.com/playlist?list=PLCaa9Mqfv2ujyosinCMtAvmiP8nEZaO-z


https://www.youtube.com/watch?v=dgOXKe2qkrg

yt-dlp -f bestaudio --cookies-from-browser firefox -o '~/downloads/%(title)s.%(ext)s' 'https://www.youtube.com/playlist?list=PLA4uAeilYkMzLU4Us41Gl1lePiyXutz52'
yt-dlp -f bestaudio --cookies-from-browser firefox "https://www.youtube.com/playlist?list=PLA4uAeilYkMzLU4Us41Gl1lePiyXutz52"
yt-dlp -x --audio-format mp3 -f bestaudio "https://www.youtube.com/watch?v=7hjJ-CVxhPk"



yt-dlp -f "bestvideo+bestaudio/best" https://www.youtube.com/watch?v=HVfE5bsWX5A



#### AUDIO ONLY DOWNLOADS ####
yt-dlp -x --audio-format mp3 -f bestaudio https://www.youtube.com/shorts/HiX8j287Rmw


'''

