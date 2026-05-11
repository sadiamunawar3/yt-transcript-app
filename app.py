from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "Transcript API is running. Use /transcript?video_id=VIDEO_ID"
    })

@app.route("/transcript")
def get_transcript():
    video_id = request.args.get("video_id")

    if not video_id:
        return jsonify({
            "success": False,
            "error": "Missing video_id. Example: /transcript?video_id=dQw4w9WgXcQ"
        }), 400

    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)

        transcript_text = " ".join([snippet.text for snippet in fetched_transcript])

        return jsonify({
            "success": True,
            "video_id": video_id,
            "transcript": transcript_text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "video_id": video_id,
            "error": str(e),
            "error_type": type(e).__name__
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
