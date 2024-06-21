import os
import re

from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import googleapiclient.errors

from datetime import timedelta

'''
Installing Google API Client

pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
dev\Scripts\pip.exe install google-api-python-client


# Ensure you have a valid API key by going to 
API key (mrblackie): AIzaSyAivmOAheHIxPsAFo4G3Rd_ujvxIWkgJwk

# Enable YT Data API v3 here: https://console.developers.google.com/apis/api/youtube.googleapis.com/overview?project=573100328637


# all APIs are here
https://developers.google.com/apis-explorer/#p/

# were are interested in the YT api as follows
https://developers.google.com/youtube/v3/docs/?apix=true




Installation
------------
pip install --upgrade google-api-python-client

Use channels resource to get contentDetails, which contains the channel id, e.g. 'id': 'UCA_bnmQSuS-_J2VDzbl5uDg'
Use playlists resource to get ..
Use playlistItems resource to get video details.  Includes videoid which can then be used as follows:
+ https://www.youtube.com/watch?v=u-SXLaQGg50


SETUP:
+ https://youtu.be/th5_9woFJmk?t=479



'''
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"

api_key = 'AIzaSyAivmOAheHIxPsAFo4G3Rd_ujvxIWkgJwk' #'AIzaSyBrPr9-jetMN0dI4-UJQdF4ULUvXIDz6M0'


# Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
# credentials = flow.run_console()
#youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
#youtube = build(api_service_name, api_version, developerKey=api_key)



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
                    f.write(f'number: {i}\n')
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

    results = dict_response['pageInfo']['totalResults']
    
    if results > 0:
    
        channel_id = dict_response['items'][0]['id']
        if channel_id is None:
            print("ID is null!!!")
        return channel_id
    
    with open("channel.json", "a") as outfile:
        outfile.write("\nNo results.")

    return 0

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
                    f.write(f'{video_index+1},{video_duration},"{video_title}",https://www.youtube.com/watch?v={video_id},{video_date}\n')

                else:

                    f.write(f'{video_index+1}.\n')   
                    f.write(f'duration: {video_duration}\n')
                    f.write(f'title: {video_title}\n')                   
                    f.write(f'https://www.youtube.com/watch?v={video_id}\n')
                    #f.write(f'description:\n {video_desc}\n')
                    f.write(f'date: {video_date}\n')
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


def do_all(get_channel_info, get_sub_info, dump_sub_info, get_playlist_info, get_playlist_items, get_playlist_items_info, calculate_playlist_duration):
    
    yt_username = '101Computing'
    
    # Get channel id by username
    # is outputted to channel.json
    if get_channel_info:
        output_channel_info({yt_username})
    
    
    channel_id = "UCWv7vMbMWH4-V0ZXdmDpPBA"  # 'UCA_bnmQSuS-_J2VDzbl5uDg' #clone278 UCWd6hxkb0CDrPSXVeSs86Zw
        
    if get_sub_info:
        output_subscriptions_info({channel_id}, f'subscriptions/{yt_username}.txt', False)
    
    if dump_sub_info:
        dump_subscriptions_info({channel_id})
          
    producer_name = "Programming with Mosh" 
        
    # Get playlist into by channel id
    # is outputted to playlists.json
    output_filename = f'{producer_name}.csv' # DEFAULT 'playlist.txt'
    
    if get_playlist_info:
        output_playlist_info({channel_id}, f'playlists/{output_filename}', True)


'''
Building a Social Media App With Django: Part 1 Landing Page and User Authentication
Legion Script - Building a Social Media App With Django
47,723 views  20 Dec 2020  Social Media Web App With Python 3 and Django
https://www.youtube.com/playlist?list=PLPSM8rIid1a3TkwEmHyDALNuHhqiUiU5A

Minecraft 1.19.3 - Forge Modding Tutorial: Workspace Setup | #1

Modding by Kaupenjoe
21.1K subscribers

https://www.youtube.com/watch?v=p-mp91zrlqo&list=PLKGarocXCE1FlLU16RRfaS0bcabHDSvLA

'''

playlist_id = 'PLKGarocXCE1FlLU16RRfaS0bcabHDSvLA'
output_filename = 'Modding by Kaupenjoe - Minecraft 1.19.3 - Forge Modding Tutorial' # DEFAULT 'playlist.txt'
#output_playlist_items(playlist_id)
output_playlist_items_info(playlist_id, f'playlistitems/{output_filename}.csv', True)

    if calculate_playlist_duration:
        calculate_playlist_duration(playlist_id)
        
    print("Mission complete.")
        
do_all(False, #get_channel_info
            False, #get_sub_info, 
            False, #dump_sub_info, 
            False, #get_playlist_info, 
            False, #get_playlist_items, 
            True, #get_playlist_items_info, 
            False) #calculate_playlist_duration)