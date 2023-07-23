from pytube import YouTube
import os
from pprint import pprint

def download_highest_quality(youtube_url, output_path):
    # Download video and audio in the highest quality
    youtube = YouTube(youtube_url, use_oauth=True, allow_oauth_cache=True)
    pprint(youtube.streams.all())
    video_itag = input("Enter the video itag")
    audio_itag = input("Enter the audio itag")
    video_stream = youtube.streams.get_by_itag(video_itag)
    audio_stream = youtube.streams.get_by_itag(audio_itag)

    tmo_video_filename = f"{youtube.title}_1.mp4"
    tmp_audio_filename = f"{youtube.title}_1.mp3"

    video_stream.download(output_path=output_path, filename=tmo_video_filename)
    audio_stream.download(output_path=output_path, filename=tmp_audio_filename)

    local_video_path = f"{os.path.join(output_path, tmo_video_filename)}"
    local_audio_path = f"{os.path.join(output_path, tmp_audio_filename)}"
    final_video_path = f"{os.path.join(output_path, youtube.title)}.mp4"
    return local_video_path, local_audio_path, final_video_path

def merge_video_audio(video_path, audio_path, output_path):
    # Use ffmpeg to merge video and audio while keeping the original video name
    os.system(f"ffmpeg -i \"{video_path}\" -i \"{audio_path}\" -c:v copy -c:a aac \"{output_path}\"")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    output_directory = "~/download/videos"

    tmp_video_path, tmp_audio_path, final_video_path = download_highest_quality(youtube_url, output_directory)

    merge_video_audio(tmp_video_path, tmp_audio_path, final_video_path)

    os.remove(tmp_video_path)
    os.remove(tmp_audio_path)

    print("Video downloaded and merged successfully!")