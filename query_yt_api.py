from googleapiclient.discovery import build
import re
from datetime import timedelta

'''
Installing Google API Client

pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
dev\Scripts\pip.exe install google-api-python-client


https://developers.google.com/youtube/v3/docs/?apix=true


Use channels resource to get contentDetails, which contains the channel id, e.g. 'id': 'UCA_bnmQSuS-_J2VDzbl5uDg'
Use playlists resource to get ..
Use playlistItems resource to get video details.  Includes videoid which can then be used as follows:
+ https://www.youtube.com/watch?v=u-SXLaQGg50


SETUP:
+ https://youtu.be/th5_9woFJmk?t=479



'''
api_key = 'AIzaSyBrPr9-jetMN0dI4-UJQdF4ULUvXIDz6M0'

youtube = build('youtube', 'v3', developerKey=api_key)

def output_total_seconds_nicely(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

def output_subscriptions_info(channel_id, output_file, is_one_line):

    try:
        # output playlist items to csv or txt file
        f = open(output_file, "w")

        #need to handle long playlist where they are paged by 50 items
        nextPageToken = None
        while True:

            #call the playlists module to get 
            sub_request = youtube.subscriptions().list(
                part='contentDetails,snippet',
                channelId=channel_id,
                maxResults=50,
                pageToken=nextPageToken
            )
            sub_response = sub_request.execute()

            i = 1
            for item in sub_response['items']:
                sub_channel_id = item['snippet']['resourceId']['channelId']
                sub_title = item['snippet']['title']
                sub_desc = item['snippet']['description']

                if is_one_line:
                    f.write(f'"{sub_title}","{sub_desc}",https://www.youtube.com/channel/{sub_channel_id}\n')

                else:
                    f.write(f'order: {i}\n')
                    f.write(f'title: {sub_title}\n')
                    f.write(f'date: {sub_desc}\n')
                    f.write(f'https://www.youtube.com/channel/{sub_channel_id}\n')
                    #f.write(f'description:\n {video_desc}\n')               
                    f.write('---\n')

                i += 1

            nextPageToken = sub_response.get('nextPageToken')
            if not nextPageToken:
                break

    except Exception as e:
        print(e)
    finally:
        f.close()

def dump_subscriptions_info(channel_id):
    #call the channels module to get stuff
    ch_request = youtube.subscriptions().list(
        part='contentDetails,snippet',
        channelId=channel_id,
        maxResults=50,
    )
    dict_response = ch_request.execute()
    with open("subscriptions.json", "w") as outfile:
        outfile.write(str(dict_response))

def output_channel_info(username):
    #call the channels module to get stuff
    ch_request = youtube.channels().list(
        part='contentDetails',
        forUsername=username
    )
    dict_response = ch_request.execute()
    with open("channel.json", "w") as outfile:
        outfile.write(str(dict_response))

    channel_id = dict_response['items'][0]['id']
    if channel_id is None:
        print("ID is null!!!")
    return channel_id

def output_playlist_info(channel_id, output_file, is_one_line=False):

    '''
    # output to json file
    with open("playlists.json", "w") as outfile:
        outfile.write(str(pli_response))
    '''
    try:
        # output playlist items to csv or txt file
        f = open(output_file, "w")

        #need to handle long playlist where they are paged by 50 items
        nextPageToken = None
        while True:

            #call the playlists module to get 
            pl_request = youtube.playlists().list(
                part='contentDetails,snippet',
                channelId=channel_id,
                maxResults=50,
                pageToken=nextPageToken
            )
            pli_response = pl_request.execute()

            for item in pli_response['items']:
                playlist_id = item['id']
                playlist_title = item['snippet']['title']
                playlist_date = item['snippet']['publishedAt']


                if is_one_line:
                    f.write(f'"{playlist_title}",{playlist_date},https://www.youtube.com/playlist?list={playlist_id}\n')

                else:
                    f.write(f'title: {playlist_title}\n')
                    f.write(f'date: {playlist_date}\n')
                    f.write(f'https://www.youtube.com/playlist?list={playlist_id}\n')
                    #f.write(f'description:\n {video_desc}\n')               
                    f.write('\n')

            nextPageToken = pli_response.get('nextPageToken')
            if not nextPageToken:
                break

    except Exception as e:
        print(e)
    finally:
        f.close()

def output_playlist_items(playlist_id):
    #call the playlistItems resource
    pli_request = youtube.playlistItems().list(
        part='contentDetails,snippet',
        playlistId=playlist_id
    )
    pli_response = pli_request.execute()

    with open("items.json", "w") as outfile:
        outfile.write(str(pli_response))

def get_video_duration(id):
    # get video duration 
    vid_request = youtube.videos().list(
        part='contentDetails',
        id=id
    )
    vid_response = vid_request.execute()
    vid_dur = vid_response['items'][0]['contentDetails']['duration']
    video_seconds = parse_youtube_video_duration(vid_dur)
    return output_total_seconds_nicely(video_seconds)


'''
https://www.youtube.com/watch?v=u-SXLaQGg50
'''
def output_playlist_items_info(playlist_id, output_file, is_one_line=False ):
    
    try:
        f = open(output_file, "w")

        #need to handle long playlist where they are paged by 50 items
        nextPageToken = None
        while True:


            #call the playlistItems resource
            pli_request = youtube.playlistItems().list(
                part='contentDetails,snippet',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=nextPageToken
            )
            pli_response = pli_request.execute()

            for item in pli_response['items']:
                video_index = item['snippet']['position']
                video_id = item['contentDetails']['videoId']
                video_title = item['snippet']['title']
                #video_desc = item['snippet']['description']
                video_date = item['contentDetails']['videoPublishedAt']
                video_duration = get_video_duration(video_id)

                if is_one_line:
                    f.write(f'{video_index},"{video_title}",{video_date},{video_duration},https://www.youtube.com/watch?v={video_id}\n')

                else:

                    f.write(f'{video_index}.\n')   
                    f.write(f'title: {video_title}\n')
                    f.write(f'date: {video_date}\n')
                    f.write(f'duration: {video_duration}\n')
                    f.write(f'https://www.youtube.com/watch?v={video_id}\n')
                    #f.write(f'description:\n {video_desc}\n')
                    f.write('\n')
            
            nextPageToken = pli_response.get('nextPageToken')
            if not nextPageToken:
                break
    except Exception as e:
        print(e)
    finally:
        f.close()

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

# e.g. PT23M1S
def parse_youtube_video_duration(encoded_duration):

    hours_match = hours_pattern.search(encoded_duration)
    minutes_match = minutes_pattern.search(encoded_duration)
    seconds_match = seconds_pattern.search(encoded_duration)

    hours = int(hours_match.group(1)) if hours_match else 0
    minutes = int(minutes_match.group(1)) if minutes_match else 0
    seconds = int(seconds_match.group(1)) if seconds_match else 0

    # concert all to secs
    video_seconds = timedelta(
        hours=hours,
        minutes=minutes,
        seconds=seconds
    ).total_seconds()

    return int(video_seconds)

def calculate_playlist_duration(playlist_id):
    
    total_seconds = 0

    #need to handle long playlist where they are paged by 50 items
    nextPageToken = None
    while True:

        #call the video resource
        pli_request = youtube.playlistItems().list(
            part='contentDetails,snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        )
        pli_response = pli_request.execute()

        vid_ids = []
        for item in pli_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])

        # need to pass comma separated string of items
        ids = ','.join(vid_ids)

        vid_request = youtube.videos().list(
            part='contentDetails',
            id=ids
        )
        vid_response = vid_request.execute()

        for item in vid_response['items']:
            vid_dur = item['contentDetails']['duration']
            total_seconds += parse_youtube_video_duration(vid_dur)

        # returns None when there are no more page
        nextPageToken = pli_response.get('nextPageToken')

        if not nextPageToken:
            break
    
    print(output_total_seconds_nicely(total_seconds))

# Get channel id by username
# is outputted to channel.json
#output_channel_info('clone278')
#output_subscriptions_info('UCA_bnmQSuS-_J2VDzbl5uDg', f'subscriptions/clone278.txt', False)
#dump_subscriptions_info('UCA_bnmQSuS-_J2VDzbl5uDg')
# Get playlist into by channel id
# is outputted to playlists.json
output_filename = 'Programming with Mosh.csv' # DEFAULT 'playlist.txt'
#output_playlist_info("UCWv7vMbMWH4-V0ZXdmDpPBA", f'playlists/{output_filename}', True)


'''
A level: OCR Specification Order
Craig'n'Dave
162 videos 1,627,344 views Last updated on 26 Jan
https://www.youtube.com/playlist?list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da

'''

playlist_id = 'PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da'
output_filename = 'CraignDave - A level - OCR videos' # DEFAULT 'playlist.txt'
#output_playlist_items(playlist_id)
output_playlist_items_info(playlist_id, f'playlistitems/{output_filename}.csv', True)

#calculate_playlist_duration(playlist_id)