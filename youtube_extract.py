from youtube_transcript_api import YouTubeTranscriptApi


def get_youtube_transcript(video_url):
    try:
        # Extract video ID from the YouTube URL
        video_id = video_url.split("v=")[-1].split("&")[0]

        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine the transcript into a single text block
        full_transcript = "\n".join([entry['text'] for entry in transcript])

        return full_transcript
    except Exception as e:
        return f"An error occurred: {e}"
    