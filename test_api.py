import requests

# Test the API with a sample video ID (Rick Astley - Never Gonna Give You Up)
response = requests.get('http://localhost:5000/transcript?video_id=dQw4w9WgXcQ')

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# Check if transcript is present and is a string
if response.status_code == 200:
    data = response.json()
    if data['success'] and 'transcript' in data:
        print(f"Transcript length: {len(data['transcript'])} characters")
        print("First 200 characters of transcript:")
        print(data['transcript'][:200] + "...")
    else:
        print("Error in response")
else:
    print("Request failed")