from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    bg_image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    #Logica para que se reemplaze el bg_image por si se ingresa otro o se actualiza
    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if this.bg_image != self.bg_image:
                this.bg_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)