# YouTube Transcript API Flask App

A simple Flask application that fetches YouTube video transcripts using the YouTube Transcript API.

## Features

- Fetches transcripts from YouTube videos
- Returns clean, timestamp-free text in JSON format
- Ready for deployment on Render

## API Endpoint

### GET /transcript

Fetches the transcript for a YouTube video.

**Parameters:**
- `video_id` (required): The YouTube video ID (e.g., "dQw4w9WgXcQ")

**Response:**
```json
{
  "success": true,
  "video_id": "dQw4w9WgXcQ",
  "transcript": "Full transcript text here..."
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message"
}
```

## Local Development

1. **Clone or download this repository**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Test the API:**
   Open your browser and visit: `http://localhost:5000/transcript?video_id=dQw4w9WgXcQ`
   (Replace `dQw4w9WgXcQ` with any YouTube video ID that has captions)

## Deployment to Render

1. **Create a Render account** at [render.com](https://render.com)

2. **Connect your GitHub repository:**
   - Push this code to a GitHub repository
   - Connect Render to your GitHub account

3. **Create a new Web Service:**
   - Choose "Web Service" from the dashboard
   - Connect your GitHub repository
   - Set the following options:
     - **Runtime:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
   - Click "Create Web Service"

4. **Your API will be available at:** `https://your-app-name.onrender.com/transcript?video_id=VIDEO_ID`

## Requirements

- Python 3.7+
- Flask
- youtube-transcript-api
- gunicorn (for production)

## Notes

- Only works with YouTube videos that have captions/transcripts available
- Transcripts are returned as plain text without timestamps
- The app handles basic error cases (missing video_id, transcript not available)