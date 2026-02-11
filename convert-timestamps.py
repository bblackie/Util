'''
Can use Whisper Web to get a transcript from a video/audio file but the timestamps are not in a standard format. This script converts them to SRT format.

Need to know the framerate of the video/audio file to do the conversion.

The most common frame rates are:

- **23.976 fps** (film standard)
- **24 fps** (cinema)
- **25 fps** (PAL)
- **29.97 fps** (NTSC)
- **30 fps**
- **50 fps** / **60 fps** (high frame rate)

Can find the framerate using DaVinci Resolve or VLC Media Player.

'''


import json

# CONFIGURATION
fps = 24  # Change this to match your video's frame rate
input_file = 'transcripts/transcript.json'
output_file = 'transcripts/converted_timestamps.json'

def seconds_to_timecode(seconds, fps=24):
    """Convert seconds to timecode format HH:MM:SS:FF"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    frames = int((seconds % 1) * fps)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}:{frames:02d}"

# Load the JSON data from file
with open(input_file, 'r') as f:
    json_data = json.load(f)

# Convert all timestamps
converted_data = []

for entry in json_data:
    start_seconds, end_seconds = entry["timestamp"]
    converted_entry = {
        "timestamp": [
            seconds_to_timecode(start_seconds, fps),
            seconds_to_timecode(end_seconds, fps)
        ],
        "text": entry["text"]
    }
    converted_data.append(converted_entry)

# Print sample results
print(f"Processing with FPS: {fps}")
print(f"Total entries: {len(converted_data)}")
print("Sample converted timestamps:")
for i, entry in enumerate(converted_data[:5]):
    print(f"\nEntry {i+1}:")
    print(f"Start: {entry['timestamp'][0]}")
    print(f"End: {entry['timestamp'][1]}")
    print(f"Text: {entry['text'][:50]}...")

# Save full results to a file
with open(output_file, 'w') as f:
    json.dump(converted_data, f, indent=2)
     
     
print(f"\nMission complete. Converted timestamps saved to {output_file}")
