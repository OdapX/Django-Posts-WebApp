from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='posts_pics')

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
