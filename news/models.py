import os

from django.db import models
from django.core.files import File
from versatileimagefield.fields import VersatileImageField
from pytubefix import YouTube


class News(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    image = VersatileImageField(
        upload_to="news/", width_field="width", height_field="height"
    )
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}"

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Songs(models.Model):
    title = models.CharField(max_length=1000)
    youtube_url = models.CharField(max_length=1000)
    audio_file = models.FileField(upload_to="songs/", null=True, blank=True)

    def download_video(self):
        try:
            yt = YouTube(self.youtube_url, on_progress_callback=self.on_progress)
            stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()  # Get the audio stream
            
            audio = stream.download(output_path="media/songs") 

            audio_filename = os.path.splitext(os.path.basename(audio))[0] + ".mp3"
            
            os.rename(audio, f"media/songs/{audio_filename}")

            with open(f"media/songs/{audio_filename}", "rb") as f:
                self.audio_file.name = f"songs/{audio_filename}"
                self.audio_file.save(audio_filename, File(f), save=True)
            os.remove(f"media/songs/{audio_filename}")
            
        except Exception as e:
            print(f"Error downloading audio: {e}")
    
    def on_progress(self, stream, chunk, bytes_remaining):
        """Callback for showing download progress."""
        print(f"Downloading: {bytes_remaining} bytes remaining")
    
    def save(self, *args, **kwargs):
        """Override save method to download when a new song is added."""
        if not self.audio_file:
            self.download_video()
        super(Songs, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Songs"
        verbose_name_plural = "Songs"
