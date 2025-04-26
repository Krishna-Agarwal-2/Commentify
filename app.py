# app.py
import streamlit as st
from youtube_utils import get_comments, extract_video_id
from analyzer import analyze_comment
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY", "")

st.title("🎥 YouTube Comment Analyzer")

video_url = st.text_input("📺 Paste a YouTube Video URL:")
max_comments = st.slider("Number of comments to analyze", 10, 100, 50)

if st.button("Analyze"):
    if not video_url:
        st.error("Please enter a YouTube video URL")
    else:
        try:
            video_id = extract_video_id(video_url)
            if not video_id:
                st.error("Invalid YouTube URL. Please enter a valid YouTube video URL")
            else:
                with st.spinner("Fetching comments..."):
                    comments = get_comments(video_url, max_comments)
                    
                    if not comments or len(comments) == 0:
                        st.error("No comments found. The video might have comments disabled or be restricted.")
                        st.info("Try another video or check if comments are enabled.")
                    else:
                        results = [analyze_comment(c) for c in comments if c]
                        if not results:
                            st.error("Could not analyze the comments. The comments may be empty or invalid.")
                        else:
                            df = pd.DataFrame(results)
                            st.success(f"Successfully analyzed {len(results)} comments!")

                            # Sentiment summary
                            if 'sentiment' in df.columns:
                                st.subheader("📊 Sentiment Distribution")
                                st.bar_chart(df['sentiment'].value_counts())

                            # Toxic vs clean
                            if 'toxic' in df.columns:
                                st.subheader("☢️ Toxic Comments")
                                toxic_pct = df['toxic'].mean() * 100
                                st.write(f"{toxic_pct:.2f}% comments are toxic")
                            else:
                                st.warning("No toxic data found!")

                            # Word cloud
                            if 'comment' in df.columns and not df['comment'].empty:
                                st.subheader("☁️ Most Common Words")
                                all_text = " ".join(df["comment"])
                                wc = WordCloud(width=800, height=300, background_color="white").generate(all_text)
                                plt.imshow(wc, interpolation="bilinear")
                                plt.axis("off")
                                st.pyplot(plt)
                            else:
                                st.warning("No comments available for word cloud generation")

                            # Display table
                            st.subheader("📃 Analyzed Comments")
                            st.dataframe(df)

        except Exception as e:
            st.error(f"Error occurred: {str(e)}")
            st.info("Please check if the video URL is correct and the video is accessible")
