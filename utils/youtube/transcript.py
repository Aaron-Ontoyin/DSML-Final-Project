from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if transcript:
            return transcript
    except Exception as e:
        raise ValueError("This video does not have a transcript.")

    transcript_list = YouTubeTranscriptApi.list_transcripts("video_id")
    for transcript in transcript_list:
        transcript = transcript.translate("en").fetch()
        if transcript:
            return transcript
