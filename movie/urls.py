from django.urls import path
from .views import MovieListAPIView, MovieDetailAPIView, VideoFileDownloadView


urlpatterns = [
    
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),

    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),

    path('download/<int:video_file_id>/', VideoFileDownloadView.as_view(), name='download_video_file'),

    # Add more URLs for other views if needed
]
