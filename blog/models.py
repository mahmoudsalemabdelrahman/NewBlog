from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify  

# Create your models here.

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id, instance.id,  extension)
class Post(models.Model):
    author = models.ForeignKey(User, related_name=("blog"), on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    slug = models.SlugField(null=False, unique=True) 
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_upload)
    publish_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
