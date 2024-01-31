from rest_framework import serializers
from .models import Movie, VideoFile



class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'download_link', 'actors']
        

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = ['id', 'movie', 'file_path']  # Add other fields as needed
