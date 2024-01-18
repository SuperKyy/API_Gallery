from django.db import models

# Create your models here.
class Gallery(models.Model):
    Judul = models.CharField(max_length=100)
    Gambar = models.ImageField(upload_to="img%y")
    Deskripsi = models.TextField()
    def __str__(self):
        return self.Judul
