from moviepy.editor import VideoFileClip

def generate_thumbnail(video_file):
    try:
        clip = VideoFileClip(video_file.file_path.path)
        thumbnail_path = f'thumbnails/thumbnail_{video_file.id}.jpg'  # Set your thumbnail path

        # Generate and save thumbnail
        clip.save_frame(thumbnail_path, t=5)  # Capture frame at 5 seconds (adjust as needed)
        
        # Save thumbnail path to the model
        video_file.thumbnail = thumbnail_path
        video_file.save()
        
        return thumbnail_path  # Return the thumbnail path if needed
    except Exception as e:
        # Handle exceptions, e.g., log error or display a message
        print(f"Error generating thumbnail: {e}")
        return None
