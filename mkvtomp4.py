import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def mkv_to_mp4(input_file, output_file=None, ffmpeg_path="C:\\Program Files\\BlueStacks_nxt\\ffmpeg.exe"):
    """
    Converts an MKV file to MP4 format using FFmpeg.

    Parameters:
    input_file (str): The path to the input MKV file.
    output_file (str): The path to the output MP4 file. Optional.
                      If not provided, it will generate one based on the input file name.
    ffmpeg_path (str): The path to the ffmpeg executable. Default is set to BlueStacks path.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist. Please check the file path and try again.")
        return

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".mp4"

    try:
        command = [
            ffmpeg_path,
            '-i', input_file,
            '-c', 'copy',
            output_file
        ]
        subprocess.run(command, check=True)
        print(f"File successfully converted to: {output_file}")
    except subprocess.CalledProcessError as e:
        print("Error occurred while converting MKV to MP4:", e)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(title="Select the input MKV file", filetypes=[("MKV files", "*.mkv")])
    if not input_path:
        print("No input file selected. Exiting.")
    else:
        mkv_to_mp4(input_path)
