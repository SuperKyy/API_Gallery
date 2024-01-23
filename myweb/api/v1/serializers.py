from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Gallery
from drf_extra_fields.fields import Base64ImageField

class GallerySerializer(ModelSerializer):
    Gambar = Base64ImageField(required=False)
    class Meta:
        model = Gallery
        fields = ['id','Judul','Gambar','Deskripsi']
    