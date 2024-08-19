from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    if transcript:
        return transcript

    transcript_list = YouTubeTranscriptApi.list_transcripts("video_id")
    for transcript in transcript_list:
        transcript = transcript.translate("en").fetch()
        if transcript:
            return transcript
