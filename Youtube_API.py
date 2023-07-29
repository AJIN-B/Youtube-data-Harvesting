
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import googleapiclient.errors
from googleapiclient.errors import HttpError
import requests
import re


API_KEY = 'AIzaSyCaTjMuKjuY38AC7UDXskFJ6F9sEWLzzFc'

#%%

def get_channel_id(channel_link):
    
    if "@" in channel_link:
        channel_url = channel_link+"/about"
    
        response = requests.get(channel_url) # Send a GET request to the channel page
    
        channel_id_match = re.search(r'"channelId":"([A-Za-z0-9_-]+)"', response.text) # Extract the channel ID using regular expressions
    
        if channel_id_match:
            channel_id = channel_id_match.group(1)
    return  channel_id



def get_Channel_Information(all_id):
    
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    cha_res = youtube.channels().list(
                    part='contentDetails,snippet,statistics',
                    id=all_id).execute()
    ch_ti1 = []
    for i in cha_res['items']:
            ch_id = i['id']
            channel_link = f"https://www.youtube.com/channel/{ch_id}"
            ch_title = i['snippet']['title']
            ch_playlist = i['contentDetails']['relatedPlaylists']['uploads']
            CreatedAt = i['snippet']['publishedAt']
            Subcount = i['statistics']['subscriberCount']
            TotalViews = i['statistics']['viewCount']
            TotalVideos = i['statistics']['videoCount']
            ch_logo = i['snippet']['thumbnails']['medium']['url']
            ch_ti1.append({"Channel_id": ch_id,"Channel_Name": ch_title,"Playlist_id": ch_playlist,"Created_Date":CreatedAt,
                                                    "Subcribers":Subcount,"TotalViews":TotalViews,"TotalVideos":TotalVideos,
                                                    "Thumbnail":ch_logo,"Channel_link":channel_link})
        
    
    return ch_ti1[0]


def get_video_ids(playlist_id):
    
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    video_ids = []

    try:
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50  )

        counter = 0  # Counter for tracking the number of video IDs
        while request and counter < 100:  # Stop when 100 video IDs are obtained
            response = request.execute()
            for item in response['items']:
                video_ids.append(item['contentDetails']['videoId'])
                counter += 1
            request = youtube.playlistItems().list_next(request, response)

    except HttpError as e:
        error_message = e.content.decode("utf-8")
        print("An error occurred:", error_message)

    return video_ids[:50] 



def get_comments_data(vid_lis):
    
    youtube = build('youtube', 'v3', developerKey=API_KEY)
        
    comments = []
    for vids in vid_lis:
        try:
            ch_response = youtube.videos().list(
                part='snippet',
                id=vids).execute()

            for video in ch_response['items']:
                ch_id = video['snippet']['channelId']
                vid_title = video['snippet']["title"]
                Channel_title = video['snippet']["channelTitle"]

            response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=vids,
                maxResults=30,
            ).execute()
            
            video_comments = []
            for item in response['items']:
                
                comment = item['snippet']['topLevelComment']['snippet']['textOriginal']                
                
                repl = []
                if 'replies' in item:
                    replies = item['replies']['comments']
                    for reply in replies:
                        reply_text = reply['snippet']['textOriginal']
                        repl.append(reply_text)

                else:
                    repl = ["No reply"]
                
                video_comments.append({"Comments":comment,"Replies": repl})
            comments.append({"Channel_id":ch_id,"Video_id": vids,"Video_title":vid_title,"Comments":video_comments})

        except HttpError as e:
            if e.resp.status == 403:
                pass

    return comments



def get_video_info(video_ids):
    
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    #video_ids = video_ids[:100]
    all_video_stats = []
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute()

        for video in response['items']:
            ch_id = video['snippet']['channelId']
            Video_Id = video['id']
            Title = video['snippet']['title']
            Published_date = video['snippet']['publishedAt']
            
            try:
                Views = video['statistics']['viewCount']
                Likes = video['statistics']['likeCount']
                Comments = video['statistics']['commentCount']
                
                all_video_stats.append({"Channel_id": ch_id,"Video_id":Video_Id,"Video_Title":Title,"Uploaded_Date":Published_date,
                                                           "Total_Views":Views,"Total_Likes":Likes,
                                                                  "Total_Comments":Comments})
            except KeyError:
                continue
    
    return all_video_stats

def convert_comment_df(data):
    re_data = []
    for d in data:
        for i in d['Comments']:
            dt = dict()
            dt.update({'Channel_id':d['Channel_id'],'Video_id':d['Video_id'],
                      'Video_title':d['Video_title']})
            dt.update({'Comments':i['Comments'],'Replies':i['Replies'][0]})
            re_data.append(dt)
    return re_data
    


