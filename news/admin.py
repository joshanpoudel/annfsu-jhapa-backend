from django.contrib import admin
from .models import News, Songs
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ("title", "image_preview", "created_at", "updated_at")
    search_fields = ("title", "body")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    fields = ("title", "body", "image")
    readonly_fields = ("created_at", "updated_at", "height", "width")

    def image_preview(self, obj):
        """Return HTML to preview the image in admin."""
        if obj.image:
            return format_html(
                '<img src="{}" width="200" height="100" />', obj.image.url
            )
        return "No Image"

    image_preview.allow_tags = True

    def get_app_label(self):
        return ""



class SongsAdmin(admin.ModelAdmin):
    list_display = ("title", "youtube_url", "audio")
    search_fields = ("title", "youtube_url")
    fields = ("title", "youtube_url", "audio", "audio_file")
    readonly_fields = ("audio_file", "audio")
    
    def save_model(self, request, obj, form, change):
        if obj.pk:
            old_obj = Songs.objects.get(pk=obj.pk)
            if old_obj.youtube_url != obj.youtube_url:
                old_obj.audio_file.delete(save=False)
                obj.download_video()
        else:
            if not obj.audio_file:
                obj.download_video()
        
        super().save_model(request, obj, form, change)

    def audio(self, obj):
        if obj.audio_file:
            audio_url = obj.audio_file.url
            return format_html(
                '<audio width="120" height="90" controls>'
                '<source src="{}" type="audio/mp3">'
                "Your browser does not support the audio tag."
                "</audio>",
                audio_url,
            )
        return "No Audio"

    audio.short_description = "Audio"

    def delete_model(self, request, obj):
        if obj.audio_file:
            obj.audio_file.delete()
        obj.delete()

    

admin.site.register(Songs, SongsAdmin)
admin.site.register(News, NewsAdmin)
