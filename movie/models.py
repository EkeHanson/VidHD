from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    download_link = models.URLField()
    actors = models.CharField(max_length=1000)

    def __str__(self): 
        return self.title
    

class VideoFile(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='files/')  # 'files/' is the directory where files will be uploaded
    # You can add other necessary fields related to video files here
    
    def __str__(self):
        return f"Video file of {self.movie.title}"
