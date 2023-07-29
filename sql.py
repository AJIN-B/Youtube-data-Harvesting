import mysql.connector
import pandas as pd


def update_mysql(channel_data,video_df,comment_df):
    
    channel_id = channel_data['Channel_id']
    
    video_df = pd.DataFrame(video_df)
    comment_df = pd.DataFrame(comment_df)
    
    mydb = mysql.connector.connect(host='localhost',user='youruser',
                                   password='yourpassword',database ='yourdatabase')
    
    cursor = mydb.cursor()
    
    ch_schema = """
        CREATE TABLE IF NOT EXISTS Channel_Table (
            Channel_Id VARCHAR(30),
            Channel_Name VARCHAR(40),
            Playlist_Id VARCHAR(50),
            Created_Date DATETIME,
            Subscribers BIGINT,
            Total_Views BIGINT,
            Total_Videos BIGINT
        )
    """
    
    vi_schema = """
        CREATE TABLE IF NOT EXISTS Videos_Table (
            Channel_Id VARCHAR(30),
            Video_Id VARCHAR(30),
            Video_Title VARCHAR(100),
            Uploaded_Date DATETIME,
            Total_Views BIGINT,
            Total_Likes BIGINT,
            Total_Comments BIGINT
        )
    """
    
    comm_schema = """
        CREATE TABLE IF NOT EXISTS Comments_Table (
            Channel_Id VARCHAR(30),
            Video_Id VARCHAR(30),
            Video_Title VARCHAR(100),
            Comments VARCHAR(200),
            Replies VARCHAR(200)
        )
    """
    
    cursor.execute(ch_schema)
    cursor.execute(vi_schema)
    cursor.execute(comm_schema)
    
    cursor.execute("""
        INSERT IGNORE INTO Channel_Table (Channel_Id, Channel_Name, Playlist_Id, Created_Date, Subscribers, Total_Views, Total_Videos)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        channel_data['Channel_id'],
        channel_data['Channel_Name'],
        channel_data['Playlist_id'],
        channel_data['Created_Date'],
        channel_data['Subcribers'],
        channel_data['TotalViews'],
        channel_data['TotalVideos']
    ))
    

    
    for vindex, vrow in video_df.iterrows():
        cursor.execute("""
            INSERT IGNORE INTO Videos_Table (Channel_Id, Video_Id, Video_Title, Uploaded_Date, Total_Views, Total_Likes, Total_Comments)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            channel_id,
            vrow['Video_id'],
            vrow['Video_Title'],
            vrow['Uploaded_Date'],
            vrow['Total_Views'],
            vrow['Total_Likes'],
            vrow['Total_Comments']
        ))
    
        
        video_id = vrow['Video_id']
        
        for cindex, crow in comment_df[(comment_df['Channel_id'] == channel_id) & (comment_df['Video_id'] == vrow['Video_id']) ].iterrows():
            cursor.execute("""
                INSERT IGNORE INTO Comments_Table (Channel_Id, Video_Id, Video_Title, Comments, Replies)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                channel_id,
                video_id,
                crow['Video_title'],
                crow['Comments'],
                crow['Replies']
            ))
    
    

    mydb.commit()
    cursor.close()
    mydb.close()
    

