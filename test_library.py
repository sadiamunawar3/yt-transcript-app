from youtube_transcript_api import YouTubeTranscriptApi

# Test with a known video that has transcripts
video_id = 'dQw4w9WgXcQ'  # Rick Astley

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print("Transcript fetched successfully")
    print(f"Number of items: {len(transcript)}")
    print(f"First item: {transcript[0]}")
    full_text = ' '.join([item['text'] for item in transcript])
    print(f"Full transcript length: {len(full_text)}")
    print(f"First 200 chars: {full_text[:200]}")
except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e)}")