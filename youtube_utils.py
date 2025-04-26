from youtube_comment_downloader import YoutubeCommentDownloader
import re

def get_comments(video_url, max_comments=50):
    """
    Fetches comments from a YouTube video using the YoutubeCommentDownloader library.
    Takes in the video URL and max_comments to limit the number of comments.
    """
    downloader = YoutubeCommentDownloader()
    comments = []

    try:
        # Get comments sorted by top/popular instead of recent
        comment_generator = downloader.get_comments_from_url(video_url, sort_by=0)  # 0 = SORT_BY_POPULAR
        
        # Add error handling and timeout
        for comment in comment_generator:
            if isinstance(comment, dict) and 'text' in comment:
                comment_text = comment['text'].strip()
                if comment_text:  # Only add non-empty comments
                    comments.append(comment_text)
                    if len(comments) >= max_comments:
                        break
        
        if not comments:
            print(f"No comments found for URL: {video_url}")
            
    except Exception as e:
        print(f"Error fetching comments: {str(e)}")
        return []

    return comments


def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    pattern = r"(?:https?://)?(?:www\.)?(?:youtube\.com(?:/[^/]+)*/|\S*?v=)([A-Za-z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")