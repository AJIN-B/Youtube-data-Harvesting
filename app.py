
import streamlit as st
import pandas as pd
from Youtube_API import (get_channel_id,get_Channel_Information,
                         get_video_ids,get_comments_data,
                         get_video_info,convert_comment_df)
from sql import update_mysql
from mango import mdb_insert


#%%

st.set_page_config(page_title = 'Youtube Data Harvesting' , layout='wide')

colT1,colT2 = st.columns([10,28])
with colT2:
    st.title(' :blue[Youtube Data Harvesting]') 
    
st.markdown("<h3 style='text-align: center;'>&#x1F680 This app was created for harvest the data from the youbetube &#x1F680; </h3>", unsafe_allow_html=True)

colS1,colS2 = st.columns([1,5])
with colS2:
    link = st.text_input(" :orange[Enter The Youtube Channel link]")
    
colB1,colB2 = st.columns([10,10])
with colB2:
    searc = st.button('search')

if searc:
    if link:
        channel_id = get_channel_id(link)
        channel_data = get_Channel_Information(channel_id)
        Channel_link = channel_data['Channel_link']
        
        video_id = get_video_ids(channel_data['Playlist_id']) 

        comments_data = get_comments_data(video_id)
        comment_df = convert_comment_df(comments_data)

        get_video_info = get_video_info(video_id)


        st.markdown("---")
        
        colc1,colc2,colc3,colc4 = st.columns([7,7,7,10])
    
        with colc4:
            st.image(channel_data['Thumbnail'], width=200)
        
        with colc1:
            st.subheader(" :orange[Channel Name]")
            st.markdown(f"##### {channel_data['Channel_Name']}")
            
            st.subheader(' :orange[Channel link]' )
            link_html = f"<div style='text-align: left;'><a href={Channel_link} target='_blank'>Channel Link</a></div>"
            st.markdown(link_html, unsafe_allow_html=True)
            
        with colc3:
            st.subheader(" :orange[Total Subcribers]")
            st.markdown(f"##### {channel_data['Subcribers']}")
            
            st.subheader(" :orange[Total Views]")
            st.markdown(f"##### {channel_data['TotalViews']}")
            
        with colc2:
            st.subheader(" :orange[Created Date]")
            cre = channel_data['Created_Date'].split("T")[0]
            st.markdown(f"##### {cre}")
            
            st.subheader(" :orange[Total Videos]")
            st.markdown(f"##### {channel_data['TotalVideos']}")
        
        st.markdown("---")
        
        st.dataframe(pd.DataFrame(get_video_info).drop(['Channel_id','Video_id'],axis=1), width=1200, height=200)
        st.dataframe(pd.DataFrame(comment_df).drop(['Channel_id','Video_id'],axis=1), width=1200, height=200)
        
        colB1,colB2,colB3 = st.columns([5,7,10])
        
        with colB3:
            mang_bt = st.button(' :green[ upload to mangodb ]',on_click = mdb_insert(channel_data['Channel_Name'],channel_data,pd.DataFrame(get_video_info),pd.DataFrame(comment_df)))

        with colB2:
            sql_bt = st.button(' :green[ upload to sqldb ]',on_click=update_mysql(channel_data,get_video_info,comment_df))
        
        
        st.markdown("---")
        
        
        
        