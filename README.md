# MKVtoMP4 Converter

A simple Python tool to convert MKV video files to MP4 format using FFmpeg as the conversion engine.

## Features

- Simple graphical interface for file selection
- Direct container format conversion from MKV to MP4 without re-encoding
- Preserves original video and audio quality
- Fast conversion since only the container format is changed

## Requirements

- Python 3.x
- tkinter module (Python standard library)
- FFmpeg (default path is set to the BlueStacks installed version)

## Installation

1. Ensure Python 3.x is installed
2. Make sure FFmpeg is available, or use the version included with BlueStacks
3. Download the code

## Usage

1. Run the Python script
   ```
   python mkvtomp4.py
   ```
2. Select the MKV file you want to convert from the file dialog
3. The program will automatically generate an MP4 file with the same name in the same location

## Custom FFmpeg Path

If your FFmpeg is not in the default location, you can modify the `ffmpeg_path` parameter in the code:

```python
mkv_to_mp4(input_path, ffmpeg_path="your/ffmpeg/path")
```

## Advanced Usage

You can also import this module into your own Python programs:

```python
from mkvtomp4 import mkv_to_mp4

# Convert a single file
mkv_to_mp4("input.mkv", "output.mp4")

# Use a custom FFmpeg path
mkv_to_mp4("input.mkv", ffmpeg_path="C:\\path\\to\\ffmpeg.exe")
```

## Notes

- This program does not re-encode the video/audio, only converts the container format, which makes it fast but requires that the MP4 format supports the original file's codecs
- If conversion fails, you may need to use a full FFmpeg command with transcoding options
